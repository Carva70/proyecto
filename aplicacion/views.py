from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from .models import Usuario, Tweet, Retweet


def index(request):
    
    context = {
        'retweets': Retweet.objects.order_by('fechaDeRetweet'),
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


