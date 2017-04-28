from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # required field
    user = models.OneToOneField(User, related_name="profile")

    sciper = models.PositiveIntegerField(null=True, blank=True)
    where = models.CharField(max_length=100, null=True, blank=True)
    units = models.CharField(max_length=300, null=True, blank=True)
    group = models.CharField(max_length=150, null=True, blank=True)
    classe = models.CharField(max_length=100, null=True, blank=True)
    statut = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return ""


# Trigger for creating a profile on user creation
def user_post_save(sender, instance, **kwargs):
    profile, new = UserProfile.objects.get_or_create(user=instance)

# Register the trigger
models.signals.post_save.connect(user_post_save, sender=User)
