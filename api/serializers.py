from rest_framework.serializers import ModelSerializer, ListSerializer
from .models import User_data

class User_createSerializer(ListSerializer):
    def create(self, validated_data):
        user = [User_data(**item) for item in validated_data]
        return User_data.objects.bulk_create(user)
    
    class Meta:
        model = User_data
        fields = '__all__'



class User_dataSerializer(ModelSerializer):
    class Meta:
        model = User_data
        fields = ['id', 'username', 'password']