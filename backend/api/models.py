from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.TextChoices):
    INHABITANT = "inhabitant"
    GUARD = "guard"
    MANAGER = "manager"
    ADMIN = "admin"

class User(AbstractUser):
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.INHABITANT,
    )

    # You can add related_name to avoid the clash with the auth User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='api_user_set',  # Custom related_name to avoid clash
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='api_user_permissions_set',  # Custom related_name to avoid clash
        blank=True
    )
    
    def has_access_to_apartment(self, apartment):
        if self.role == Role.ADMIN:
            return True
        elif self.role == Role.MANAGER:
            return apartment.entrance.building in self.buildings.all()
        elif self.role == Role.GUARD:
            return apartment.entrance in self.entrances.all()
        elif self.role == Role.INHABITANT:
            return apartment in self.apartments.all()
        return False

    def has_access_to_entrance(self, entrance):
        if self.role == Role.ADMIN:
            return True
        elif self.role == Role.MANAGER:
            return entrance.building in self.buildings.all()
        elif self.role == Role.GUARD:
            return entrance in self.entrances.all()
        return False

    def has_access_to_building(self, building):
        if self.role == Role.ADMIN:
            return True
        elif self.role == Role.MANAGER:
            return building in self.buildings.all()
        return False


class Building(models.Model):
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=10)


class Entrance(models.Model):
    building = models.ForeignKey(Building, related_name="entrances", on_delete=models.CASCADE)
    number = models.CharField(max_length=10)


class Apartment(models.Model):
    entrance = models.ForeignKey(Entrance, related_name="apartments", on_delete=models.CASCADE)
    number = models.CharField(max_length=10)

# User roles with specific access
User.add_to_class('apartments', models.ManyToManyField(Apartment, related_name='inhabitants', blank=True))
User.add_to_class('entrances', models.ManyToManyField(Entrance, related_name='guards', blank=True))
User.add_to_class('buildings', models.ManyToManyField(Building, related_name='managers', blank=True))
