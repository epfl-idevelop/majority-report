from rest_framework import serializers

from .models import Vote, Option, Evaluation


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ['evaluation']


class OptionSerializer(serializers.ModelSerializer):
    evaluations_median = serializers.ReadOnlyField(source='compute_evaluations_median')

    class Meta:
        model = Option
        fields = ('name', 'evaluations_median')


class VoteSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=1000)
    closed = serializers.BooleanField(default=False)
    options = OptionSerializer(many=True)

    class Meta:
        model = Vote
        fields = ('title', 'options', 'closed')

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        vote = Vote.objects.create(**validated_data)
        option_id = 0
        for option_data in options_data:
            Option.objects.create(vote=vote, option_id=option_id, **option_data)
            option_id += 1
        return vote

    def update(self, instance, validated_data):
        instance.closed = validated_data.get('closed', instance.closed)
        instance.save()
        return instance
