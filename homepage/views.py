from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone



class IndexView(generic.ListView):
    template_name = 'homepage/index.html'


    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
