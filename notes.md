# General Notes Taken From The Documentation

# Starting the Project
Once Django is installed launch the following command in order to create a new Django project named *mysite*:

> django-admin startproject mysite

This command will create a folder which contains another folder and a python file.
The file, *manage.py*, is a command-line utility that permits to interact with the Django project in various ways. [Here's the complete documentation](https://docs.djangoproject.com/en/4.1/ref/django-admin/).
The outer root directory is a container fo the project and the name does not matter to Django, while the inner folder is the actual Python package for the project.
In order to run the project and view its status on the broswer locally, the following command is needed:

> python manage.py runserver

This command will return the local url needed to view the site.


### Note
The development server automatically reloads Python code, but some actions like **adding files don't trigger a restart**, so restarting the server is needed.


# Creating the App
Each application written in Django consists of a Python package that follows a certain convention. These apps can live anywhere on the Python path, if created in the same directory as where `manage.py` file is, the app can be imported ad its own top-level module, rather than a submodule of the app itself. To create the app, run the following command, making sure that you lunch it in the same directory there `manage.py` is:

> python manage.py startapp app_name

This command will create a folder where the app will be contained.

## URL Config
Needed in order to call the views created in `view.py`, all that's needed is to create a `url.py` in the app directory.
In this file the view functions can be called (as normal Python functions). But, before this, another step is needed: poin the root URLconf at the *app_name.urls* module. This is done in the `urls.py` file contained in *app_name* folder, including it to the path contained in the *urlpatterns*.
In `/project_name/urls.py`, where the rounting between files happens, the **include()** function allows referencing other URLconfs. Whenever Django encounters **include()**, it chops off whatever part of the URL matched up to that point and sends the maining string to the included URLcon for the further processing.


# Adding the App to the Django 'Intalled App' List
In order to make Django see the creating app and (don't got this pretty well) to adjourn this table of apps the following command is needed:

> python manage.py migrate

This command looks at the *INSTALLED_APPS* setting and creats any necessary database table according to the database settings in `project_name/settings.py` file and the database migrations shipped with the app.



# Models
For this part telling Django that the developing app is installed is mandatory. In order to do this just add the application in the *INSTALLED_APPS* in the `settings.py` file adding, for this particular case, the following line:

> 'pollsApp.apps.PollsappConfig',

The information about the names to put in the just written line is in `apps.py` (first word is *name*, then there is the class name at the end).
In `models.py` it's possible to create all the models needed which is done by Python classes. Each model has a number of class variables, each of which tapresents a database field in the model.
In this particular case *ForeignKey* tells Django each chouce is related to a single *Question*. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.

After having added the app to the installed ones list, run the following command:

> python manage.py makemirgations app_name

This command tells Django that some changes to the models were done and that this changes will be stored as a *migration*, they are files on disk.
So, the steps to make model changes:
1. change your models (in `models.py`)
2. To create migrations for those changes, run:
    > python amange.py makemigrations
3. To apply those changes, run:
    > python manage.py migrate



# API
Django gives you a free API (application programming interface).

## Playing on Terminal
From the terminal, it's possible to try the created models via Python shell.

> from app_name.models import Choice, Question
> Question.objects.all()            # this command shows all the question in the database

> from django.utils import timezone
> q = Question(question_text="What's new?", pub_date=timezone.now())
> q.save()

Onces all these is done, the first question is in the database. It's possible to access (and also change) question fields using the dot notation.
If the command used to show the database is called again the question stored is showed.

> Question.objects.all()
>> <QuerySet [<Question: Question object (1)>]>

As it's possible to see, the way the question is shown in the database it's not very meaningfull. To personalize it adding the *__str__()* method is needed. It's important to add this method, for various reasons (when calling the database by prompt and because objects' rappresentations are used throughout Django automatically-generated admin).

In order to create choices related to the question, first have the question saved in a variable (in this case will keeps being *q*). Then use the following commands:

> q.choice_set.all()
> q.choice_set.create(choice_text="The question you want to ask", votes=0)
> c = q.choice_set.create(choice_text="Other questions", votes=0)
> c.question        # Choice objects have API access to their related Question objects
>> <Question: The question yuo want to ask>
> q.choice_set.all()        # gives back all the setted up choices => django.db.models.query.QuerySet class
> q.choice_set.count()
> Choice.objects.filte(question__pub_date__year=1995)   # The API automatically follows relationships as far as it's needed, just use double underscores
> c = q.choice_set.filter(choice_text__startswith="Starting text")
> c.delete()        # this will eliminate the choice stored in the variable *c*



# Django Admin
For site managers and management.
To create a user who can login to the admin site, run the following command:

> python manage.py createsuperuser

This will give the possibility to create the superuser. Then, run the following command in order to activate the site and then to go to the admin page:

> python manage.py runserver

Remember to add the */admin* part at the end of the local given url.
Once logged in, it's possible to see a few types of editable content: *group* and *users*. They are provided by *django.contrib.auth*, the authentication framework shipped by Django.

## Making the App Modificable in the Admin Page
It has to be added to the `app_name/admin.py` file. In particular it has to be registered there.
Things to note here:

- the form is automatically generated from the Question model
- different model field types (**DateTimeFiled**, **CharField**) correspond to the appropriate HTML input widget. Each type of field knows how to display itself in the Django admin
- each **DateTimeField** gets free JavaScript shortcut (dates get a "Today" shortcut and calendar popup, and times get a "Now" shortcut and a convenient popup that lists commonly entered times)



# Views
In Django, web pages and other content are delivered by views which, each of them, are rapresented by a Python function (or method, in case of class-based views).
Views can take arguments and they are always in addition to *request*.
They all needs to be wired into the `app_name/urls.py` by adding the *path* calls.
Django loads the *mysite.urls* Python module by default because it's pointed to by the *ROOT_URLCONF* setting. It finds the variable named *urlpatterns* and traverses the patterns in order. After finding the match at *app_name/*, it strips the matching text ("app_name/") and sends the remainig text to the *polls.urls* URLconf for further processing.


### Templates
Creating a folder named *templates* in the creating app, Django will automatically look for templates there (this is done by Django for each of the installed apps under *INSTALLED_APPS*).

The template system uses dot-lookup syntax to access variable attributes. First, Django does a dictionary lookup on the object. If this fails, it tries an attribute lookup. If also the latter one fails, it tries a list-index lookup.


## Context
Like in the *views.index*, **context** is a dictionary mapping template variable names to Python objects.


# 404 Error
In order to do it *get_object_or_404* it's needed. If the passed object does not exists, it raises **404 Error**.
On the other hand, there also is *get_list_or_404*, which is the same this as the previously mentioned one, it just works on the lists, and if the passed list is empty it'll raise **404 Error**.


# Namespaces
In order to get Django know where to look app-wise talking for the *urlpatterns*, add the namespace.


# POST & CSRF
Whenever a **POST** mode is used, a worry about *Cross Site Request Forgeries* is needed. Django comes with a helpful system for protecting against it. In short, all **POST** forms that are targeted at internal URL should use the *{% csrf_token %} template tag.
Django also provides **request.GET** data in the same way, but in some cases is mandatory to ensure that data is only altered via POST call.

## Some More Information About POST
The following notes are about `details.html` file content.

- **request.POST** is a dictionary-like object that lets the access to submitted data by key name. **request.POST['choice']** returns the ID of the selected choice as a string
- **HttpResponseRedirect** takes a single argument: the URL which the user will be redirected. As good general web development practice, always return an **HttpsResponseRedirect** after dealing with POST data.
- **reverse()** function helps avoid having hardcode a URL in the view function. To it, the name of the view that it's wanted to pass control to it's passed



# Generic Views: Less Code is Better
This case is one that is common case of basic web development: getting data from the database according to the paramenter passe in the URL, loading a template and returning the rendered template. As it's so common, Django provides a shorctut called the "generic views" system. These *generic views* abstract common patterns to the point where you don't even need to write an app.

## Generic Views Used
**ListView** and **DetailView**, they respectively abstracts the concepts of "display a list of objects" and "display a detail page for a particular type of object". Moreover the **DetailView** generic view expects the primary key value captured from the URL to be called "pk", so it will replace *question_id*.
**Note:** for *DetailView* the *question* variable is provided automatically by the Django model *Question*. However, for *ListView*, the automatically generated context variable  is *question_list*. Providing *context_object_name* the latter is overrided, specifying that we want to use *latest_question_list* instead.




# Automated Testing
Testing operates at different levels. Some test might apply to a tiny detail, while others examine the overall operation of the software.
In `app_name/test.py` it's possible to create all the tests needed.
The created application so far has a bug: if the published date is in the future, was_published_recently() returns *True*, which it's not wanted. So a test to spot the bug was created. What happens in the test is the following:

 1. **manage.py test polls** looked for tests in the *pollsApp* application
 2. it founds a subclass of the **django.test.TestCase** class
 3. it created a special database for the purpose of testing
 4. it looked for test methods - ones whose names begin iwth *test*
 5. in **test_was_publish_recently_with_future_question** it created a *Question* instance whose *pub_date* field is in 30 days in the future
 6. ... and using the **assertIs()** method, it discovered that its **was_published_recently()** returns True, though we wanted it to return False

 ### Good Rules-Of-Thumb
 They include having:

 - a separate **TestClass** for each model of view
 - a separate test method for each set of conditions that should want to test
 - test method names that describe thei function


 The test informs us which test failed and even the line on which the failure occurred.

 ## Django Test Client
 Django provides a test **Client** to simulate a user interacting with the code at the view level.

 ## Django Test Views
 Here's some information about the test code written:

 1. **test_no_questions** doesn't create any questions, but checks the message "No polls are available." and verifies the **latest_question_list** is empty. Note that the **django.test.TestCase** class provides some additional assertion methods (in this project **assertContains()** and **assertQuerysetEqual()**).
 2. in **test_past_question**, it creates a question and verify that it appears in the list
 3. in **test_future_question**, it creates a question with a *pub_date* in the future.

 The database is reset for each test method, so the previously created questions are no longer there.

 ## Further Testing
 We saw testing about internal logic of a model, but that's not all about it. There are some "in-browser" framwork as [Salenium](https://www.selenium.dev/) to test the way the HTML actually renders in a browser. These tools allow to check not just the behaviour of the Django coed, but also, for example, of your JavaScript. Django includes **LiveServerTestCase** to facilitate integratoin with tools like Selenium.



 # Static Files
 Static files are such as images, JavaScript, or CSS.
 **django.conntrib.staticfiles** collects static files from each of the applications (and any other specified places) into a single location that can esasily be served in production.

 Because of how the **AppDirectoriesFinder** staticfile finder works, it's possible to refer to static files as `polls/style.css`, similar to how you reference the path for templates.

 **IMPORTANT NOTE**: we used a path like `static/polls` instead of just getting away by using `static` without subdirectories because of Django will chose the first static file it finds whose name matches. So, if there is a static file with the same name in a *different* application, Django would be unable to distinguish between them. The best way to ensure that Django points at the right one is by *namespacing* them which is done by putting those static files inside another directory named for the application itself.



 # Admin Site Interface
 Doing some changes it's possible to custom the way the admin page is displayed.

 # Overridding Django Default Admin Templates
 Any of Django's default admin templates can be overriden (even `admin/index.html` which is the most important page of the admin):

 - Create an `templates/admin` folder in the app
 - Copy the template from the default directory in the just created folder (or already existing)
 - Make any changes needed