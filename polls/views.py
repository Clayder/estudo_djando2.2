from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from polls.models import Question
from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }

    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("Retornando perguntas pelo id: %s." % question_id)


def results(request, question_id):
    response = "Resultados da pergunta %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Você está votando na pergunta %s" % question_id)

