from django.urls import path
from .views import CurrentAffairsTemplateView, HomePageTemplateView

urlpatterns = [
    path("", HomePageTemplateView.as_view(), name="home"),
    path("current-affairs/", CurrentAffairsTemplateView.as_view(), name="current-affairs"),
]