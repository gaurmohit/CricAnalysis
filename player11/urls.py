from django.conf.urls import url
from .views import home,player11

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^player11/', player11 , name="player11"),    
]