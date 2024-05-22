from django.urls import path
from . import views

#creates the URL patterns to map with views
urlpatterns = [
    path('', views.index, name='index'),
    path('result/<int:pk>/', views.result, name='result'),
    path('reference/<str:reference_number>/', views.reference, name='reference'),
    path('search/', views.search, name='search'),
    path('search_page/', views.search_page, name='search_page'),
]
