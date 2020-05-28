from django.shortcuts import render
import requests
import json
from django_countries.fields import CountryField
from django_countries import countries
# Create your views here.

def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"
    val = request.POST.get('dropdown')
    print(dict(countries)[val])
    x = dict(countries)[val]
    querystring = {"country" : x }

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "ea75790284mshc149cb256a0fafep18274djsn652e67f52063"
        }

    response = requests.request("GET", url, headers=headers, params = querystring).json()
    data = response['response']
    d = data[0]
    print(d)
    context = {
        'all' : d['cases']['total'],
        'recovered' : d['cases']['recovered'],
        'deaths' : d['deaths']['total'],
        'new' : d['cases']['new'],
        'critical' : d['cases']['critical'],
        'tests' : d['tests']['total'],
        'day' : d['day'],
        'time' : d['time'][11:],
        'active' : d['cases']['active'],
        'new_deaths' : d['deaths']['new'],
    }


    return render(request, 'index.html', context)

