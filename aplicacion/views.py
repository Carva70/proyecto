from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from .models import Usuario, Tweet, Retweet


def index(request):

    if Retweet.objects.order_by('fechaDeRetweet').count() == 0:
        return render(request, 'index.html', context = {'error': 'Error: base de datos vacía'})



    context = {
        'retweets': Retweet.objects.order_by('fechaDeRetweet').filter(tweet__usuario=Usuario.objects.get(id=1002)),
        'username': Usuario.objects.get(id=1002).username
    }

    return render(request, 'index.html', context=context)

