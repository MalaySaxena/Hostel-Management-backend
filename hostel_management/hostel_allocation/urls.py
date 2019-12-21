from django.urls import path
from django.conf.urls import include, url
from .views import checkAvaibility

urlpatterns = [
    path('/<int:id>/<str:type>/<str:lux>', checkAvaibility,name='status')
]