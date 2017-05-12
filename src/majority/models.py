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
