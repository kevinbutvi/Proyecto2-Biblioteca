# Generated by Django 3.2 on 2022-02-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]