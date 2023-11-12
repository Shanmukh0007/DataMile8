from django.db import models    
from django.utils import timezone

# This is the login table created in MySQL
class Login(models.Model):

    # MaxValueValidator limits the value to the given value
    Roll_number = models.BigIntegerField(primary_key=True)

    Name = models.CharField(null=True,max_length=100)

    Year_of_join = models.BigIntegerField(null=True)

    Stream = models.CharField(null=True,max_length=100)

    Password = models.CharField(null=True, max_length=100)

class ProjectTable(models.Model):

    ProjectName=models.CharField(null=True,max_length=100)

    ProjectDescription=models.CharField(null=True,max_length=10000)

    TeamLeader=models.BigIntegerField(null=True)

class TeamTable(models.Model):

    TeamMembers=models.BigIntegerField(null=True)

    ProjectName=models.CharField(null=True,max_length=100)




