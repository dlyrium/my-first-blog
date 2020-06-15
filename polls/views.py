from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

PUBLISHED_ONLY = Question.objects.filter(pub_date__lte=timezone.now())


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        valid_questions = []
        for question in PUBLISHED_ONLY:
            if question.choice_set.all():
                valid_questions.append(question)
        # .order_by('-pub_date')[:5]
        return valid_questions[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    # Exclude questions not published yet.
    def get_queryset(self):
        return PUBLISHED_ONLY


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        return PUBLISHED_ONLY


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice!", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
