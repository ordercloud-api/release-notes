[All Releases](../../README.md) / [2017](../README.md) / [January](README.md) / v37-rc

# API 37 Release Candidate Notes 

Planned to be released to Production Tuesday, January 31st, 2017. _This date is subject to change_

## New Features
- We've added SSO via SAML **MORE DETAILS HERE** 

## Bug Fixes
- We've fixed an issue where, if a product on an lineitem has required specs, but no specs are filled out and there's no default, the line item create is successful. Instead, now an error is thrown with **MORE DETAILS HERE**.
- You should now be able to successfully set a string as a spec value on a lineitem if the product on the lineitem allows open text.
- If a buyer user has a private credit card **and** elevated roles (`FullAccess`, `CreditCardReader` & `OrderAdmin`, for example), you'll be able to create a payment on the private credit card without errors.
- Admin listing endpoints for assignments (`listProductAssignments`, etc) will no longer return assignments for deleted buyers. 
