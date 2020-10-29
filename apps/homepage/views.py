import requests

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.apps import apps
from .models import ChooseMostSold
from .forms import FormContact


def get_model(app_label: str, model_name: str):
    return apps.get_model(app_label, model_name)


def send_message(text):
    url = "https://api.telegram.org/bot1397404758:AAEBfHXgaxWM0j-FGnsFsUxQjo4sMuyEz5Q/"
    params = {
        'chat_id': 399344900,
        'text': text
    }
    requests.post(url + 'sendMessage', data=params)


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            form.save()

            send_message(
                text=f"Поступил новый запрос на звонок:\nИмя: {request.POST['name']}\nПочта: {request.POST['email']}\nТелефон: {request.POST['phone']}\n"
            )

            return HttpResponseRedirect(reverse('home_page:home_page'))

    else:
        model = get_model('bicycle', 'Bicycle')

        most_sold = ChooseMostSold.objects.all().order_by('-id')[0]

        first_most_sold = most_sold.first_bike_id
        second_most_sold = most_sold.second_bike_id

        most_sold1 = model.objects.get(id=first_most_sold)
        most_sold2 = model.objects.get(id=second_most_sold)

        form = FormContact()
        context = {
            'first_most_sold': most_sold1,
            'second_most_sold': most_sold2,
        }
        return render(request, 'index.html', context)
