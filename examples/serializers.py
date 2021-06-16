from rest_framework import serializers
from examples.models import Example

# Create your views here.
class ExampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Example
        fields = ('id',
                  'title',
                  'description',
                  'published')
