from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.mail import EmailMessage,get_connection
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from .models import Invitation
from django.conf import settings
from users.serializers import UserSerializer
from users.models import PersonalSpace

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_invitation(request):
    inviter = request.user
    invitee_email = request.data.get('invitee_email')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    #  token
    token = default_token_generator.make_token(inviter)

    invitation = Invitation.objects.create(
        inviter=inviter, 
        invitee_email=invitee_email, 
        token=token,
        first_name=first_name,
        last_name=last_name
    )

    # Email 
    current_site = get_current_site(request)
    mail_subject = 'Invitation to join the project'
    message = (
        f"{inviter.username} has invited you to join their personal space on {current_site.domain}.\n\n"
        f"Use this link to accept the invitation:\n"
        f"http://{current_site.domain}/invite/accept-invitation/?token={token}\n\n"
    )

    # Email 
    email = EmailMessage(
        mail_subject,
        message,
        from_email=settings.EMAIL_HOST_USER,  
        to=[invitee_email],
    )

    # Send email
    email.send(fail_silently=False)

    return Response({'detail': 'Invitation sent successfully', 'token': token}, status=status.HTTP_200_OK)


@api_view(['GET'])
def accept_invitation(request):
    token = request.GET.get('token')
    # email = request.GET.get('email')

    if not token :
        return Response({'error': 'Token and email are required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        invitation = Invitation.objects.get(token=token, accepted=False)
    except Invitation.DoesNotExist:
        return Response({'error': 'Invalid token or invitation already accepted'}, status=status.HTTP_400_BAD_REQUEST)

    # dadastureba
    invitation.accepted = True
    #shevinaxot bazashi
    invitation.save() 
    return Response({'detail': 'Invitation accepted successfully', 'token': token}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')

    if not email or not password or not confirm_password:
        return Response({'error': 'Email, password, and confirm password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        invitations = Invitation.objects.filter(invitee_email=email, accepted=True)

        if invitations.exists():
            invitation = invitations.latest('created_at')
            inviter = invitation.inviter
            # invitee = invitation.invitee_email
        else:
            return Response({'error': 'No valid invitation found for this email'}, status=status.HTTP_400_BAD_REQUEST)

    except Invitation.DoesNotExist:
        return Response({'error': 'No valid invitation found for this email'}, status=status.HTTP_400_BAD_REQUEST)
    except Invitation.MultipleObjectsReturned:
        return Response({'error': 'Multiple invitations found for this email'}, status=status.HTTP_400_BAD_REQUEST)

    # tu gmail ukve arsebobs
    try:
        user = get_user_model().objects.get(email=email)
        return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    except get_user_model().DoesNotExist:
        pass

    # serializeristvis
    user_data = {
        'email': email,
        'password': password,
        'confirm_password': confirm_password,
        'first_name': inviter.first_name,
        'last_name': inviter.last_name,
        'username': email  # gmail rogorc username, amis shecvla shemidzlia rorame
    }

    serializer = UserSerializer(data=user_data)
    if serializer.is_valid():
        user = serializer.save()

        # personal spacestvis
        personal_space, created = PersonalSpace.objects.get_or_create(user=user)

        # mowvevis washla dadasturebis mere magram jobia jer ar wavshalo 
        # invitation.delete()

        # authetifikacia
        refresh = RefreshToken.for_user(user)
        token_data = {
            'refresh': str(refresh), #stringi ar gamomrches 
            'access': str(refresh.access_token),
        }

        return Response({'user': serializer.data, 'token': token_data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
