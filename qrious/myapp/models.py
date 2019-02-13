from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Userdata(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.player.username


class Level(models.Model):
    level_id = models.PositiveIntegerField()

    def __str__(self):
        return str(self.level_id)


class Question(models.Model):
    question_id = models.PositiveIntegerField()
    question_level = models.ForeignKey(Level, on_delete=models.CASCADE)
    question = models.CharField(max_length=450, unique=True)

    def __str__(self):
        return str(self.question_id)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice1 = models.CharField(max_length=450, null=True)
    choice2 = models.CharField(max_length=450, null=True)
    choice3 = models.CharField(max_length=450, null=True)
    choice4 = models.CharField(max_length=450, null=True)
    correctchoice = models.CharField(max_length=450, null=True)

    def __str__(self):
        return str(self.choice_id)
