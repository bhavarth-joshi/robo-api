import json

from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import action

from .utils import parse_test_data, execute_tests

from testai.models import Tests, TestCase, TestStep
from testai.serializers import TestsSerializer, TestCaseSerializer, TestStepSerializer


class TestViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer
    
    @action(detail=True)
    def execute(self, request, *args, **kwargs):
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                test_cases = parse_test_data(data)
                results = execute_tests(test_cases)
                return JsonResponse(results, safe=False)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)


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
