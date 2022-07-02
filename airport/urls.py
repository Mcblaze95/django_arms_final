from django.contrib import admin
from django.urls import path,include
from . import views
from airlines import views
from flights import views
from armsApp import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('airport/',views.list_airport,name='airport-page'),
    path('manage_airport',views.manage_airport,name='manage-airport'),
    path('manage_airport/<int:pk>',views.manage_airport,name='manage-airport-pk'),
    path('save_airport',views.save_airport,name='save-airport'),
    path('delete_airport/<int:pk>',views.delete_airport,name='delete-airport-pk'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
