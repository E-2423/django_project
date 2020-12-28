from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm


def home_view(request):
    # return HttpResponse("This is about page")
    
    form = StudentForm()
    
    my_context = {
        'title': '<b>Clarusway</b>',
        'dict_1': {'django':'best framework'},
        'my_list': [2, 3, 4, 5],
        'form': form
        
    }
    return render(request, "fscohort/home.html", my_context)

def about(request):
    return HttpResponse("About Page")

# Create your views here.
