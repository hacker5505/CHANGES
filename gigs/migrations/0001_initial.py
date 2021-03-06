# Generated by Django 3.2.5 on 2021-10-24 05:02

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '__first__'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField(max_length=1200)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('image2', models.ImageField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('image3', models.ImageField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('video', models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['mp4', 'avi'])])),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=100)),
                ('revision', models.CharField(choices=[('', 'Select number of revisions for this gig'), ('1', '1'), ('2', '2'), ('3', '3 '), ('unlimited', 'unlimited')], default='', max_length=20)),
                ('delivery_time', models.CharField(choices=[('', 'Select delivery time for this gig'), ('1', '1 day'), ('2', '2 days'), ('3', '3 days'), ('unlimited', 'unlimited')], default='', max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OverView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('search_tags', models.CharField(max_length=102)),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='CompleteGig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=False, null=True)),
                ('description', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gigs.description')),
                ('media', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gigs.media')),
                ('over_view', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gigs.overview')),
                ('pricing', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gigs.pricing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
        ),
    ]
