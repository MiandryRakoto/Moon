from django.urls import path
from . import  views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.users, name="users"),
    path('<int:pk>/', views.discussion, name="discussion"),
]
