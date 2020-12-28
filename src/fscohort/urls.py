from django.urls import path
from fscohort.views import home_view, student_add, student_list

urlpatterns = [
    path("", home_view),
    path("list/", student_list),
    path("add/", student_add),
]
