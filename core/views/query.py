from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from parser.drom import Drom

from user_profile.serializers import CarSerializer

from core.models import (
    Brand,
    Model,
    Generation,
    Modification,
)
from core.serializers import (
    QueryResultSerializer,
)

class QueryAPIView(APIView):
    car_serializer_class = CarSerializer
    serializer_class = QueryResultSerializer

    def get(self, request):
        get_data = request.GET.dict()
        brand = Brand.objects.get(
            name=get_data.get('brand')
        )
        model = Model.objects.filter(
            brand=brand,
            name=get_data.get('model')
        ).first()
        generation = Generation.objects.filter(
            model=model,
            number=get_data.get('generation')
        ).first()
        modification = Modification.objects.filter(
            generation=generation,
            fuel=get_data.get('engine_fuel'),
            volume=get_data.get('engine_volume')
        ).first()
        car = dict({
            'brand': brand.id,
            'model': model.id if model else None,
            'generation': generation.id if generation else None,
            'modification': modification.id if modification else None
        })
        car_serializer = self.car_serializer_class(data=car)
        if car_serializer.is_valid():
            car_serializer.save(user=request.user)

        query = Drom().get_query_html(**get_data)
        data = Drom().get_min_max_avg_price(query)

        car = dict({
            **car,
            **data,
            'query': get_data.get('query')
        })
        serializer = self.serializer_class(data=car)
        if serializer.is_valid():
            serializer.save(user=request.user)
        return Response({ **data }, status=HTTP_200_OK)
