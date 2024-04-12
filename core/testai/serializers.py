from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from testai.models import Tests, TestCase, TestStep

class TestStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestStep
        fields = ['description'] #  'created', 'testcase', 

class TestCaseSerializer(WritableNestedModelSerializer):
    steps = TestStepSerializer(many=True)
    
    class Meta:
        model = TestCase
        fields = ['title', 'steps'] # 'id', 'created', 'test',

class TestsSerializer(WritableNestedModelSerializer):
    tests = TestCaseSerializer(many=True)
    
    class Meta:
        model = Tests
        fields = ['tests'] # 'id', , 'steps' 'created', 'name', 'description', 
