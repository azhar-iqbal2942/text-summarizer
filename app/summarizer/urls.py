from django.urls import path

from .views import TextSummarizerView

urlpatterns = [path("summarize", TextSummarizerView.as_view())]
