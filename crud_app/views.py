from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from crud_app.models import Question
from .forms import QuestionForm

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, "crud_app/index.html", context)

def add(request):
    context = {}
 
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "crud_app/create_question.html", context)

def detail_view(request, id):
    context ={}
    context["question"] = Question.objects.get(id = id)
         
    return render(request, "crud_app/detail_view.html", context)

def update_view(request, id):
    print(id)
    context ={}
 
    obj = get_object_or_404(Question, id = id)
 
    # pass the object as instance in form
    form = QuestionForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/crud/show/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "crud_app/update_question.html", context)

def delete_view(request, id):
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Question, id = id)
 
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/crud")
 
    return render(request, "crud_app/delete_view.html", context)