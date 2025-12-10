from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms



class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.

def index(request):
    if "tasks" not in request.session:
        #create empty list called tasks if not in session
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
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
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            #if data is invalid send data back to be resubmitted
            return render(request, "tasks/add.html", {
                "form": form
            })


    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })