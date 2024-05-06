from django.shortcuts import render
import requests
from django.http import HttpResponse
from .forms import NameForm


# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def projects(request):
    return render(request, '')

def apiTest(request):
    # pull from 3rd part rest api
    response = requests.get('https://jsonplaceholder.typicode.com/users')

    #convert data to json
    pulled_users_data = response.json() # a json is already a dictionary, so you can bind it to your template and access the keys for displaying their values
    
    #print(pulled_users_data) # testing data consumed

    return render(request, "api_test.html", {'pulled_users': pulled_users_data})

def nameToAge(request):

    name_form = NameForm(request.POST)
    my_age = None

    if request.method == 'POST':

        if name_form.is_valid():
            this_name = name_form.cleaned_data['name']
            name_param = "name=" + str(this_name) # construct one parameter at a time
            api_url = "https://api.agify.io/?" + name_param # use modularity to construct url with all required/valid parameters
            print(api_url)

            response = requests.get(api_url)
            my_age = response.json()
            print(my_age)
        else:
            print('bad data')

    else:
        name_form = NameForm(request.POST)

    return render(request, 'nameToAge.html', {'my_age': my_age, 'name_form': name_form})



def pokemonAPI(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
    pokemon_data = response.json()
    print(pokemon_data)
    return render(request, 'poke_api.html')