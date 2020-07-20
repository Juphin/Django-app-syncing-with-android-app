from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Publication


class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = ['id', 'title', 'content']
        #extra_kwargs = {'id': {'read_only': True}}


