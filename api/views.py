from rest_framework import status, generics, filters
from django.db.models import Sum, F

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer, ColorSerializer, CarBrandSerializer, CarModelSerializer, \
    QuantitySerializer

from .models import Order, Color, CarBrand, CarModel


names = {
    'Order': [Order, OrderSerializer],
    'Color': [Color, ColorSerializer],
    'CarBrand': [CarBrand, CarBrandSerializer],
    'CarModel': [CarModel, CarModelSerializer],

}


def model_list(model_name):
    model = names[model_name][0]
    model_serializer = names[model_name][1]

    @api_view(['GET', 'POST'])
    def _model_list(request):
        if request.method == 'GET':
            objects = model.objects.all()
            serializer = model_serializer(objects, many=True)
            for data in serializer.data:
                data['car_model'] = CarModel.objects.get(id=data['car_model']).title
                data['color'] = Color.objects.get(id=data['color']).title

            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = model_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return _model_list


def model_detail(model_name):
    model = names[model_name][0]
    model_serializer = names[model_name][1]

    @api_view(['GET', 'PUT', 'DELETE'])
    def _model_detail(request, pk):
        try:
            object = model.objects.get(pk=pk)
        except model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = model_serializer(object)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = model_serializer(object, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    return _model_detail


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['car_model__title']
    ordering_fields = ['quantity']


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ColorList(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class CarBrandList(generics.ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarBrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarModelList(generics.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class ColorQuantity(generics.ListAPIView):
    queryset = Order.objects.annotate(title=F('color__title')).values('title').annotate(quantity=Sum('quantity'))
    serializer_class = QuantitySerializer


class BrandsQuantity(generics.ListAPIView):
    queryset = Order.objects.annotate(title=F('car_model__car_brand__title')).values('title').annotate(quantity=Sum('quantity'))
    serializer_class = QuantitySerializer
