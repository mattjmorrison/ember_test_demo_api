from rest_framework_json_api import serializers
from developers.models import Developer


class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = '__all__'
