from django.urls import path
from fscohort.views import home_view

urlpatterns = [
    path("", home_view),
    # path("about/", about)
]
