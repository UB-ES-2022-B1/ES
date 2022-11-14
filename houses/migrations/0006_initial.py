# Generated by Django 4.1.2 on 2022-11-01 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0005_delete_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocked', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('id_house', models.IntegerField(null=True)),
                ('base_price', models.FloatField(max_length=7)),
                ('extra_costs', models.FloatField(max_length=7)),
                ('taxes', models.FloatField(max_length=7)),
                ('num_hab', models.IntegerField()),
                ('num_beds', models.IntegerField()),
                ('num_bathrooms', models.IntegerField()),
                ('num_people', models.IntegerField()),
                ('company_individual', models.CharField(max_length=100)),
                ('kitchen', models.BooleanField()),
                ('swiming_pool', models.BooleanField()),
                ('garden', models.BooleanField()),
                ('billar_table', models.BooleanField()),
                ('gym', models.BooleanField()),
                ('TV', models.BooleanField()),
                ('WIFII', models.BooleanField()),
                ('dishwasher', models.BooleanField()),
                ('washing_machine', models.BooleanField()),
                ('air_conditioning', models.BooleanField()),
                ('free_parking', models.BooleanField()),
                ('spacious', models.BooleanField()),
                ('central', models.BooleanField()),
                ('quite', models.BooleanField()),
                ('alarm', models.BooleanField()),
                ('smoke_detector', models.BooleanField()),
                ('health_kit', models.BooleanField()),
            ],
        ),
    ]
