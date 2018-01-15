---
Title: The Rules Engine Has Arrived, and It’ll Do for Behavior What XP Did for Data
Category: Blog Posts
Tags: Development, Rules Engine, Orders, Order Approvals
Slug: rules-engine-has-arrived
Authors: Todd Menier
Date: June 13th, 2016
---

The Platform Team is excited to announce the release of our shiny new rules engine, with its first application being to power **order approval** workflows.

## What's a rules engine?

Simply put, it's a system that executes rules. 

Okay... so what's a rule? 

In its simplest form, it's an if-then statement that is provided from the outside, rather than being “baked into” the engine itself. In the case of OrderCloud.io, we'll define the “thens” (starting with “order requires approval”) and allow you to define the “if”s via custom logic expressions. Effectively, we're going to allow you to extend platform behavior in much the same way `XP` allows you to extend the data model.

## Let's see an example.

Say you want every order over $200 with some specific `XP` value to require approval from a manager. You would first create a `UserGroup` containing all approving managers, then create a new `ApprovalRule`, setting the `ApprovingGroupID` to the ID of the new `UserGroup`, and setting `ApprovalRule.Expression` to this:

`order.Total > 200 and order.xp.MyCustomProperty = 'XYZ'`

A couple things to note:

- `order` supports the same properties as the Order model returned from /orders API endpoints, including `XP`.
- `=`, `<`, `<=`, `>=`, `<>` comparison operators are supported.
- `and`, `or`, and `not` logical operators are supported.
- `+`, `-`, `*`, `/` mathematical operators are supported.
- String values must be enclosed in straight single quotes.
- Date values must be enclosed in # symbols, e.g. `#6/15/2016#`
- Parentheses may be used to enclose sub-expressions and control order of execution.

## What about line items?

Glad you asked, because which products are being purchased, in what quantities, charged against which cost centers, etc, are very common in the world of approval rules. But line items are a collection, so we use **aggregate functions** to inspect them. 

Here's how you would require approval on all orders over $200 charged to cost center ABC:
`order.Total > 200 and items.any(CostCenter = 'ABC')`

That's pretty powerful, but it's more likely that you only care about the subtotal of just the line items matching your CostCenter condition. 
For this you can use the items.total function:

`items.total(CostCenter = 'ABC') > 200`

The condition inside the function (called a filter) can be more complex and contain and, or, etc. just like other parts of the expression:

`items.quantity(ProductID = 'P1' or ProductID = 'P2') > 5`

`items` supports a total of 4 functions:
- `items.any` (true if any item matches filter)
- `items.all` (true if all items match filter)
- `items.quantity` (compare result to a number)
- `items.total` (compare result to a dollar amount)

Speaking of functions, there is one defined on order:

`order.approved('id_of_some_other_rule')`

This one's powerful, because it allows you to set up multi-level approval workflows by chaining rules together. For example, in a larger organization, getting the approval from a department manager might not be enough, and a higher-level VP must also sign off.

There's nothing to stop you from using `and` or `or` in conjunction with multiple order.approved checks, if that's what's needed to support your flow. In fact, all valid elements of rule expressions can be mixed & matched as needed, allowing for very sophisticated rules to be supported:

`(order.Total > 20 and order.approved('rule_id_1')) or (not item.any(ProductID = 'QQQ') and approved('rule_id_2'))`

##A word of caution:

Rules are easy to write and very powerful, but can be tricky to debug when they don't work quite like you thought they would. While you can write very complex expressions, don't get more fancy with them than you need to. In some cases it might make sense to break a complex rule into 2 or more simpler rules. As always, we're here to help if you need guidance.

##What else can I do with this?

Now that you have a better understanding of the power of rules, you might be wondering what other areas of the platform might we apply them to. Here are a few ideas currently being kicked around:

- Custom validation (upon creating/editing things)
- Time-based approval rules (aggregated totals over past week/month/quarter, etc.)
- Applying discounts/markups
- Determining coupon eligibility
- Replenish inventory
- Fire off a notification via [Webhooks](https://documentation.ordercloud.io/integration-services/overview/your-first-webhook)

In short, order approvals are just the beginning. We envision this new rules engine playing a key role in our [“Flexibility over Features“]({filename}flexibility-over-features.md) platform strategy. Stay tuned!

