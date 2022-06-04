from django.urls import path
from .views import RecordViews, RecordgetViews

urlpatterns = [
    path('new/', RecordViews.as_view()),
    path('all/', RecordgetViews.as_view())
]