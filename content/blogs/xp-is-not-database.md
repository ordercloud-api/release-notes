---
Title: So You Think You Know Your XP
Category: Blog Posts
Tags: XP
Slug: so-you-think-you-know-xp
Authors: Todd Menier
Date: 4/7/2016
--- 


This is not intended to be an introductory post. It’s less about learning something you don’t know and more about un-learning something you think you know. Let’s start with a pop quiz.

## What is XP?

1. An operating system recommended by 4 out of 5 OrderCloud.io developers.
2. An arbitrary JSON object that can be attached to any OrderCloud.io model.
3. Something you gain 20 of by throwing a curveball in Pokémon Go.
4. None of the above.

The correct answer of course is **4**. If you thought it was **1** or **3**, that’s understandable. (It’s only 3 out of 5, and a curveball is only good for 10.) If you answered **2**, welcome to your un-learning session.

Ok, so technically speaking **2** is technically true, technically. But that definition will cloud your thinking during the all-important data modeling phase of your app’s development. First off, saying it’s a JSON object is like saying `Order.Status` is a JSON property. Sure, that’s how it’s represented in the API, but it tells you nothing about what it is conceptually. Recall that `XP` stands for “e*X*tended Properties”. So let’s try this definition:

> A mechanism for adding properties to an object that my conceptual model needs but are not natively supported in OrderCloud.io.

That’s much better. It gets to the essence of what `XP` is and, perhaps more importantly, what it isn’t. Our `User` model has `FirstName`, `LastName`, and `Email`, but it doesn’t have `FavoriteColor`. If that’s an important data point for your app, just add it: `user.xp.FavoriteColor = “purple”`. We’ll store it and even index it, so later you can ask for a list of all users whose favorite color is purple, and we’ll send it to you faster than you can say “Skol Vikings”. But `XP` isn’t a dumping ground for large, deeply nested objects. It’s highly optimized for the “add a few extra data points” scenario and nothing more.

![Bart Simpson standing in front of a chalkboard where he's written "XP is not a database" over and over.](../images/xp-is-not-database.gif)

With that in mind, let’s go over some basic guidelines and best practices associated with XP.

## Know the data model, and use XP as a last resort. 

If you think `XP` properties are second-class citizens to native properties, well, they sort of are. They’re actually rather dumb. There’s no validation, no behavior, no referential integrity. Just data in, data out. Are you familiar with all the existing properties of the model you want to extend? Do you know their purpose and behavior? Are you aware that **IDs are writable**? That is perhaps one of the most underrated features of the API. If you’re using some back-office system as the master record for orders, you don’t need to add `order.xp.MyBackOfficeMasterRecordID`. Just write it to `order.ID`.

## Avoid storing big, text-y data. 

In the coming weeks we’ll be imposing some new size limits on XP. Don’t use it to store a blog. Also, `XP` is not optimized for full-text or natural language search. Things like `Product.Description` and `Order.Comment`s are better suited for this. Think smallish data points for XP.

## Avoid storing deeply nested objects.  

Think in terms of simple name/value pairs. You are allowed to store arbitrarily deep objects, but do so sparingly. A good example might be a Geocoordinates property on an `Address`. You might want to represent that with Latitude/Longitude sub-properties.

## Be careful with lists. 

Lists are dangerous, especially if it’s hard to say how long they could get. Something like `user.xp.NamesOfPets` should be ok. Avoid lists of objects. This again touches on the importance of knowing the data model. Are you sure the object doesn’t already have a list of child objects that might fit your needs?

## Avoid storing repeated “lookup” data. 

We recently discovered that a client had been storing objects like this in `XP` of every Order submitted through their app: `“MyNestedObject”: { “ID”: “xyz123”, “name”: “my thing name”, “description”: “my lengthy description” }`. In their thousands of processed orders, guess what was true about all orders with the same `xp.MyNestedObject.ID`? Yep, they all had the same name and description too. Not only does this make DBAs cry, but it’s potentially bad for the end user as well. What if a misspelling was discovered in the description? It would need to be updated in thousands of places. This can be avoided by storing just `MyNestedObjectID` in `order.xp`, and storing the lookup data associated with that ID elsewhere.

## Avoid storing global configuration data. 

Virtually all apps have some sort of global config data. Ask yourself: do you really need the API to store that for you? Assuming it rarely changes and you don’t need to build any sort of UI around changing it, it’s perfectly fine to store this along side your front-end code, such as in a JSON object in a js file.

## **Never, *ever* store highly sensitive data**. 

Don’t put passwords in `XP`. As for credit card numbers, it’s not only a bad idea, it’s a violation of our terms & conditions.

## Remember that OrderCloud.io is not a complete solution. 

You wouldn’t tell an end-customer that our API alone is their new commerce solution, point them to [Postman](https://www.getpostman.com/) or [Fiddler](https://www.telerik.com/fiddler) and be on your way. But just as a custom front-end needs to be built in order to have something useful, it’s quite possible that a great solution will require some additional back-end pieces as well. Fortunately for you, we live in an age of microservices, and if your custom data needs grow beyond bolting a few extra properties onto existing objects, you have a number of great options available in the Cloud. Google’s [Firebase](https://firebase.google.com/), Amazon’s [DynamoDB](https://aws.amazon.com/dynamodb/), and Microsoft’s [DocumentDB](https://azure.microsoft.com/en-us/services/documentdb/) are just a few. 

## When it doubt, ask. 

We want nothing more than for the apps you build on OrderCloud.io to be a smashing success. To that end, we’re here to help. We have both free and paid support options available. Use them if you feel you don’t have all the answers you need, especially in the critical early stages of development.

We like to tout `XP` as the poster child of our [“Flexibility over Features“]({filename}flexibility-over-features.md) matra. But like any tool, it is important to recognize its purpose, as well as its limitations.

