from django.shortcuts import render
from  .forms import ApplicationForm

# Create your views here.


def index(request):
    if request == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data('name')
            email = form.cleaned_data('email')
            experience = form.cleaned_data('experience')
            messege = form.cleaned_data('message')
            loc = form.cleaned_data('remote')
            print(experience)



    return render(request,'index.html')