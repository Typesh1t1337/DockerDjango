from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('search/',SearchView.as_view(), name='search'),
    path('chat/<int:chat_id>/<str:nick>/', Message_view.as_view(), name='chat'),
    path('chat/create/<str:name>/',add_user_to_chat, name='add_user_to_chat'),
    path('profile/<str:name>/',ProfileView.as_view(), name='profile'),
    path('profile/edit/<str:name>',EditProfile.as_view(), name='edit_profile'),
    path('profile/user/<str:name>',UserProfileView.as_view(), name='user_profile'),
    path("/profile/send_emails/",MessageEmailSendVIew.as_view(),name='send_emails'),
]