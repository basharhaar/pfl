from django.db import models

# Create your models here.

class Registration(models.Model):
    team_name = models.CharField(max_length=250)
    player_names = models.TextField(blank=True)
    city = models.CharField(max_length=250)
    team_manager = models.CharField(max_length=250)
    team_manager_phonenumber = models.CharField(max_length=250)
    team_manager_cnic = models.CharField(max_length=250)
    team_captain = models.CharField(max_length=250)
    team_captain_phonenumber = models.CharField(max_length=250)
    extra_remarks = models.TextField(blank=True)
    def __str__(self):
        return self.team_name