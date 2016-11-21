[All Releases](../../README.md) / [2016](../README.md) / [November](README.md) / v32
# API v32-rc Release Candidate Notes 

Planned Release Date: November 21st, 2016 at 8:00 PM Central.

## New Features:
- You can now filter list Order queries on the BillingAddress and ShippingAddress subobjects. This works on both Order and Me.Order lists. EX:  `/orders?ShippingAddress.Street1=xyz`
- We've added true order-level shipping addresses. If a shipping address is set at the order level, all line items on the order will inherit that shipping address.
    + **PLEASE NOTE**: Previously, if all your line items had the same shipping address, any new line item would have the same shipping address. This is no longer true. Line items will *ONLY* inherit a shipping address when it is explicitly set at the order level.
    + There are no longer write-only address IDs on Order or Line Items; all of the following are now read/write:
        * Order.BillingAddressID
        * Order.ShippingAddressID
        * LineItem.ShippingAddressID
        * LineItem.ShipFromAddressID
- We've made several performance improvements around product history. 

## Bug Fixes:
- You can again list and delete security profile assignments for admin users. 
- Search results will now be accurate when listing categories using a depth parameter.
- You can no longer assign an invalid spec to a product; you will get an error on assignment.
