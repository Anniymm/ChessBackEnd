from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from app.models import Project
from app.serializers import ProjectSerializer

# aq yvelaferi rigzea, kargad filtravs
class UserProjectsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # daabrunos bazidam yvela proeqti rac konkretul usrs exeba id-t
        return Project.objects.filter(Q(customers=user) | Q(contractors=user))
