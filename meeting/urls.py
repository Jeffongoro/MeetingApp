from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_meeting, name='create-meeting'),
    path('retrieve/', views.retrieve_meeting, name='retrieve-meeting'),
    path('update/<int:pk>', views.update_meeting, name='update-meeting'),
    path('delete/<int:pk>', views.delete_meeting, name='delete-meeting'),
    path('past/', views.past_meetings, name='past-meetings'),
]
