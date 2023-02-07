from django.db import models

class Event(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=225)
    
    def __str__(self):
        return f"date = {self.date}, title = {self.title}"
        
