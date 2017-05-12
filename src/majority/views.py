from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Vote
from .serializers import VoteSerializer


class VoteViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def create(self, request):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'vote created'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
