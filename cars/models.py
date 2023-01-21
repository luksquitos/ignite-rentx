from django.db import models


class Fabricante(models.Model):
    nome = models.CharField("Fabricante", max_length=80)

    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name = "Fabricante"
        verbose_name_plural = "Fabricantes"


class Carro(models.Model):
    nome = models.CharField("Nome do carro", max_length=100)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.SET_NULL, null=True, related_name="carros")
    sobre = models.TextField("Sobre o carro")
    combustivel = models.CharField(
        'Combustível', 
        max_length=50, 
        choices=(
            ("Gasolina", "Gasolina"),
            ("Elétrico", "Elétrico"),
            ("Álcool", "Álcool")
        )
    )
    transmissao = models.CharField("Transmissão", max_length=20, choices=(("Automático", "Automático"), ("Manual", "Manual")))
    valor_diaria = models.FloatField("Valor da diária", help_text="R$")
    quantidade_cavalos = models.PositiveIntegerField("Quantidade de cavalos")
    quant_lugares = models.PositiveIntegerField("Quantidade de lugares", default=2)
    quantidade = models.PositiveIntegerField("Quantidade disponível", help_text="Quantidade de carros para alocação")
    
    
    @property
    def quant_disponivel(self):
        from register.models import Agendamento
        quant_agendamentos = Agendamento.objects.filter(
            carro=self, is_returned=False
        ).count()
        return self.quantidade - quant_agendamentos
    
    quant_disponivel.fget.short_description = "Quantidade disponível"
    
    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"


class ImagemCarro(models.Model):
    carro = models.ForeignKey(Carro, models.CASCADE, related_name="imagens")
    imagem = models.FileField("Imagem", upload_to='imagem-carro')
    
    def __str__(self) -> str:
        return f'Imagem {self.id}'
    
    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"

