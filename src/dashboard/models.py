from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):

    '''
    Data related to a user. This information will be displayed on the dashboard.
    '''

    class Meta:
        verbose_name = 'User Data'    

    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    name: str = models.CharField(max_length=30)
    eye_breaks: int = models.IntegerField()
    total_break_time: int = models.IntegerField()

    def __str__(self):
        return f"{self.name} | Eye breaks: {self.eye_breaks} | Break time: {self.total_break_time}"
    