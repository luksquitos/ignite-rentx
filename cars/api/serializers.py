from rest_framework import serializers
from cars.models import Carro, Fabricante, ImagemCarro



class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["imagem"]
        model = ImagemCarro


class CarroSerializer(serializers.ModelSerializer):
    imagens = ImagemSerializer(many=True, read_only=True)
    fabricante = serializers.SerializerMethodField('get_fabricante')
    quant_disponivel = serializers.IntegerField(read_only=True)

    def get_fabricante(self, obj):
        return obj.fabricante.nome

    class Meta:
        model = Carro
        exclude = ["quantidade"]
