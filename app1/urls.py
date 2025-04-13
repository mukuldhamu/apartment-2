from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('owner_signup/', views.owner_signup, name='owner_signup'),
    path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
    path('login/', views.login, name='login'),
    path('login1/', views.login1, name='login1'),
    path('login2/', views.login2, name='login2'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
    path('tips/', views.tips, name='tips'),
    path('privacy/', views.privacy, name='privacy'),
    path('property_details/', views.property_details, name='property_details'),
    path('about/', views.about, name='about'),
    path('owner_profile/', views.owner_profile, name='owner_profile'),
    path('search_output/', views.search_output, name='search_output'),
    path('booking/', views.booking, name='booking'),
    path('change_password/', views.change_password, name='change_password'),
    path('update/', views.update, name='update'),
    path('logout/', views.logout, name='logout'),
    # path('successView/', views.successView, name='successView'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('send_request/', views.send_request, name='send_request'),
    path('approve/', views.approve, name='approve'),



]
