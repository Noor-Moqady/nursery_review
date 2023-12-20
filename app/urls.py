
from django.urls import path
from.import views

urlpatterns = [
    
    path('about', views.render_aboutus),
    path('contact', views.render_contactus),
    path('register',views.registration_form),
    path('',views.welcome),
    path('login',views.login),
    path('logout',views.logout),
    path('addnursery',views.addnursery),
    path('nursery/<int:id>', views.specific_nursery)
    

]
