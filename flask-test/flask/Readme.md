# Flask:

Flask is a light-weight framework used to quickly create web applications.

## Flask Project Structure:

##### Package:
This refers to a Python package that contains your application’s code. I’ll talk more about setting up your app as a package in this chapter, but for now just know that the package is a sub-directory of the repository.
##### Module:
A module is a single Python file that can be imported by other Python files. A package is essentially multiple modules packaged together.

##### Orginization patterns

Basic sample structure (a few hundred lines of code), normally referred to as a __single module__
```
app.py                          -> Application logic 
> config.py                  -> Configuration such as secrets
> requirements.txt     -> A snapshot of the application's packages and dependencies
> static/                        -> Static .html, .css and .js files 
> templates/                -> Dynamic .html files (templates) 
```
A similar, but more advanced structure is referred to a __package__:
```
config.py                       ->  Configuration for the application
requirements.txt          ->    Snapshot of the application's dependencies
run.py                             -> It gets an instance of the application. This wouldn't be in production, but serves as a development server.
instance/                        
    config.py                    -> This file contains configuration variables that shouldn’t be in version control. This includes things like API keys and database URIs containing passwords. This also contains variables that are specific to this particular instance of your application. For example, you might have DEBUG = False in config.py, but set DEBUG = True in instance/config.py on your local machine for development. Since this file will be read in after config.py, it will override it and set DEBUG = True
yourapp/                        -> Your application. 
    __init__.py                  -> Brings together your application and its various components.
    views.py                     -> Defines the routes, (may) split into its own package.
    models.py                  -> Your application's models. This may be split into several modules in the same way as views.py.
    forms.py                     ->  
    static/                          -> This directory contains the public CSS, JavaScript, images and other files that you want to make public via your app. It is accessible from yourapp.com/static/ by default.
    templates/                  -> This is where you’ll put the Jinja2 templates for your app.
```

### Blueprint:
At some point you may find that you have a lot of related routes. If you’re like me, your first thought will be to split views.py into a package and group those views into modules. When you’re at this point, it may be time to factor your application into blueprints.

Blueprints are essentially components of your app defined in a somewhat self-contained manner. They act as apps within your application. You might have different blueprints for the admin panel, the front-end and the user dashboard. This lets you group views, static files and templates by components, while letting you share models, forms and other aspects of your application between these components. We’ll talk about using Blueprints to organize your application soon.

### Summary:
* Using a single module for your application is good for quick projects.
* Using a package for your application is good for projects with views, models, forms and other components.
* Blueprints are a great way to organize projects with several distinct components.
## Flask-SQLAlchemy:

Is a rather easy-to-use ORM to help handle queries and it abstracts business-logic.
However, there may be performance issues with using an ORM as poor routines (queries) may be generated.

