import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

import django
django.setup()

from aplicacion.models import Usuario, Tweet, Retweet


def populate():

    for aut in Usuario.objects.order_by('username'):
            aut.delete()
    for t in Tweet.objects.order_by('id'):
            t.delete()
    for r in Retweet.objects.order_by('id'):
            r.delete()
    
    usuarios = [
        {
            'id': 1001,
            'username': 'usuario_01'
        },
        {
            'id': 1002,
            'username': 'usuario_02'
        },
        {
            'id': 1003,
            'username': 'usuario_02'
        }
    ]

    for us in usuarios:
        uss = Usuario(username=us['username'], id=us['id'])
        uss.save()

    tweets = [
        {
            'id': 1001,
            'texto': 'texto de mensaje 01',
            'usuario': Usuario.objects.get(id=1002),
            'fecha': '2021-01-05'
        },
        {
            'id': 1002,
            'texto': 'texto de mensaje 02',
            'usuario': Usuario.objects.get(id=1001),
            'fecha': '2021-01-10'
        },
        {
            'id': 1003,
            'texto': 'texto de mensaje 03',
            'usuario': Usuario.objects.get(id=1002),
            'fecha': '2021-01-12'
        },
        {
            'id': 1004,
            'texto': 'texto de mensaje 04',
            'usuario': Usuario.objects.get(id=1002),
            'fecha': '2021-01-15'
        }
    ]

    for tw in tweets:
        tww = Tweet(id=tw['id'], texto=tw['texto'], usuario=tw['usuario'], fecha=tw['fecha'])
        tww.save()

    retweets = [
        {
            'id': 1001,
            'tweet': Tweet.objects.get(id=1001),
            'usuario': Usuario.objects.get(id=1003),
            'fechaDeRetweet': '2021-01-05'
        },
        {
            'id': 1002,
            'tweet': Tweet.objects.get(id=1001),
            'usuario': Usuario.objects.get(id=1001),
            'fechaDeRetweet': '2021-01-10'
        },
        {
            'id': 1003,
            'tweet': Tweet.objects.get(id=1002),
            'usuario': Usuario.objects.get(id=1003),
            'fechaDeRetweet': '2021-01-12'
        },
        {
            'id': 1004,
            'tweet': Tweet.objects.get(id=1003),
            'usuario': Usuario.objects.get(id=1003),
            'fechaDeRetweet': '2021-01-15'
        }
    ]

    for rtw in retweets:
        rtww = Retweet(id=rtw['id'], tweet=rtw['tweet'], usuario=rtw['usuario'], fechaDeRetweet=rtw['fechaDeRetweet'])
        rtww.save()

if __name__ == '__main__':
    print("Starting catalog population script...")
    populate()
    print("Done!")