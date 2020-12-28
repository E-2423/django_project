from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    # return HttpResponse("This is about page")
    my_context = {
        'title': '<b>Clarussway</b>',
        'dict_1': {'django':'best framework'},
        'my_list': [2, 3, 4, 5]
    }
    return render(request, "fscohort/home.html", my_context)

def about(request):
    return HttpResponse("About Page")

# Create your views here.
