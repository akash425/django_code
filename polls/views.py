from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Create your views here.
from .models import Question, Choice

#Get Questions and display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html' , context)
#Show Specific question-answer

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Not Found")
    return render(request, 'polls/detail.html', { 'question':question})


#Get Question and view results

def results(request, question_id):
    question = get_object_or_404(Question, question_id)
    return render(request, 'polls/result.html', { 'question': question })

# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request, 'polls/detail.html', {'question':question, 'error_message': "You did'nt selected Choice"})
    
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))