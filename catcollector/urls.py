"""catcollector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# * this is how the web page first opens EXCEPT
from django.contrib import admin
# * include 
# is added here which allows us to tie another applications urls
# * path is used to define a URL pattern and its corresponding view function
from django.urls import path, include

# * url patterns is the name by convention but it could've been named anything. 
#  url patterns contains a list of the urls
urlpatterns = [
    # * the admin link below is used when a super user is created and
    # then that super user can login when the user attaches /admin to the localhoost:
    path('admin/', admin.site.urls),
    # * instead of '/', in django, the homepage is referenced using ''
    path('', include('main_app.urls')),
    # include the built-in auth urls for the built-in views
    path('accounts/', include('django.contrib.auth.urls')),
]
