from django import forms
from .models import Assessment, AssessmentQuestion


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = [
            'course_id',
            'assessment_type',
            'start_date',
            'duration',
            'faculty_id'
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = AssessmentQuestion
        fields = [
            'question_type',
            'assessment_id',
            'text',
            'max_marks',
            'question_order',
            'marking_scheme',
            'outcome_id'
        ]