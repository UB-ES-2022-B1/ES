# Generated by Django 4.1.2 on 2022-10-26 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=30, verbose_name='Country')),
                ('birthdate', models.DateField(verbose_name='Birth Date')),
                ('failedLoginAttemps', models.IntegerField(default=0, verbose_name='Number of Failed logins')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]