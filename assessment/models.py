from django.db import models
from enumerations.enum import QuestionType, AssessmentType
from user.models import User
from course.models import Course, CourseOutcome
from faculty.models import Faculty
from django.utils import timezone
from django.urls import reverse


class Assessment(models.Model):
    course_id = models.ForeignKey(Course, on_delete=None)
    assessment_type = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in AssessmentType])
    start_date = models.DateField(default=timezone.now)
    duration = models.DurationField()
    faculty_id = models.ForeignKey(Faculty, on_delete=None)

    def get_absolute_url(self):
        return reverse("assessment:create", kwargs={"id": self.id})


class AssessmentQuestion(models.Model):
    question_type = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in QuestionType])
    assessment_id = models.ForeignKey(Assessment, on_delete=None)
    text = models.TextField()
    max_marks = models.PositiveSmallIntegerField()
    question_order = models.PositiveSmallIntegerField()
    marking_scheme = models.TextField()
    outcome_id = models.ForeignKey(CourseOutcome, on_delete=None)

    def get_absolute_url(self):
        return reverse("assessment:question", kwargs={"id": self.id})


class AssessmentResult(models.Model):
    question = models.ForeignKey(AssessmentQuestion, on_delete=None)
    student = models.ForeignKey(User, on_delete=None)
    obtained_marks = models.PositiveSmallIntegerField()
    remarks = models.TextField()


