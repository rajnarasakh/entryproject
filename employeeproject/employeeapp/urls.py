from django.urls import path
from .import views
urlpatterns=[
    path('',views.home_view),
    path('emp',views.empdetails)
]