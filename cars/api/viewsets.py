from rest_framework import viewsets
from cars.models import Carro
from cars.api.serializers import CarroSerializer
from django_filters.rest_framework import DjangoFilterBackend



class CarroViewset(viewsets.ModelViewSet):
    serializer_class = CarroSerializer
    queryset = Carro.objects.all()
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["combustivel", "transmissao"]
    
    #TODO Para fazer o filtro da margem de preço
    # será necessário sobrescrever o método
    # get_queryset, eu acho.
    #
    # Para pegar os parâmetros da URL, será utilizado 
    # o self.request.query_params
    # agora é saber como o queryset é retornado
    # com esse parâmetro
    
    def get_queryset(self):
        print('o dir do request é  ', self.request.query_params)
        queryset = super().get_queryset()
        return queryset
