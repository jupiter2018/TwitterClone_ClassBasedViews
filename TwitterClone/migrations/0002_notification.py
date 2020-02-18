# Generated by Django 2.2.6 on 2019-10-31 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TwitterClone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetfor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TwitterClone.TwitterUser')),
                ('tweetfrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TwitterClone.Tweet')),
            ],
        ),
    ]
