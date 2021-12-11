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

if __name__ == '__main__':
    print("Deleting database...")
    populate()
    print("Done!")