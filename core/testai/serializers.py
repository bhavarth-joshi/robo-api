from rest_framework import serializers
from testai.models import Tests

class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tests
        fields = ('title', 'steps') # 'id', 'created',
