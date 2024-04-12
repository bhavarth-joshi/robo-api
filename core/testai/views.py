from rest_framework import viewsets

from testai.models import Tests, TestCase, TestStep
from testai.serializers import TestsSerializer, TestCaseSerializer, TestStepSerializer


class TestViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer

class TestCaseViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer

class TestStepViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = TestStep.objects.all()
    serializer_class = TestStepSerializer
