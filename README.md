My Django starter template. 

How to build a django project from scratch:

Enter the following commands into the command shell:
`mkdir [pick any directory name]`
`django-admin startproject [projectname] [directory name]`
`python manage.py startapp [app name]`

These commands will bootstrap a django project with a file struture like this:
directory-name/
    manage.py
    project-name/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    app-name/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
    
Create urls.py inside the app folder and fill it with a basic pattern:
`touch urls.py`
urls.py:
`from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
]`

set up the urls.py in the project directory like this:
`from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("[insert app name]/", include("[insert app name].urls")),
    path("admin/", admin.site.urls),
]`

run `python manage.py runserver`
and go to http://localhost:8000/[insert app name]/

