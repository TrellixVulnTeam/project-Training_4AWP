# Generated by Django 2.2.6 on 2019-10-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_doctor_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='about',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='patient',
            name='occupation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_no',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]