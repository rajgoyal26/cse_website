from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Assessment, AssessmentQuestion
from django.urls import reverse, reverse_lazy
from .forms import AssessmentForm, QuestionForm
from django.http import HttpResponse, HttpResponseRedirect


"""class AssessmentCreate(CreateView):
    template_name =  'assessment/assessment_form.html'
    model = Assessment
    fields = ['course_id', 'assessment_type', 'start_date', 'duration', 'faculty_id']

    #def get_success_url(self, **kwargs):
     #   return reverse('assessment:question', kwargs={'pk': self.object.pk})

class AssessmentQuestion(CreateView):
    model = AssessmentQuestion
    fields = ['question_type', 'assessment_id', 'text', 'max_marks', 'question_order', 'marking_scheme', 'outcome_id']"""


def assessment_create(request):
    #instance = get_object_or_404(AssessmentQuestion, id=id)
    form = AssessmentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('question/')
    context = {
        "form": form,
    }

    def get_success_url(self):
        success_url = reverse_lazy('assessment:question', {'id': self.object.pk})
        return success_url
    return render(request, "assessment/assessment_form.html", context)


def question_create(request):
   # instance = get_object_or_404(AssessmentQuestion, id=id)
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "assessment/question_form.html", context)