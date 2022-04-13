from django.urls import path, include
from .views import HomeDetailView,HomePageView,TheListView, NewView, HomeUpdateView, DeleteUpdateView

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('thelist/',TheListView.as_view(),name='thelist'),
    path('detail/<int:pk>',HomeDetailView.as_view(),name='detail'),
    path('new',NewView.as_view(),name='new'),
    path('update/<int:pk>',HomeUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',DeleteUpdateView.as_view(),name='delete'),
   

]