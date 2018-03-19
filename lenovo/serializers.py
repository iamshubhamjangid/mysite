from lenovo.models import Poll, Choice
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poll
        fields = ('question', 'pub_date')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('poll', 'choice', 'votes')

