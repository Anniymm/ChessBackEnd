from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tokens/', TokenRefreshView.as_view(), name='token_obtain_pair'), # token ganaxlebistvis 
    path('personal/', PersonalSpaceView.as_view(), name='personal-space'),
]