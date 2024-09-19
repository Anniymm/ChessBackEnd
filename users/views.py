from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, logout
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer, PersonalSpaceSerializer
from .models import PersonalSpace
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()
#  aqqac unda damibrunos tokenebi
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)


        response_data = {
            'user': UserSerializer(user).data,
            'access': access_token,
            'refresh': refresh_token,
        }

        return Response(response_data, status=status.HTTP_201_CREATED)



class LoginView(APIView):        
    permission_classes = [AllowAny] # yvelas sheedzlos login

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user is not None: 
                #useris avtomaturad shesvlistvis
                refresh = RefreshToken.for_user(user)
                # user_data = UserSerializer(user).data
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    # 'user': user_data
                }, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

    
class PersonalSpaceView(generics.RetrieveUpdateAPIView):
    queryset = PersonalSpace.objects.all()
    serializer_class = PersonalSpaceSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self): # unda gavitvaliswino roca arsebobs migheba da roca ar arsebobs sheqmna // kalatis kontroli
        user = self.request.user
        personal_space, created = PersonalSpace.objects.get_or_create(user=user)
        return personal_space