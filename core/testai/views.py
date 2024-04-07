from rest_framework import viewsets

from testai.models import Tests
from testai.serializers import TestsSerializer


class TestViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer
