from django.contrib import admin
from django.urls import path

from alphaR.planet.views.planet_views import list_planets, edit_planet, create_planet, delete_planet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('planets/', list_planets, name='list_planets'),
    path('create/planet/', create_planet, name='create_planet'),
    path('edit/planet/<uuid:pk>/', edit_planet, name='edit_planet'),
    path('delete/planet/<uuid:pk>/', delete_planet, name='delete_planet'),
]
