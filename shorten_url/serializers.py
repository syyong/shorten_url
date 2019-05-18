from rest_framework import serializers
from .models import Redirect


# pylint: disable=too-few-public-methods
class RedirectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Redirect
        fields = ('url', 'destination', 'code', 'visits',)
