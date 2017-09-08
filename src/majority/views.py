from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.decorators import detail_route

from .models import Vote, Option, Evaluation
from .serializers import VoteSerializer


class VoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def create(self, request):
        serializer = VoteSerializer(data=request.data)
        vote = None
        if serializer.is_valid():
            vote = serializer.save()
            return Response({'url': reverse('vote-detail', args=[vote.id])})

    @detail_route(methods=['post'])
    def submit(self, request, pk=None):
        data = request.data
        option = None
        evaluation_value = 0
        vote = Vote.objects.get(pk=pk)
        if vote and data and 'option_id' in data and 'evaluation' in data:
            option = Option.objects.get(option_id=data['option_id'], vote=vote)
            evaluation_value = data['evaluation']
            evaluation = Evaluation.objects.create(option=option, evaluation=evaluation_value)
        else:
            return Response({ "result": "error"})
        return Response({"result": "success"})

    @detail_route(methods=['get'])
    def results(self, request, pk=None):
        vote = Vote.objects.get(pk=pk)
        if vote:
            serializer = VoteSerializer(vote)
        else:
            return Response({ "result": "error"})
        return Response(serializer.data)
