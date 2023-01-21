from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    
    #Esse método foi escrito pelo
    #próprio Fernando
    
    # def get_user
    
    class Meta:
        fields = "__all__"