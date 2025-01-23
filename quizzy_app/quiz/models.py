from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Results(models.Model): # Results model
    title = models.CharField(max_length=100)
    marks = models.IntegerField()
    date_done = models.DateTimeField(default=timezone.now)
    player = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): # Prints out the title
        return self.title