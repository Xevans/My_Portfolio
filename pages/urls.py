from django.urls import path
from .views import welcome, apiTest, nameToAge, pokemonAPI

urlpatterns = [
    path('', welcome, name='welcome'),
    path('api_test/', apiTest, name='api-test'),
    path('nameToAge/', nameToAge, name='name-age'),
    path('pokeAPI/', pokemonAPI, name='pokeAPI'),
    
]