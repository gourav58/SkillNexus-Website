from django.urls import path
from . import views

urlpatterns = [

    # Home page urls
    path('', views.Home, name='home'),
    path('about-us/', views.Aboutus, name='about-us'),
    path('services/', views.Services, name='services'),
    path('Courses/', views.Courses, name='Courses'),
    path('Blog/', views.Blog, name='Blog'),
    path('Contact-us/', views.Contactus, name='Contact-us'),
    path('Book-demo/', views.BookDemo, name='Book-demo'),

]
