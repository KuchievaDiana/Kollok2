from django.db import models


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    players = models.JSONField()
    state = models.TextField()

    class Meta:
        app_label = 'games'

    def __str__(self):
        return f'Game #{self.id} [state: {self.state}; scores: {self.players}]'


class Player(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        app_label = 'games'
