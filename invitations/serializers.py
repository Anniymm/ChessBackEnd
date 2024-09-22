from .models import Invitation
from rest_framework import serializers



class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ['invitee_email','token', 'inviter','first_name', "last_name", "accepted"] 
