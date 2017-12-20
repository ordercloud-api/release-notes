
# OrderCloud API Release Notes

Release Notes for the [OrderCloud API](). 

[![Build Status](https://travis-ci.org/ordercloud-api/release-notes.svg?branch=master)](https://travis-ci.org/ordercloud-api/release-notes)


The release notes site can be found at [https://ordercloud-api.github.io/release-notes/](https://ordercloud-api.github.io/release-notes/)


> If you are just looking for the simple **markdown** version of an OrderCloud.io release note, look to [the content folder](/content). They are organized by release version number.



## Static Site

This github.io site is generated using a [Pelican](https://blog.getpelican.com/) static site.

### Generation & Deploy Process 

To add a new release note, create a markdown-formatted version and put it in [the content folder](/content). Follow the established metadata formatting, so that Pelican will correctly generate it. 

To add a new blog article,create a markdown-formatted version and put it in [the blogs folder](/content/blogs). 

> To keep an article as a draft, add the `Status:Draft` line to your post metadata.

> To set a future publish date, set the `Date:` line in the metadata to the desired future date. 

To build locally, see [the Pelican documentation](http://docs.getpelican.com/en/stable/publish.html#). This will require [installing Pelican](http://docs.getpelican.com/en/stable/install.html) locally. See required python packages in the [requirements](requirements.txt). You may also need to [initiate the submodules](https://stackoverflow.com/a/3796947/173416) before the build works.

Please note that the `Output` folder is listed in the .gitignore file. This is to keep the source code uncluttered with the generated files from local builds. The site is generated during the Travis.ci process, as outlined below, and the static site output is avaible in the `gh-pages` branch.

The [2016](/2016) and [2017](/2017) folders and their content are historical release notes, kept to avoid link rot.

When you're ready to publish the content you've created, merge this content into the `master` branch of the release-notes repo. On any push to `master`, [Travis CI](https://travis-ci.org/ordercloud-api/release-notes.svg?branch=master) will build the Pelican site, generating the html site. The generated output will be placed in the `gh-pages` branch, where the site will be published with [Github Pages](https://help.github.com/categories/github-pages-basics/).

Currently, we are using the [foundation-default-colours](https://github.com/getpelican/pelican-themes/tree/master/foundation-default-colours) theme for Pelican. 

Ideally, I'd like to get the [Filetime from Git](https://github.com/getpelican/pelican-plugins/tree/master/filetime_from_git) plugin working, so that the date/datemodified meta doesn't need to be set manually. 


