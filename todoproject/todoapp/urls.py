from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('list/',views.listviewtask.as_view(),name='list'),
    path('detail/<int:pk>/',views.detailviewtask.as_view(),name='detail'),
    path('cbvupdate/<int:pk>/',views.updateviewtask.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.deleteviewtask.as_view(),name='cbvdelete'),
]