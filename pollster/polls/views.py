from django.http.response import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Question, Choice

# Get questions and display them


def index(request):
    # ('-pub_date') = sort by descending
    # [:5] how many we want or slice the query it by 5
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # in order to pass it on to the template, pass natin ng object or dictionary
    # good practice is context

    # context syntax is creating a dictionary
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
# Show specific questions and choice


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# Get question and display results


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Vote for a question choice


def vote(request, question_id):
    # print (request.POOST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html',
                      {'question': question,
                       'error_message': "You didnt select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after dealing with POST data.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
