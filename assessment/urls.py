from django.urls import path, re_path
from .views import (
    assessment_create,
    question_create,
    )

app_name = 'assessment'
urlpatterns = [

    path('create/', assessment_create, name='create'),
    #re_path(r'^create/(?P<pk>[0-9]+)/question$', views.AssessmentQuestion.as_view(), name='question'),
    path('create/question/',question_create, name='question')
]