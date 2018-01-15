---
Title: Flexibility Over Features
Category: blog-posts
Tags: Integrations
Slug: flexibility-over-features
Authors: Todd Menier
Date: 4/7/2016
--- 


    "That's an integration concern."

It's a phrase I utter often when new platform features are suggested. Although I try not to utter it on days I need to leave early. Some might question my motives.

When I think about Four51's transformation from a SaaS company to a PaaS company, I'm often reminded of why we embarked on this journey in the first place. I think I can sum it up in 3 words: too many checkboxes. (You thought I was going to say flexibility over features. I'll get to it.) Our SaaS app simply couldn't do enough things so satisfy everyone's needs. Custom themes on the buyer side weren't enough. Long lists of configuration options on the admin side (those pesky checkboxes) became daunting, and still didn't provide all the custom behavior needed. Simply put,  B2B is hard. Much harder than B2C, because there is much greater variability in requirements from customer to customer. We needed a better way, but without abandoning our commitment to the single-instance, multi-tenant, cloud-hosted architecture that’s served us (and our customers) so well since before The Cloud was even a thing.

So the decision was made to chop the head off the SaaS product and expose the entire data model and its behavior via a RESTful API. We now offer what we believe is the “sweet spot” between SasS and custom development. Now, we didn't simply kick the old UI to the curb and say "here ya go world, go figure it out." We actually ramped up our development team and invested heavily in UI components, integration components, SDKs in multiple languages, “seed” applications, extensive documentation and tutorials, and a suite of tools under our Dev Center umbrella to enable things like GitHub integration and one-click app deployments. Custom apps in record time, all built atop of a proven, time-tested platform.

But going down this path required a change in mindset, especially as it applies to the core platform. We’re no longer a car; we’re an engine. If you want top-of-the-line headlights, you can have them, but there there others who specialize in them and make them better than we ever could. (Besides, how deep under the hood do you want go to change a bulb?) What we do well is B2B eCommerce and order management. This has been our core competency for over 15 years. We’ve discovered countless nuances and solved them via constant evolution of our data model. Anything outside that domain is subject to re-evaluation. Take a seemingly simple example: email. Sure, we can build and send off an email directly from the platform in a few lines of code (and we did that for years). But can we offer a template management system or maintain a whitelist status (there’s more to this stuff than you might imagine) to rival MailChimp? No. MailChimp does email better than we ever could, and they offer their services via their own RESTful API. Four51’s integration engineers work tirelessly to select the best experts in their respective domains and provide out-of-the-box integration components to our customers.

Do all these newfound “integration concerns” mean the core platform is “done”? Not by a long shot. Mature, yes. Done, no. We’ve simply redefined how we prioritize enhancements to it. Which brings us to Flexibility Over Features. It’s a mantra that guides our platform roadmap and keeps us focused on what we do best. As flexible as our data model is, we still encounter situations where it’s too rigid to solve certain problems elegantly. Removing constraints and broadening the possibilities of how our data model can be utilized receive top priority on our platform agenda.

Enough with mantras and buzzwords and other abstract rantings. What are some real-world examples where we’ve put this idea to work? Extended Properties, A.K.A. “xp”, is a perfect example. Most objects in the data model now include some core set of attributes, along with an extension attribute called xp. For example, a User object contains ID, FirstName, LastName, Email, and about a half dozen other attributes. But it doesn’t include Gender, because presumably that’s not a useful datapoint in the vast majority of B2B scenarios. If it’s relevant in yours, no problem - just add it:

`user.xp.Gender = “female”`

Of course, the platform has no inherent knowledge of what “Gender” means, so it provides no special behavior around it, but it’s happy to accept this conjured-up attribute, store it, index it, and make it searchable/sortable when you get a list of Users. Need specialized behavior around it? That’s an integra….you get the idea.

Our roadmap is loaded with ideas that fit the Flexibility Over Features mantra. Currently in the works is a robust new system of Webhooks, which will provide a powerful new way to integrate with external systems via HTTP. Essentially, these systems will be able to subscribe to events that occur within the platform (order submitted, product created, etc.) and respond to them in near real time. You can already “pull” data from the platform by calling the API; think of this as a “push” mechanism, where you get what you want from the platform when it occurs, avoiding the need to periodically poll the API.

Another major project in the works is a new Rules Engine. Its first application will be a massive overhaul of Order Approvals, adding a greater degree of robustness and flexibility to this core feature than we’ve ever dreamed up in the past. It’ll support text-based logic expressions (no CompSci degree required), arbitrary approval workflows, time-based rules against aggregated totals, and much more. Look for it in the coming months.

OrderCloud is constantly evolving. But we’ve learned that we don’t need to be experts at everything. We believe the best B2B solutions on the planet will not be built from scratch nor offered out-of-the box via SaaS. Rather, they’ll be assembled out of distributed, best-in-breed components. We’re the engine. We don’t make tires or steering wheels or leather-upholstered bucket seats. But we can help you assemble all the best parts, and we think the result will be the shiniest, fastest car on the block.
