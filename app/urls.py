
from django.urls import path
from.import views

urlpatterns = [
    path('', views.render_nursery),
    path('about', views.render_aboutus),
    path('register', views.render_register),
    path('contact', views.render_contactus),
    path('team', views.render_nurseries)
]
