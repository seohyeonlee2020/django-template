# Django starter template

## How to build a django project from scratch:

Enter the following commands into the command shell:
<br>`mkdir [pick any directory name]`
<br>`django-admin startproject [projectname] [directory name]`
<br>`python manage.py startapp [app name]`

These commands will bootstrap a django project with a file struture like this:
<ul>
   <li>directory-name/</li>
   <li>manage.py</li>
   <li>project-name/</li>
      <ul>
      <li>__init__.py</li>
      <li>settings.py</li>
      <li>urls.py</li>
      <li>asgi.py</li>
      <li>wsgi.py</li>
      </ul>
    <li>app-name/</li>
    <ul>
      <li>__init__.py</li>
      <li>admin.py</li>
      <li>apps.py</li>
      <li>migrations/</li>
       <ul>
        <li>__init__.py</li>
      </ul>
    <li>models.py</li>
    <li>tests.py</li>
    <li>views.py</li>
</ul>
<br>
Create urls.py inside the app folder and fill it with a basic pattern:
<br> `touch urls.py`
<br> urls.py:

```
from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
]
```

set up the urls.py in the project directory like this:

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("[insert app name]/", include("[insert app name].urls")),
    path("admin/", admin.site.urls),
]
```

set up views.py in the app directory like this:

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("this has to show up when you go to http://localhost:8000/[insert app name]/ in the next step")
```

run `python manage.py runserver`
<br>and go to http://localhost:8000/[insert app name]/ to make sure you see what you put in your view

