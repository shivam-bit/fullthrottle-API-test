from django.contrib import admin
from django.urls import path,include
from .views import userView,loginView,logoutView,detailView

urlpatterns = [
    path('user',userView.as_view()),
    path('login',loginView.as_view()),
    path('logout',logoutView.as_view()),
    path('detail',detailView.as_view()),
]
