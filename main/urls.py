from django.urls import path
from main.views import ProfileList, ProfileDetails, ListList, TaskDetail, TaskCreate, TaskChange, ListDelete


urlpatterns = [
    path('user/', ProfileList.as_view()),
    path('my-profile/', ProfileDetails.as_view()),
    path('list/', ListList.as_view()),
    path('list-delete/<int:pk>/', ListDelete.as_view()),
    path('task/<int:pk>/', TaskDetail.as_view()),
    path('task-change/<int:pk>/', TaskChange.as_view()),
    path('task-create/', TaskCreate.as_view()),
]
