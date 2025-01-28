# Django starter template

## How to build a django project from scratch:

Enter the following commands into the command shell:
<br>`mkdir [pick any directory name]`
<br>`django-admin startproject [projectname] [directory name]`
<br>`python manage.py startapp [app name]`

These commands will bootstrap a django project with a file struture like this:
<br>directory-name/
    *manage.py
    *project-name/
        *__init__.py
        *settings.py
        *urls.py
        *asgi.py
        *wsgi.py
    *app-name/
    *__init__.py
    *admin.py
    *apps.py
    *migrations/
        *__init__.py
    *models.py
    *tests.py
    *views.py
    
Create urls.py inside the app folder and fill it with a basic pattern:
<br>`touch urls.py`
<br>urls.py:

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
from django.urls import path

from . import views

urlpatterns = [
    path("", views.[view name], name="[view name]"),
]
```

run `python manage.py runserver`
<br>and go to http://localhost:8000/[insert app name]/ to make sure you see what you put in your view

