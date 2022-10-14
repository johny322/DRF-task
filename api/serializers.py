from rest_framework import serializers
from .models import Task, Color, CarBrand, CarModel, Order


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['color'] = instance.color.title
        response['car_model'] = instance.car_model.title
        response['car_brand'] = instance.car_model.car_brand.title
        return response

    class Meta:
        model = Order
        fields = ['car_model', 'color', 'quantity', 'date']
        order_by = ('quantity',)


class QuantitySerializer(serializers.Serializer):
    title = serializers.CharField()
    quantity = serializers.IntegerField()
