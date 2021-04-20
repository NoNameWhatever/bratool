from rest_framework.views import APIView
from rest_framework.response import Response


class ToolApiView(APIView):
    """Tool API View"""

    def get(self, request, format=None):
        """Return a list of tools"""

        an_apiview = [
            'Uses HTTP methods as function (ger, post, patch, put, delete)',
            'Is similar to a traditional Django View.',
            'Gives you the most control over your application logic.',
            'Is mapped manually to URLs.',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})