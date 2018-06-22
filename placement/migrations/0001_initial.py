# Generated by Django 2.0.6 on 2018-06-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.PositiveSmallIntegerField()),
                ('area_of_operation', models.TextField()),
                ('comments', models.TextField()),
                ('contact_number', models.CharField(max_length=10)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='IndustryInteraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('person', models.TextField()),
                ('industry', models.ForeignKey(on_delete=None, to='placement.Industry')),
            ],
        ),
        migrations.CreateModel(
            name='PlacementFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('industry', models.ForeignKey(on_delete=None, to='placement.Industry')),
                ('student', models.ForeignKey(on_delete=None, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='StudentPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.BigIntegerField()),
                ('date_of_visit', models.DateField()),
                ('date_of_joining', models.DateField()),
                ('attachment', models.FileField(upload_to='')),
                ('location', models.TextField()),
                ('industry', models.ForeignKey(on_delete=None, to='placement.Industry')),
                ('student', models.ForeignKey(on_delete=None, to='user.User')),
            ],
        ),
    ]
