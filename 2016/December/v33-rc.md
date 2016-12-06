[All Releases](../../README.md) / [2016](../README.md) / [December](README.md) / v33-rc 
# API v33 Release Candidate Notes 

Planned to be released to Prod Tuesday, December 6th, 2016 at 8:00 PM CDT. _This date is subject to change_

## New Features
- We added a new User Prespective endpoint for returning a user's spending accounts. [Me/ListSpendingAccounts](http://qa-documentation.ordercloud.io/api-reference#MeSpendingAccounts)
- We've improved the information in our documentation about searchable/sortable properties and the order of precedence that these are applied in. [An example is the API Documentation around Addresses](http://qa-documentation.ordercloud.io/api-reference#MeAddresses)
- We've added some performance enhacements around Products, particularly listing all products for a buyer. 
- We now allow you to delete a product that is being used in an unsubmitted order. In submitted orders, the product information is retained, even after deletion.
- You can now use categories in the Rules Engine! For example, if you'd like to make a promotion that applies to products in only one category, you can use the following for a value expression: `items.any(product.incategory('xxx'))`

## Bug Fixes
- When you update a buyer company's default catalog, it actually updates now!
- We fixed an issue where, if you were authenticating as a user with claims other than `FullAccess`, the authentication performance was very poor.


## Client Libraries
- [Angular SDK](https://github.com/ordercloud-api/angular-sdk/releases/tag/v1.0.25-prerelease)