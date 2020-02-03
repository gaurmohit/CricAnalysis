from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^world_cup/', views.world_cup , name="world_cup"),
    url(r'final_cup/', views.final_cup , name="final_cup")
]