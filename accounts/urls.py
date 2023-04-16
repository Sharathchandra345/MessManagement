from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/',views.signup, name='signup'),
    path('',views.user_login, name='signin'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('contacts/',views.contact,name='contact'),
    path('full_mess/',views.full_mess,name='full_mess'),
    path('feedback/',views.feedback,name='feedback'),
      path('nighttuck/',views.night_tuck,name='nighttuck'),
    path('profileform/',views.profileform,name='profileform'),
     # path('signout/',views.signup, name='signout'),
]
