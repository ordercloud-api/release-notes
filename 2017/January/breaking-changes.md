[All Releases](../../README.md) / [2017](../README.md) / [January](README.md) / breaking changes release

# API Breaking Changes Release Candidate Notes 

A public staging environment will be available starting on Sunday, April 2nd. The Breaking Change Release will be released to Production on May 4th at 7:30 PM Central.

You can access the staging environment using your production data and the following:

api: `https://stagingapi.ordercloud.io`

auth: `https://stagingauth.ordercloud.io`

devcenter: [https://staging-account.ordercloud.io](https://staging-account.ordercloud.io)

Production data will be copied down to the Staging environment weekly, on Sundays. In Staging, all webhooks will have their assignments deleted to disable them initially. Please update your webhooks and integrations in Staging to point somewhere other than Production ASAP. On the production release, no staging data will be transfered to production.

The planned release to Production is May 4th at 7:30 PM Central. _This date is subject to change_

## New Features
- Payments have a new boolean field, `Accepted`. Only users with the new `ProcessPayments` role will be able to create or update payments with `Accepted` set to `true`, and create Payment Transactions. 
- Order submit logic will validate `Payment.Accepted=true` and orders without an accepted payment will fail.
- Previously, any admin user could impersonate any buyer user. Going forward, an admin user must have the `BuyerImpersonation` claim in their security profile to impersonate buyer users.
- Due to refactoring around our password hash algorithm, and since we do not store users' passwords ourselves, but simply a hash of the password, **users will need to reset their passwords before they can log into the OrderCloud DevCenter or any OrderCloud apps**. When you authenticate to the Ordercloud API initially after this release, the only role your user will have is the `PasswordReset` role, and after you've reset your password, you'll need to re-authenticate to get your full array of roles. 
    + If you provide an application to users, we recommend have the application redirect any user who authenticates and only has the `PasswordReset` role to be redirected to a different view, where their password can be reset using the new `/me/password` endpoint.
    + Alternately, any user can trigger an email-based password reset, using the [Forgotten Password](https://staging-documentation.herokuapp.com/api-reference#PasswordResets) endpoint. 
- Due to the aforementioned password changes, DevCenter users will need to reset their DevCenter passwords by going to the "Forgot Password" link in DevCenter. Users will need to do this in the Staging Environment *and* in Prod after the production release. 
- Added roles that control who can list or edit shipments. Now users with `ShipmentAdmin` *or* `OrderAdmin` can create or edit shipments. Users with `ShipmentReader` or `OrderReader` can get/list shipments.
- Seller-side product lists (`v1/products`) can now be filtered on `CatalogID` and `CategoryID` (`CategoryID` is unique only within a Catalog, so you must specify both in order to filter on Category.)
- Buyer-side product lists (`v1/me/products`) that specify `CategoryID` can also specify `depth`, which can be an integer 1 or greater (`depth=1` means products directly assigned to category) or `all`. Default is `all`. 
- The Buyer-side order list for incoming orders (`v1/me/orders/incoming`) will now return all orders available for a user's approval.
- An order that requires approval can now be sent back to the submitting user by the approver user for editing and re-submission. See [Decline Orders](https://staging-documentation.herokuapp.com/api-reference#Orders_Decline) for more details. 
- We are changing the route to register an anonymous user (previously called "Create From Temp User") to `PUT` `v1/me/register`. This will help make our Swagger spec more flexible.
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
- The nested `Shipment.Items` collection has been removed, and shipment items are instead retrieved or saved via new endpoints, much like line items.
- `BuyerID` has been removed from routes, meaning you can list shipments across multiple buyers. 
- Shipment IDs are now seller-unique.
- All new fields listed below derive their values from corresponding LineItems, helping to avoid additional lookups when working with shipments.

| New Shipment Field                                        | Notes                          |
|-----------------------------------------------------------|--------------------------------|
| Shipment.Account                                          | writeable                      |
| Shipment.FromAddressID                                    | writeable                      |
| Shipment.ToAddressID                                      | writeable                      |
| Shipment.FromAddress                                      | nested object, read-only       |
| Shipment.ToAddress                                        | nested object, read-only       |
| ShipmentItem.UnitPrice                                    | read-only                      | 
| ShipmentItem.CostCenter                                   | read-only                      |
| ShipmentItem.DateNeeded                                   | nested object, read-only       |
| ShipmentItem.Product                                      | nested object, read-only       |
| ShipmentItem.Specs                                        | nested collection, read-only   |
| ShipmentItem.xp                                           | read-only                      |

| Old Endpoint                                               | New Endpoint                                         |
|------------------------------------------------------------|------------------------------------------------------|
| `GET v1/:BuyerID/shipments`                                | `GET v1/shipments`                                   |
| `GET v1/:BuyerID/shipments/:id`                            | `GET v1/shipments/:id`                               |
| N/A                                                        | `GET v1/shipments/:id/items`                         |
| N/A                                                        | `GET v1/shipments/:id/items/:orderID/:lineItemID`    |
| N/A                                                        | `POST v1/shipments/:id/items`                        |
| N/A                                                        | `PATCH v1/shipments/:id/items/:orderID/:lineItemID`  |

### Simplified Product and Category Assignments

|            New Properties           |                   Notes                    |
|-------------------------------------|--------------------------------------------|
| Catalog.Active                      |                                            |
| CatalogAssignment.ViewAllCategories |                                            |
| CatalogAssignment.ViewAllProducts   |                                            |
| CategoryAssignment.Visible          | Nullable, inherited from parent or catalog |
| CategoryAssignment.ViewAllProducts  | Nullable, inherited from parent or catalog |
| Product.DefaultPriceScheduleId      | Optional, but encouraged.                  |

- For a Buyer User to see a Product in the User Perspective (`GET v1/me/products`), *all* of the following must be true:
    * `Product.Active` is `true`
    * Product belongs to a Catalog where `Catalog.Active` is `true`
    * Buyer is assigned to this Catalog

- In addition, *one* of the following must be true:
    * In Buyer assignment to Catalog, `CatalogAssignment.ViewAllProducts` is `true`, **OR**
    * Product belongs to active Category in the catalog, Category is assigned to Buyer (or any Group the user is in), and `CategoryAssignment.ViewAllProducts` is `true`, **OR**
    * Product is assigned directly to Buyer (or any Group the user is in).

### Order URI Changes

Order IDs are unique to both the buyer and the seller. Hence, specifying buyerID in the URI is not technically necessary. With the recent addition of Suppliers, it became clear that regardless of your commerce role (Buyer, Seller, or Supplier) the only peices of information necessary to identify an Order are its ID and direction (`incoming` or `outgoing`). Therefore, we are changing all order related URIs as follows:

**Old:** `v1/buyers/:buyerID/orders/*`

**New:** `v1/orders/:direction/*`

**Notes:**
- This affects virtually all Order, Line Item, and Payment URIs. The only exception is Order List, which already use `incoming`/`outgoing`.
- Order Create (`POST v1/orders`) is the _only_ case where direction is not specified, because it's the only order releated action no one other than the "from" user can perform, hence it's always `outgoing`.


## Client Libraries

### [Javascript SDK]() 
- We've simplified our old SDK to be more vanilla Javascript, with a separate Angular SDK. This should make things a little more framework agnostic. :D
- We've updated our terminology around claims vs roles to consistently use roles. You may need to check your token requests and make sure that you've updated your code to use roles.
- `MesageSenders` is now correctly spelled as `MessageSenders` in the SDK.
- required parameters are passed in first, while optional parameters are passed in as an object with key value pairs
ex:
`ListProducts( {page:1, filters:{'xp.test':true})} )`
- Docs are now generated with the SDK, to make your life easier. Check them out at the bottom of the [readme](https://github.com/cobrien451/OrderCloud-JavaScript-SDK)!

### [Angular SDK]()
- As mentioned above, we've simplified our SDKs to be more framework agnostic, and there is now an Angular-specific SDK available.

### [C# SDK](https://github.com/ordercloud-api/csharp-sdk)
