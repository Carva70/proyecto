from django.contrib import admin

# Register your models here.

from .models import Usuario, Tweet, Retweet


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username',)

    fields = ['username',]

class TweetAdmin(admin.ModelAdmin):
    list_display = ('texto', 'usuario', 'fecha')

    fields = ['texto', 'usuario', 'fecha']

class RetweetAdmin(admin.ModelAdmin):
    list_display = ('tweet', 'usuario', 'fechaDeRetweet')

    fields = ['tweet', 'usuario', 'fechaDeRetweet']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Retweet, RetweetAdmin)