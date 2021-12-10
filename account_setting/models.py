from django.db import models
from users.models import UserProfile

REASON = (
    ('Account', (
     ('Unsubscribe from Miver emails', 'Unsubscribe from Miver emails'),
     ('I want to change my username', 'I want to change my username'),
        ('I have another Miver account', 'I have another Miver account'),
        ('Other', 'Other')
     )
     ),
    ('Buying', (
     ('I can not find what I need on Miver',
      'I can not find what I need on Miver'),
     ('Miver is complicated or hard to use',
      'Miver is complicated or hard to use'),
     ('Negative experience with seller/s', 'Negative experience with seller/s'),
     ('I am unhappy with Mivers policies', 'I am unhappy with Miver policies'),
     ('other', 'other')
     )
     ),
)


class AccountDeactivation(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)
    reason = models.CharField(
        choices=REASON, default='male', max_length=50)
    detail = models.TextField()
