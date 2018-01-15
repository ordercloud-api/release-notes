---
Title: Leveraging Extended Properties in the Development of Custom eCommerce Apps
Category: Blog Posts
Tags: XP
Slug: leverage-xp
Authors: Steve Davis
Date: 3/09/2016
---

Recently I came across a post from one of my favorite developers and technology thought leaders that centered on how to work with some architecture patterns that drive so much of the development work that occurs today. His name is [Rob Conery](https://twitter.com/robconery), and he posts to his [blog](http://rob.conery.io/) frequently. I never miss a post, and listen to so much of what he publishes through his terrific podcast, [This Developer’s Life](http://thisdeveloperslife.com/). In his most recent post, [JSONB and PostreSQL: Work Faster By Ditching Migrations](http://rob.conery.io/2016/02/27/jsonb-and-postgresql/) he touched on a subject that resonated with our OrderCloud.io API strategy. In particular, how we manage our Extended Properties (`XP`) strategy, and ways to leverage it in the development of custom solutions.

Conery touches on the difficulties in choosing ORM patterns and his dislike of them, his love for SQL, and the choice to use good SQL project management, especially when the database begins to grow into a robust and production ready system. His answer, as he’s approaching in his latest project, is to work with JSONB at the top level. In doing so he’s able to use a schema-less approach to reduce friction and “nail the idea first”. I found his thought process enlightening.

With OrderCloud.io, we’ve actually enabled this very development process. Our data model is the product of over 16 years worth of intellectual property in B2B Commerce and Order Management. Add to that 100% exposure via our [REST API](https://devcenter.ordercloud.io/docs/api), and we believe we have the most robust and flexible B2B solution in the industry.

Still, we recognize that it can’t cover every conceivable scenario. We can’t predict every column in every table that your hypothetical database might need. That’s why we created our own schema-less solution with Extended Properties (XP) and exposed it on every API resource. We might not have `Product.YourSpecialDataPoint`, but we certainly do have `Product.xp.YourSpecialDataPoint`.

In your development projects you will encounter needs to customize the data model. With more rigid platforms like Magento you’re going to face challenges that require extensive work and timely development efforts.

    Our Extended Properties strategy allows you to overcome those obstacles and continue to create and develop fast.

Additionally, leveraging the tools in the [OrderCloud.io Dev Center](https://devcenter.ordercloud.io/) enables you to collaborate with our Architects and Developers to enhance the data model through suggestions. Developers are now a first-class customer. We seek out and encourage suggestions and so many of those suggestions will be born out of the usage of XP and the power it provides.

Learn more about [OrderCloud.io Extended Properties](https://devcenter.ordercloud.io/docs/guides/basic-api-features/extended-properties) here, or get started building on the OrderCloud.io Dev Center for free [here](https://devcenter.ordercloud.io/about).

