from django.urls import path
from fscohort.views import home_view, student_add, student_list, student_detail

urlpatterns = [
    path("", home_view, name="home"),
    path("list/", student_list, name="list"),
    path("add/", student_add, name="add"),
    path("<int:id>", student_detail, name="detail"),
]
