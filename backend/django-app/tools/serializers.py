from rest_framework import serializers

from tools import models

class TestSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)

class ToolsSerializer(serializers.ModelSerializer):
    """Serializes tools object"""    

    class Meta:
        model = models.Tool
        fields = ('id', 'name', 'identification', 'description', 'department', 'keeper')

    def create(self, validated_data):
        """Create and return new tool"""
        tool = models.Tool.objects.create(
            name=validated_data['name'],
            identification=validated_data['identification'],
            description=validated_data['description'],
            keeper=validated_data['keeper'],            
        )

        tool.department.set(validated_data['department'])

        return tool

