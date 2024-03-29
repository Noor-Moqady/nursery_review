
from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('about', views.render_aboutus),
    path('contact', views.render_contactus),
    path('register',views.registration_form),
    path('',views.welcome),
    path('login',views.login),
    path('logout',views.logout),
    path('addnursery',views.addnursery),
    path('updatenursery/<int:id>',views.update_nursery),
    path('nursery/<int:id>', views.specific_nursery),
    path('deletenursery/<int:id>', views.delete_nursery),
    path('review/<int:id>', views.addreview),
    path('delete/<int:id2>', views.delete_review),
    path('update/<int:id>', views.update_review),
    path('reviews',views.reviews),
    path('search',views.search)
] 




