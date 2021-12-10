from django.db import models
from users.models import UserProfile


STATUS = ( ('', 'Please select status'), ('progress','progress'),('cancelled','cancelled')
)


class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order_summary=models.CharField(max_length=20,null=False,blank=False)
    order_date=models.DateTimeField(auto_now=True)
    due_date=models.DateTimeField(null=False)
    price = models.IntegerField(null=False, blank=False)
    status=models.CharField(max_length=10 , choices=STATUS,default='')
    active=models.BooleanField(default=False)
    delivered=models.BooleanField(default=False)
    cancelled=models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user.user_name}'
    









