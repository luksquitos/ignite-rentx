from django.db import models
from django.db.models.aggregates import Count
from django.contrib.auth.models import User
from cars.models import Carro


class Pessoa(models.Model):
    user = models.ForeignKey(User, models.CASCADE, null=True)
    nome = models.CharField("Nome", help_text='Nome completo', max_length=120)
    email = models.EmailField("Email", unique=True)
    
    #TODO Testar depois o código abaixo
    # com dados no banco
    # https://www.youtube.com/watch?v=2vH3y53FsGI
    
    @property
    def carro_favorito(self):
        # FIXME Pode ser que haja duplicação.
        # Caso tenham utilizar .distinct() antes
        # do annotate
        #
        # var = Carro.objects.filter(
        #     agendamentos__pessoa=self
        # ).annotate(quant_agendamentos=Count('agendamentos'))
        # 
        # return var
        #
        # var irá retornar um Queryset com todos os carros 
        # alugados por tal pessoa, juntamente
        # com um novo att "quant_agendamentos"
        # para cada instância presente no queryset
        # EU ACHO...
        ...

class Agendamento(models.Model):
    is_returned = models.BooleanField("Carro retornado?")
    pessoa = models.ForeignKey(Pessoa, models.CASCADE, related_name="agendamentos")
    carro = models.ForeignKey(Carro, models.DO_NOTHING, related_name='agendamentos')
    dia_agendamento = models.DateField("Dia do agendamento")
    dia_entrega = models.DateField("Dia da entrega")
    
    # Será que isso vai reclamar caso o valor não seja informado no post?
    valor_agendamento = models.FloatField("Valor do agendamento") 
    
    

#Pessoa poder seguir uma fabricante
#Pessoa ver agendamentos de outras pessoas que segue?



