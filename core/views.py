from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from parser.drom import Drom

# Create your views here.

def home(request):
    return render(request, 'home_page.html')



class CarListAPIView(APIView):
    def get(self, request):
        cars = Drom().get_car_list()
        return Response(cars)



class CarModelListAPIView(APIView):
    def get(self, request, car_name):
        models = Drom().get_car_models(car_name)
        return Response(models)



class ModelGenerationListAPIView(APIView):
    def get(self, request, model_name):
        generations = Drom().get_model_generations(model_name)
        return Response(generations)



class GenerationModificationListAPIView(APIView):
    def get(self, request, model_name, generation):
        modifications = Drom().get_generation_modifications(model_name, generation)
        return Response(modifications)



class QueryAPIView(APIView):
    def get(self, request):
        query = Drom().get_query_html(**request.GET)
        data = Drom().get_min_max_avg_price(query)
        return Response({ **data })
