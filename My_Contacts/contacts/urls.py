from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('',index.as_view(),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',signup,name='signup'),
    path('add',add,name='add'),
    path('delete/<int:id>',delete,name='delete'),
    path('edit/<int:pk>',edit.as_view(),name='edit'),
]
