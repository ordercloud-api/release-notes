---
Title: How To Use Premium Search/Facet Search
Category: blog-posts
Tags: Search
Slug: Premium-Search
Status: draft
Authors: Todd Menier, Kate Reeher
Date: 4/7/2016
--- 

## Availability

"Premium" search must be turned on at both the Seller and Buyer level, and for now there is no endpoint or UI to do that. I created a sproc to do this, I imagine Todd or Jeff will typically be the ones to run it:

> exec EnableProductSearch @CompanyID

Here’s how to disable:

> exec EnableProductSearch @CompanyID, 0

For everyone who does not have premium search enabled, nothing changes. Poor man's search, etc, work as they do today.

## Building Indexes

A periodic WebJob (currently once per minute) will (re)build new/expired indexes in Elasticsearch, so there will always be a waiting period of one to several minutes (or longer for huge catalogs) after search is enabled for the index to actually be ready.

At any time after enabling search for someone, you can check on the progress by looking at the database:

>SELECT * FROM ProductSearchIndex

In-progress index (re)builds will have Status = "Building", and these columns are useful to see how far along it is: ProductsCompleted, TotalProducts, PercentComplete

## Searching

**Currently only Buyers get Elasticsearch-powered search via `me/products`**.
Using it for admin endpoints is a possible future enhancement, but I'm holding off until it's requested by someone. The API for search, filter, sort, etc. haven't changed - it's the same "fancy list" semantics used everywhere else, they're just entirely powered by Elasticsearch instead of SQL. Here's some improvements you should notice over poor man's search:

- Better results in terms of search hits and ranking. 
    "Better" is subjective - I'm guessing the beta group will help us determine how good it is in real-world scenarios. Elasticsearch has an endless amount of levers and knobs to play with, and it could take lots of iterations to get it just right.)
- Better performance. 
    Will be interesting to test against catalogs known to be slow.
- Searchable xp, including specifying specific fields and wildcards in searchOn (i.e. "xp.*" or "xp.nested.*")

## Defining Facets
Facet values are assigned to products via product.xp, but you must designate which xp fields should be considered facets. Do this by creating ProductFacet objects which, like products, are a seller-level concept. The usual CRUD patterns are supported, including ProductFacetAdmin and ProductFacetReader roles along with these endpoints:

>GET productfacets
GET productfacets/:id
POST productfacets
PUT productfacets/:id
PATCH productfacets/:id

The ProductFacet model has these properties:

- ID (must match product.xp field name unless XpPath is specified)
- Name
- XpPath (optional. specify if you want to use a different xp field than ID. particularly useful for nested xp fields, since an ID cannot contain a ".".)
- ListOrder
- MinCount (default is 1, meaning zero-count facet values won't be returned in list results. set to 0 if you want them all returned.)
- xp

**NOTE**:
Creating a new XP value via creation of a ProductFacet indexes the XP automatically for the Buyer the ProductFacet is used with. This does not extend to the Seller. If you want to search on an XP in the Seller, you will still need to index the XP.

## Using Facets

List endpoints will now include a Meta.Facets property. This is an array of facets, each containing an array of values with counts, all reflecting the current list context (search, filters, category, etc reflected in counts). Facet behaviors described in detail in this doc:

https://docs.google.com/document/d/1DC6GaPagpdjx5dOLZloND4olSIQCCYWtGzrMrIFRd58/edit?usp=sharing