from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    # Define fields for the UserProfile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        """
        Return a string representation of the UserProfile instance,
        using the username of the associated User.
        """
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler function that creates or updates the user profile
    whenever a User instance is saved.

    Parameters:
    - sender: The model class that sent the signal (User in this case).
    - instance: The actual instance of the model that was saved.
    - created: A boolean indicating whether a new instance was created.
    - **kwargs: Additional keyword arguments.
    """
    if created:
        # If a new User instance was created, create a corresponding 
        # UserProfile instance
        UserProfile.objects.create(user=instance)
    else:
        # If an existing User instance was saved, 
        # update the corresponding UserProfile instance
        instance.userprofile.save()
