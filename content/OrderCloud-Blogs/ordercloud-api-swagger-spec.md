---
Title: How to Explore the OrderCloud.io API Using the Swagger Spec
Category: Blog Posts
Tags: Swagger Spec
Slug: ordercloud-api-swagger-spec
Authors: Connor O'Brien
Date: 9/15/2016
Status: Draft
---

We’re excited to announce that the [OrderCloud.io Swagger Spec](https://github.com/ordercloud-api/swagger/) is now available to the public. Now, you’re able to interact with OrderCloud.io through third-party applications without having to manually enter every route (for example, [Postman](https://www.getpostman.com)), as well as easily visualize the complexity of the OrderCloud.io API.

[Swagger](https://swagger.io/) is a JSON-based tool to describe an API. Their goal is to make it easier for both humans and machines not only discover, but also understand, the capabilities of APIs without needing to access the source code, documentation, or network inspection. By creating an OrderCloud.io Swagger spec, we’re making it easier for you to access and take advantage of our complex B2B data model.

The Swagger specification defines a set of files to describe APIs, which can then be utilized in a multitude of ways. APIs that adhere to the Swagger spec are more consumable, making them easier to read and utilize for developers.

Here are two ways you can explore the OrderCloud.io API using the Swagger Spec:

1. Visualize the API using the Chrome plug-in [Swagger UI Console](https://chrome.google.com/webstore/detail/swaggered/kaggdmjacnelneophkagkdljffninnpd?hl=en). Add the swagger.ed Google Chrome extension on your browser and open the [raw JSON format](https://raw.githubusercontent.com/ordercloud-api/swagger/master/ordercloud_swagger.json) of the OrderCloud.io API. When you select the plug-in from your browser, you’ll be able to see the entire data model, as well as all of the resources. Check out the OrderCloud.io API below:

[SCREENCAST THE COOL SWAGGER.ED ORDERCLOUD.IO API]

You can also explore further into each resource to see if it solves your needs:

[SCREENSHOT OF DETAILED INFO]

2. Import the Swagger spec into Postman to test API calls. It’s easy to import the OrderCloud.io Swagger spec into Postman. By doing so, you have the ability to test API calls and further explore the OrderCloud.io API. Simply clone the repository containing the Swagger definition to your local machine. Then, open the Postman Import box and hit the File tab. After you upload the Swagger file, Postman will take care of the rest. Once you get the success message, you’ll be good to go.

Explore away. Check out the OrderCloud.io Swagger spec here or 

<div class="postman-run-button"
data-postman-action="collection/import"
data-postman-var-1="35f40ce80f0934e33a9d"></div>
<script type="text/javascript">
  (function (p,o,s,t,m,a,n) {
    !p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); });
    !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild((
      (n = o.createElement("script")),
      (n.id = s+t), (n.async = 1), (n.src = m), n
    ));
  }(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));
</script>

