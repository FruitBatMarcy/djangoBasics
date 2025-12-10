from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

tasks = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    #if add.html submits a post response
    if request.method == "POST":
        #get the data in the post
        form = NewTaskForm(request.POST)
        #validate
        if form.is_valid():
            #get data and append it to the list of tasks
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            #if data is invalid send data back to be resubmitted
            return render(request, "tasks/add.html", {
                "form": form
            })


    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })