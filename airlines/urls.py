from django.contrib import admin
from django.urls import path,include
from . import views
from armsApp import views
from flights import views
from airport import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('airlines/',views.list_airline,name='airline-page'),
    path('manage_airline',views.manage_airline,name='manage-airline'),
    path('manage_airline/<int:pk>',views.manage_airline,name='manage-airline-pk'),
    path('save_airline',views.save_airline,name='save-airline'),
    path('delete_airline/<int:pk>',views.delete_airline,name='delete-airline-pk'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
