# Generated by Django 3.2.8 on 2021-10-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cre', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
