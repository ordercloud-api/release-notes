[All Releases](../../README.md) / [2016](../README.md) / [December](README.md) / v33-rc 
# API v33 Release Candidate Notes 

Planned to be released to Prod TBD. {{Weekday}}, {{Month}} {{Date}}, {{Year}} at {{Hour PM/AM}} CST. _This date is subject to change_

## New Features
- We added a new User Prespective endpoint for returning a user's spending accounts. [Me/ListSpendingAccounts](qa-documentation link here)
- We've improved the information in our documentation about searchable/sortable properties and the order of precedence that these are applied in. [An example is X](doc link)
- We've added some performance enhacements around Products, particularly listing all products for a buyer. 

## Bug Fixes
- When you update a buyer company's default catalog, it actually updates now!
- We fixed an issue where, if you were authenticating as a user with claims other than `FullAccess`, the authentication performance was very poor.


## Client Libraries
- [Angular SDK](https://github.com/ordercloud-api/angular-sdk/releases/tag/v1.0.25-prerelease)