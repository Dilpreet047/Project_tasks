
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.function1, name='start'),
    path('result/', views.function2, name='result')
]
