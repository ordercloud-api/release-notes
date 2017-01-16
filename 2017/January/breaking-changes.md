[All Releases](../../README.md) / [2017](../README.md) / [January](README.md) / breaking changes release

# API Breaking Changes Release Candidate Notes 

Planned to be released to Staging environment TBD. This public staging environment will be available for 30 days. The planned release to Production is TBD. _This date is subject to change_

## New Features
- Payments have a new boolean field, `Accepted`. Only users with the new `ProcessPayments` role will be able to create or update payments with `Accepted` set to `true`, and create Payment Transactions. 
- Order submit logic will validate `Payment.Accepted=true` and orders without an accepted payment will fail with {ERROR CODE}.
- Previously, any admin user could impersonate any buyer user. Going forward, {}
- `XP` must be an object containing name/value pairs, not a primitive or an array.
- Due to refactoring around our password hash algorithm, and since we do not store users' passwords ourselves, but simply a hash of the password, **users will need to reset their passwords through the normal password reset process before they can log into the OrderCloud devcenter or any OrderCloud apps**.
- Previously, you could filter a list based on `XP` that is *not* some value, but it would not return objects without that `XP` at all. 
- Added roles that control who can list or edit shipments. Now users with `ShipmentAdmin` *or* `OrderAdmin` can create or edit shipments. Users with `ShipmentReader` or `OrderReader` can get/list shipments.
- You can now filter product lists based on `CategoryID`. 
- `MesageSenders` is now correctly spelled as `MessageSenders` in the SDK.
- We are changing the route to register an anonymous user (previously called "Create From Temp User") to `PUT` `v1/me/temp`. This will help make our Swagger spec more flexible.
- Any buyer user can now list shipments for their own orders in a User Perspective route, `me/shipments`. No more need for elevated permissions!
- We have added a sub-object to Approvals to list Approving User information.
Example:
`{
"ApprovalRuleID": null,
"ApprovingGroupID": null,
"Status": "Pending",
"DateCreated": null,
"DateCompleted": null,
"ApprovingUser:
{ "ApproverID": null, "ApproverFirstName": null, "ApproverLastName": null, "ApproverUserName": null, "ApproverEmail": null }
"Comments": null
}`
- We have also moved approval comments out of the URL query string and into the request body. There is a maximum length of 2000 characters.




### Inventory Revamp
- Inventory is now a sub-object on the Product model.

#### Summary of Inventory Object Changes:

|            Old Inventory Object           |    New Product.Inventory Sub-Object    |
|-------------------------------------------|----------------------------------------|
| Product.InventoryEnabled                  | Product.Inventory.Enabled              |
| Product.InventoryNotificationPoint        | Product.Inventory.NotificationPoint    |
| Product.VarientLevelInventory             | Product.Inventory.VariantLevelTracking |
| Product.AllowOrderExceedInventory         | Product.Inventory.OrderCanExceed       |
| Product.InventoryVisible                  | *gone!*                                |
| `/products/:id/inventory`                 | *gone!*                                |
| Inventory.ID                              | *gone!*                                |
| Inventory.Name                            | *gone!*                                |
| number posted to `/product/:id/inventory` | Product.Inventory.Quantity             |
| Inventory.Available                       | Product.Inventory.AvailableQuantity    |
| Inventory.Reserved                        | Product.Inventory.ReservedQuantity     |
| Inventory.LastUpdated                     | Product.Inventory.LastUpdated          |
| `/products/:id/inventory`                 | *gone!*                                |

#### Summary of Inventory Action Changes:

|                  Action                 |  Quantity | ReservedQuantity | Available Quantity |
|-----------------------------------------|-----------|------------------|--------------------|
| Add Item To Order                       | No Change | Increases        | Decreases          |
| Submit, Submit for Approval, or Approve | No Change | No Change        | No Change          |
| Ship Item                               | Decreases | Decreases        | No Change          |
| Cancel or Decline Shipped Order         | No Change | Decreases        | Increases          |
| Remove Unshipped Line Item              | No Change | Decreases        | Increases          |
| Manually Increase Inventory             | Increases | No Change        | Increases          |

- **Quantity** is writeable and represents the total amount physically warehoused by the seller.
- **ReservedQuantity** is read-only and represents the total unshipped amount on live orders (submitted or unsubmitted).
- **AvailableQuantity** is read-only and is the difference Quantity and ReservedQuantity. It is usually the number you want to display to the buyer, and is the number checked when enforcing that orders cannot exceed inventory.

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


## Bug Fixes


## Client Libraries
- Save Security Profile assignment parameter order changes
- We've updated our terminology around claims vs roles to consistently use roles. You may need to check your token requests and make sure that you've updated your code to use roles.
