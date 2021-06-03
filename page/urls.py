
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path('ticket/<int:ticket_id>', views.confirm, name="confirm"),
    path('ticket', views.ticket, name='ticket'),
    path("blog", views.blog, name="blog"),
    
]  