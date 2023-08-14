from rest_framework import serializers
from task.models import Product

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"