from statistics import median

from django.db import models


class Vote(models.Model):
    """ A vote"""
    title = models.CharField(max_length=1000)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Option(models.Model):
    """An option for a vote"""
    name = models.CharField(max_length=1000)
    vote = models.ForeignKey(Vote, related_name='options')
    option_id = models.IntegerField()

    def compute_evaluations_median(self):
        evaluations = self.evaluations.order_by('evaluation').values_list('evaluation', flat=True)
        if len(evaluations) == 0:
            return 0
        else:
            return median(evaluations)

    def __str__(self):
        return self.name


class Evaluation(models.Model):
    REJECT = 0
    NOT_ENOUGH = 1
    PASSABLE = 2
    MEDIUM = 3
    GOOD = 4
    VERY_GOOD = 5
    EXCELLENT = 6
    EVALUATION_CHOICES = (
        (REJECT, "A rejeter"),
        (NOT_ENOUGH, "Insuffisant"),
        (PASSABLE, "Passable"),
        (MEDIUM, "Assez Bien"),
        (GOOD, "Bien"),
        (VERY_GOOD, "Très bien"),
        (EXCELLENT, "Excellent")
    )
    option = models.ForeignKey(Option, related_name='evaluations')
    evaluation = models.PositiveSmallIntegerField(choices=EVALUATION_CHOICES)

    def __str__(self):
        return str(self.evaluation)
