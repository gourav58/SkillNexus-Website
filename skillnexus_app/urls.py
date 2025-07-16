from django.urls import path
from . import views

urlpatterns = [

    # Home page urls
    path('', views.Home, name='home'),
    path('about-us/', views.Aboutus, name='about-us'),
    path('services/', views.Services, name='services'),
    path('courses/', views.Courses, name='courses'),
    path('blog/', views.Blog, name='blog'),
    path('contact-us/', views.Contactus, name='contact-us'),
    path('apply-internship/', views.ApplyInternship, name='apply-internship'),

]
