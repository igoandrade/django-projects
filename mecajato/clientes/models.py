from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=150)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class Carro(models.Model):
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)
    ano = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lavagens = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.carro} [{self.cliente}]"

