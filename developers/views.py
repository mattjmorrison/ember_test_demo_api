from rest_framework import viewsets
from developers.serializers import DeveloperSerializer
from developers.models import Developer


class Developers(viewsets.ModelViewSet):
    serializer_class = DeveloperSerializer

    def get_queryset(self):
        return Developer.objects.all()
