
from django.urls import path
from.import views

urlpatterns = [
    # path('', views.render_nursery),
    # path('about', views.render_aboutus),
    # path('register', views.render_register),
    # path('contact', views.render_contactus),
    # path('nurseries', views.render_nurseries)
    path('register',views.registration_form),
    path('',views.welcome),
    path('login',views.login),
    path('logout',views.logout)
]
