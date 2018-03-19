# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from lenovo.models import Poll, Choice
from rest_framework import viewsets
from lenovo.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows POlls to be viewed or edited.
    """
    queryset = Poll.objects.all().order_by('pub_date')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Choices to be viewed or edited.
    """
    queryset = Choice.objects.all()
    serializer_class = GroupSerializer



