# Generated by Django 2.0.6 on 2018-06-25 10:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('faculty', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_type', models.CharField(choices=[('Int', 'Internal'), ('M', 'Main')], max_length=10)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('duration', models.DurationField()),
                ('course_id', models.ForeignKey(on_delete=None, to='course.Course')),
                ('faculty_id', models.ForeignKey(on_delete=None, to='faculty.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('RE', 'Remember'), ('UN', 'Understood'), ('AP', 'Apply'), ('AN', 'Analyze'), ('EV', 'Evaluate'), ('CD', 'Create/Design')], max_length=10)),
                ('text', models.TextField()),
                ('max_marks', models.PositiveSmallIntegerField()),
                ('question_order', models.PositiveSmallIntegerField()),
                ('marking_scheme', models.TextField()),
                ('assessment_id', models.ForeignKey(on_delete=None, to='assessment.Assessment')),
                ('outcome_id', models.ForeignKey(on_delete=None, to='course.CourseOutcome')),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obtained_marks', models.PositiveSmallIntegerField()),
                ('remarks', models.TextField()),
                ('question', models.ForeignKey(on_delete=None, to='assessment.AssessmentQuestion')),
                ('student', models.ForeignKey(on_delete=None, to='user.User')),
            ],
        ),
    ]
