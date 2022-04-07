from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """name field for testing our api view"""

    name = serializers.CharField(max_length = 15)