[All Releases](../../README.md) / [2017](../README.md) / [March](README.md) / v43-rc
# API v1.0.43-rc Release Candidate Notes 

Planned to be released to Production on Wednesday, April 5th, 2017 at 7:30 PM Central. 

## Bug Fixes
- We now round the following to two decimal places:
    * `OrderPromotion.Amount`
    * `LineItem.LineTotal`
    * `Order.Subtotal`
    * `Order.ShippingCost`
    * `Order.TaxCost`
    * `Order.PromotionDiscount`
    * `SpendingAccount.Balance`
    * `Shipment.Cost`
    * `Payment.Amount`
    * `PaymentTransaction.Amount`
- We now return a useful and informative error message if you try to list `CatalogAssignments` without required parameters.
- We now return a useful and informative error message if you try to delete a user who has an open order outstanding.
- We now decrement `SpendingAccounts` on delete of a payment and not if it's just routed for approval. 
