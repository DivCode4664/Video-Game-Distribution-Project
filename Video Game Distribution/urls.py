"""gamingdistribution URL Configuration
 
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.style),
    path('homepage',views.homepage,name="homepage"),
    path('',views.homepage,name="homepage"),
    path('showPublisher',views.showPublisher, name = "showPublisher"),
    path('showGame',views.showGame,name="showGame"),
    path('InsertGame',views.InsertGame,name="InsertGame"),
    path('InsertPublisher',views.InsertPublisher,name="InsertPublisher"),
    path('updateGame/<int:id>',views.updateGame,name="updateGame"),
    path('EditGame/<int:id>',views.EditGame,name="EditGame"),
    path('EditPublisher/<int:id>',views.EditPublisher,name="EditPublisher"),
    path('DelGame/<int:id>',views.DelGame,name="DelGame"),
    path('deletedGame/<int:id>',views.deletedGame,name="deletedGame"),
    path('DelPublisher/<int:id>',views.DelPublisher,name="DelPublisher"),
    path('deletedPublisher/<int:id>',views.deletedPublisher,name="deletedPublisher"),
    path('updatePublisher/<int:id>',views.updatePublisher,name="updatePublisher"),
    path('SortGame',views.SortGame,name="SortGame"),
    path('SortPublisher',views.SortPublisher,name="SortPublisher"),
    path('QueryforGame',views.QueryforGame,name="QueryforGame"),
    path('QueryforPublisher',views.QueryforPublisher,name="QueryforPublisher"),
]
