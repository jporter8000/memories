from django.conf.urls import url 
from memories_app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('doggos/', views.doggos, name = 'doggos'),
    path('doggostest/', views.doggostest, name = 'doggostest')
]