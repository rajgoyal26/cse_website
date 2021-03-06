# Generated by Django 2.0.6 on 2018-06-25 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('head_name', models.CharField(max_length=50)),
                ('foundation_year', models.CharField(max_length=4)),
                ('vision', models.TextField()),
                ('mission', models.TextField()),
                ('resources', models.TextField()),
                ('rules_reg', models.TextField()),
                ('calendar', models.IntegerField()),
            ],
        ),
    ]
