from rest_framework import serializers
from testai.models import Tests, TestCase, TestStep

class TestStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestStep
        fields = ['description'] # 'id', 'created', 'testcase', 

class TestCaseSerializer(serializers.ModelSerializer):
    steps = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='description'
    )
    
    class Meta:
        model = TestCase
        fields = ['title', 'steps'] # 'id', 'created', 'test',

class TestsSerializer(serializers.ModelSerializer):
    tests = TestCaseSerializer(
        many=True,
        read_only=True
    )
    
    class Meta:
        model = Tests
        fields = ['tests'] # 'id', , 'steps' 'created', 'name', 'description', 
