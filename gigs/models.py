from django.db import models
from partners.models import SubCategory
from users.models import UserProfile
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator

REVISIONS = (
    ('', 'Select number of revisions for this gig'), ('1',
                                                      '1'), ('2', '2'), ('3', '3 '), ('unlimited', 'unlimited')
)

DELIVERY = (
    ('', 'Select delivery time for this gig'), ('1',
                                                '1 day'), ('2', '2 days'), ('3', '3 days'), ('unlimited', 'unlimited')
)


class OverView(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=False, blank=False)
    search_tags = models.CharField(
        max_length=102, null=False, blank=False)

    def __str__(self):
        return f'{self.title}'


class Pricing(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    description = models.TextField(max_length=100, null=False, blank=False)
    revision = models.CharField(
        max_length=20, null=False, blank=False, choices=REVISIONS, default='')
    delivery_time = models.CharField(
        max_length=20, null=False, blank=False, choices=DELIVERY, default='')
    price = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class Description(models.Model):
    description = RichTextField(max_length=1200, null=False, blank=False)

    def __str__(self):
        return f'{self.id}'


class Media(models.Model):
    main_image = models.ImageField(null=False, blank=False, validators=[
                                   FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    image2 = models.ImageField(null=True, blank=True, validators=[
        FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    image3 = models.ImageField(null=True, blank=True, validators=[
        FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    video = models.FileField(null=True, blank=True, validators=[
        FileExtensionValidator(['mp4', 'avi'])])

    def __str__(self):
        return f'{self.id}'


class CompleteGig(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    over_view = models.OneToOneField(OverView, on_delete=models.CASCADE)
    pricing = models.OneToOneField(
        Pricing, on_delete=models.CASCADE, null=True, blank=True)
    description = models.OneToOneField(
        Description, on_delete=models.CASCADE, null=True, blank=True)
    media = models.OneToOneField(
        Media, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(null=True, blank=True, default=False)

    def delete(self, *args, **kwargs):
        self.over_view.delete()
        if self.pricing:
            self.pricing.delete()
        if self.description:
            self.description.delete()
        if self.media:
            self.media.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

    def __str__(self):
        return f'{self.user.user_name}'
