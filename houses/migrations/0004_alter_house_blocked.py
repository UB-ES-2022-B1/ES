# Generated by Django 4.1.2 on 2022-11-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_alter_house_blocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
    ]
