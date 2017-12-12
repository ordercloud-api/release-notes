
# OrderCloud API Release Notes

Release Notes for the [OrderCloud API](). 

[![Build Status](https://travis-ci.org/ordercloud-api/release-notes.svg?branch=master)](https://travis-ci.org/ordercloud-api/release-notes)


The release notes site can be found at [https://ordercloud-api.github.io/release-notes/](https://ordercloud-api.github.io/release-notes/)


> If you are just looking for the simple markdown version of an OrderCloud.io release note, look to [the content folder](/content). They are organized by release version number.



## Static Site

This github.io site is generated using a [Pelican](https://blog.getpelican.com/) static site.

### Generation & Deploy Process 

To add a new release note, create a markdown-formatted version and put it in [the content folder](/content). Follow the established metadata formatting, so that Pelican will correctly generate it. 

When the commit with the new release note is in the `master` branch of the release-notes repo, [Travis CI](https://travis-ci.org/ordercloud-api/release-notes.svg?branch=master) will build the Pelican site, generating the html site. The generated output will be placed in the `gh-pages` branch, where the site will be published with [Github Pages](https://help.github.com/categories/github-pages-basics/).

Currently, we are using the [Gum](https://github.com/getpelican/pelican-themes/tree/master/gum) theme for Pelican. 

Ideally, I'd like to get the [Filetime from Git](https://github.com/getpelican/pelican-plugins/tree/master/filetime_from_git) plugin working, so that the date/datemodified meta doesn't need to be set manually. 


