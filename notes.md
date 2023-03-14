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

This command looks at the `INSTALLED_APPS` setting and creats any necessary database table according to the database settings in `project_name/settings.py` file and the database migrations shipped with the app.



# Models
For this part telling Django that the developing app is installed is mandatory. In order to do this just add the application in the `INSTALLED_APPS` in the `settings.py` file adding, for this particular case, the following line:

> 'pollsApp.apps.PollsappConfig',

In `models.py` it's possible to create all the models needed which is done by Python classes. Each model has a number of class variables, each of which tapresents a database field in the model.
In this particular case `ForeignKey` tells Django each chouce is related to a single *Question*. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.

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
- Each **DateTimeField** gets free JavaScript shortcut (dates get a "Today" shortcut and calendar popup, and times get a "Now" shortcut and a convenient popup that lists commonly entered times)