from django.urls import path
from .views import *
#defaultebze gadavawyo, default routerebze
urlpatterns = [
    path('send-invitation', send_invitation, name='send-invitation'),
    path('accept-invitation/', accept_invitation, name='accept-invitation'),
    path('register-invitee', register_user, name='register-user'),
]
