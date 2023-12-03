from django.urls import path
from . import views
urlpatterns=[
    path('index/', views.index),
    path('home/', views.index),
    path('about/', views.about),
    path('product/', views.product),
    path('myorder/', views.myorder),
    path('enquiry/', views.enquiry),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('mens/', views.mens),
    path('kids/', views.kids),
    path('womens/', views.womens),
    path('profile/', views.myprofile),
    path('viewproduct/', views.viewproduct),
    path('' ,views.index),
    path('signout/' ,views.signout),
    path('myordr/' ,views.myordr),
    path('mcart/' ,views.mycart),
    path('showcart/' ,views.showcart),
    path('cpdetail/' ,views.cpdetail),


]