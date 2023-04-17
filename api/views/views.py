from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
"""
Because I restructured the folder of app in many sub-folder, I have to use absolute path of modules to import one
"""
from api.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow users to be viewed or edited
    """
    queryset = User.objects.all().order_by(('-date_joined'))
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow users to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permissions_classes = [permissions.IsAuthenticated]