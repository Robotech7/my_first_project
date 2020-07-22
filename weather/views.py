from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import requests
from configs import settings


class WeatherView(LoginRequiredMixin, View):
    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&lang=ru&appid=' + \
          settings.OPEN_WEATHER_MAP_API

    def get(self, request):
        return render(request, 'weather/weather.html')

    def post(self, request):
        city = request.POST['city']
        data = requests.get(self.url.format(city)).json()

        return JsonResponse(data)

