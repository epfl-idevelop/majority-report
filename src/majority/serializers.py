from rest_framework import serializers

from .models import Vote, Option, Evaluation


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ['evaluation']

class OptionSerializer(serializers.ModelSerializer):
    evaluations = EvaluationSerializer(many=True, required=False)

    class Meta:
        model = Option
        fields = ('name', 'evaluations')

class VoteSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Vote
        fields = ('title', 'options', 'closed')

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        vote = Vote.objects.create(**validated_data)
        for option_data in options_data:
            Option.objects.create(vote=vote, **option_data)
        return vote

    def update(self, instance, validated_data):
        instance.closed = validated_data.get('closed', instance.closed)
        instance.save()
        return instance
