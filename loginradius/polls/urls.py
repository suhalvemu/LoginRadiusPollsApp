from django.urls import path,include
from django.views.generic import TemplateView
from .LoginView import *
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login',ViewLogManual.as_view(),name='login'),
    path('votes',DisplayPolls.as_view(),name='votes'),
    path('results',PollResults.as_view(),name='results'),
    path('logout', logout_request,name='logout')
]