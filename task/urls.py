from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtask/', views.addtask, name='addtask'),
    path('viewtask/<str:tasktitle>', views.viewtask, name='viewtask'),
    path('delete/<str:tasktitle>', views.delete , name='delete'),
]