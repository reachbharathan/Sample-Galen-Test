Galen_demo
==========

Demonstration of web-responsive testing framework Galen.Galen concepts have been explored using static website.

To bring-up test website,follow these Steps

Installation of Demo website using jenkyll
----------------

Jekyll is a simple, blog-aware, static site generator. It takes a template directory containing raw text files in various formats, runs it through a converter (like Markdown) and our Liquid renderer, and spits out a complete, ready-to-publish static website suitable for serving with your favorite web server. Jekyll also happens to be the engine behind GitHub Pages, which means you can use Jekyll to host your project’s page, blog, or website from GitHub’s servers for free.

More info : http://jekyllrb.com/

To install,follow the steps here http://jekyllrb.com/docs/installation/

Checkout the theme for website

As Responsive design is needed for this demo,I picked the following theme

http://phlow.github.io/feeling-responsive/

Check-out the repo for the same

https://github.com/Phlow/feeling-responsive.git

switch to the feeling-responsive directory,and execute the command

jenkyll serve

Hit the localhost:4000 to see the website up & running

Execute the tests
-------------------
To execute the tests provided in this demo.

Pre-requisite

   Galen Installation(http://galenframework.com/)

After installing galen repo,Check out this repo and execute the following command

      galen test tests/responsive.test

If you want the report of the execution,you can include --report

      galen test tests/responsive.test --htmlreport reports

Reports can be found under same directory with name 'reports',after execution
