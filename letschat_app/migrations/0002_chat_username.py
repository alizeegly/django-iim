# Generated by Django 4.0.4 on 2022-04-28 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letschat_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='username',
            field=models.CharField(default='Anonymous', max_length=200),
        ),
    ]
