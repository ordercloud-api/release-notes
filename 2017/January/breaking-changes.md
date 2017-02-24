[All Releases](../../README.md) / [2017](../README.md) / [January](README.md) / breaking changes release

# API Breaking Changes Release Candidate Notes 

Planned to be released to Staging environment TBD. 

This public staging environment will be available for 30 days. Production data will be copied down to the Staging environment once, on TBD. In Staging, all webhooks will be disabled initially. Please update your webhooks and integrations in Staging to point somewhere other than Production ASAP.

The planned release to Production is TBD. _This date is subject to change_

## New Features
- Payments have a new boolean field, `Accepted`. Only users with the new `ProcessPayments` role will be able to create or update payments with `Accepted` set to `true`, and create Payment Transactions. 
- Order submit logic will validate `Payment.Accepted=true` and orders without an accepted payment will fail with **ERROR CODE**.
- Previously, any admin user could impersonate any buyer user. Going forward, **MORE DETAILS HERE**.
- Due to refactoring around our password hash algorithm, and since we do not store users' passwords ourselves, but simply a hash of the password, **users will need to reset their passwords before they can log into the OrderCloud devcenter or any OrderCloud apps**. When you authenticate to the Ordercloud API initially after this release, the only role your user will have is the `PasswordReset` role, and after you've reset your password, you'll need to re-authenticate to get your full array of roles. 
    + If you provide an application to users, we recommend have the application redirect any user who authenticates and only has the `PasswordReset` role to be redirected to a different view, where their password can be reset using the new `/me/password` endpoint.
    + Alternately, any user can trigger an email-based password reset, using the [Forgot Password]() endpoint. 
- Added roles that control who can list or edit shipments. Now users with `ShipmentAdmin` *or* `OrderAdmin` can create or edit shipments. Users with `ShipmentReader` or `OrderReader` can get/list shipments.
- Seller-side product lists (`v1/products`) can now be filtered on `CatalogID` and `CategoryID` (`CategoryID` is unique only within a Catalog, so you must specify both in order to filter on Category.)
- Buyer-side product lists (`v1/me/products`) that specify `CategoryID` can also specify `depth`, which can be an integer 1 or greater (`depth=1` means products directly assigned to category) or `all`. Default is `all`. 
- An order that requires approval can now be sent back to the submitting user by the approver user for editing and re-submission. **MORE DETAILS HERE**
- We are changing the route to register an anonymous user (previously called "Create From Temp User") to `PUT` `v1/me/temp`. This will help make our Swagger spec more flexible.
- Any buyer user can now list shipments for their own orders in a User Perspective route, `me/shipments`. No more need for elevated permissions!
- In order to encourage best practices, only group-level and buyer-level assignments will be allowed for the following resources:
    + Products
    + Categories
    + Promotions
    + Cost Centers
    + Message Config

**If there are existing user-level assignments for any of the above, you must convert them to group- or buyer-level before the production release date**.

- `OrderApproval` now contains nested `Approver` object containing all details of the approving user. Example:
````
{
    "ApprovalRuleID": "...",
    "ApprovingGroupID": "...",
    "Status": "Pending",
    "DateCreated": "...",
    "DateCompleted": "...",
    "Approver":
    {
        "ID": "...",
        "FirstName": "...",
        "LastName": "...",
        "UserName": "...",
        "Email": "...",
        "Active": "...",
        "xp" : { ... }
    },
    "Comments": "..."
}
````
- We have also moved approval comments out of the URL query string and into the request body. There is a maximum length of 2000 characters.

### Inventory Revamp
- Inventory-related data points on `Product` are being moved into a nested `Inventory` object.

#### Summary of Inventory Object Changes:

| Old                                       | New                                    |
|-------------------------------------------|----------------------------------------|
| Product.InventoryEnabled                  | Product.Inventory.Enabled              |
| Product.InventoryNotificationPoint        | Product.Inventory.NotificationPoint    |
| Product.VarientLevelInventory             | Product.Inventory.VariantLevelTracking |
| Product.AllowOrderExceedInventory         | Product.Inventory.OrderCanExceed       |
| Product.InventoryVisible                  | *removed*                              |
| `/products/:id/inventory` resource        | *removed*                              |
| Inventory.Available                       | Product.Inventory.QuantityAvailable    |
| Inventory.LastUpdated                     | Product.Inventory.LastUpdated          |
| Inventory.ID                              | *removed*                              |
| Inventory.Name                            | *removed*                              |
| Inventory.Reserved                        | *removed*                              |
| `/products/:id/inventory`                 | *removed*                              |

#### Summary of Inventory Behavioral Changes:
- `Product.Inventory.QuantityAvailable` is writable.
  - `PATCH v1/products/:id { "Inventory": { "QuantityAvailable": 999 } }` is the preferred way to manually set inventory.
- `QuantityAvailable` is deducted on order submit or final order approval (whichever point order status changes to `Open`).
- `QuantityAvailable` is adjusted when quantity changes are made to line items on `Open` orders.
- `QuantityAvailable` is validated, but not adjusted, when items are added or quantities change on `Unsubmitted` orders. A 400 error occurs if item quantity exceeds available inventory and `Product.Inventory.OrderCanExceed` is false.
- `QuantityAvailable` is always re-validated per the rules above on order submit.

### Shipment Changes
- We have removed Shipment.Items, and shipped items are instead retrieved or updated via new endpoints, much like line items.
- BuyerID has been removed from routes, meaning you can list shipments across multiple buyers. 
- Shipment IDs are now seller-unique.
- Many of the new fields on Shipment and ShipmentItem are derived from LineItems, to increase performance on lookup.

|                    New Shipment Object                    |                     Notes                     |
|-----------------------------------------------------------|-----------------------------------------------|
| Shipment.ShippingAccount                                  | writeable, default derived from LineItems [1] |
| Shipment.ShippingAddressID                                | writeable, default derived from LineItems [1] |
| Shipment.ShippingAddressID                                | writeable, default derived from LineItems [1] |
| Shipment.ShipFromAddressID                                | read-only, derived from LineItems             |
| Shipment.ShippingAddress                                  | read-only, derived from LineItems             |
| Shipment.ShipFromAddress                                  | read-only, derived from LineItems             |
| ShipmentItem.UnitPrice                                    | read-only, derived from LineItems             |
| ShipmentItem.CostCenter                                   | read-only, derived from LineItems             |
| ShipmentItem.DateNeeded                                   | read-only, derived from LineItems             |
| ShipmentItem.Product                                      | read-only, derived from LineItems             |
| ShipmentItem.Specs                                        | read-only, derived from LineItems             |
| ShipmentItem.xp                                           | read-only, derived from LineItems             |
| `GET` `v1/shipments`                                      |                                               |
| `GET` `v1/shipments/{id}`                                 |                                               |
| `GET` `v1/shipments/{id}/items                          ` |                                               |
| `GET` `v1/shipments/{id}/items/{orderID}/{lineItemID}   ` |                                               |
| `POST` `v1/shipments/{id}/items                         ` |                                               |
| `PATCH` `v1/shipments/{id}/items/{orderID}/{lineItemID}`  |                                               |

[1] Updating these on the Shipment will update the underlying LineItem as well.

### Simplified Product and Category Assignments

|            New Properties           |                   Notes                    |
|-------------------------------------|--------------------------------------------|
| Catalog.Active                      |                                            |
| CatalogAssignment.ViewAllCategories |                                            |
| CatalogAssignment.ViewAllProducts   |                                            |
|-------------------------------------|--------------------------------------------|
| CategoryAssignment.Visible          | Nullable, inherited from parent or catalog |
| CategoryAssignment.ViewAllProducts  | Nullable, inherited from parent or catalog |
|-------------------------------------|--------------------------------------------|
| Product.DefaultPriceScheduleId      | Optional, but encouraged.                    |

- For a Buyer User to see a Product in the User Perspective (`GET` `/me/products`), the following must *all* be true:
    * `Product.Active` = `true`
    * Catalog exists where:
        + `Catalog.Active` = `true`
        + `Buyer` is assigned via `CatalogAssignment`
        + `Product` is assigned via `ProductCatalogAssignment`
- For a Buyer User to see a Product in the User Perspective (`GET` `/me/products`), *one* of the following must be true:
    * `CatalogAssignment.ViewAllProducts` = `true`, **OR**
    * Category exists in Catalog where:
        + `Active` = `true`
        + Product assigned via `CategoryProductAssignment`
        + `CategoryAssignment` exists where:
            - `Buyer`, `User`, or `Group` matches the user
            - `ViewAllProducts` = true for first non-null setting up the tree
        + `ProductAssignment` exists for Buyer, User, or any Group the user belongs to. (`PriceScheduleID` not required)
- me/products > me/catalog/products



## Bug Fixes


## Client Libraries
- Save Security Profile assignment parameter order changes
- We've updated our terminology around claims vs roles to consistently use roles. You may need to check your token requests and make sure that you've updated your code to use roles.
- `MesageSenders` is now correctly spelled as `MessageSenders` in the SDK.
