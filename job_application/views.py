from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages


# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        print("chikkam")
        print(form.errors)
        if form.is_valid():

            print("yes")
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            experience = form.cleaned_data["experience"]
            self_intro = form.cleaned_data["message"]

            preference = form.cleaned_data["remote"]

            Form.objects.create(name=name,email=email,experience=experience,self_intro=self_intro,resume=resume,preference=preference)
            messages.success(request,"Form submitted successfully..!")
            print("yes")
            print(experience)

        else:
            print(form.errors)

    return render(request, 'index.html')
