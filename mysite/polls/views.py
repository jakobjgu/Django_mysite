from django.http import HttpResponse
from .models import Question

def index(request):
    return HttpResponse("Hello World. You're at the polls index.")


def detail(request, question_id):
    q = Question.objects.get(pk=question_id)
    question_txt = q.question_text
    response_text = f"""You're looking at question {question_id}.
                         The question you are being asked is: {question_txt}
                      """
    return HttpResponse(response_text)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you're voting on question %s." % question_id)
