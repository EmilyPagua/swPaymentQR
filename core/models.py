from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    fecha_inicio = models.DateTimeField(auto_now=True)
    fecha_finalizacion = models.DateTimeField(blank=True, null=True)
    propietario = models.ForeignKey(User, related_name='propietario')
    todo = models.TextField()
    hecho = models.BooleanField(default=False)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.propietario,self.todo)


class UserPerfil(models.Model):
    user = models.ForeignKey(User, related_name='user')
    is_company = models.BooleanField(default=False)
    code = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'{0} - {1} - {2}'.format(self.user,self.is_company,self.code)


class TypeCard(models.Model):
    name = models.TextField(blank=False, null=False)

    def __unicode__(self):
        return u'{0}'.format(self.name)


class Card(models.Model):
    type_card = models.ForeignKey(TypeCard, related_name='type_card')
    owner = models.ForeignKey(User, related_name='owner')
    number_card = models.IntegerField(blank=False, null=False)
    name_card = models.TextField(blank=False, null=False)
    expiration_year = models.DateField(blank=False, null=False)
    available = models.IntegerField(blank=False, null=False)

    def __unicode__(self):
        return u'{0} - {1} - {2}'.format(self.type_card, self.name_card, self.owner)


class Transaction(models.Model):
    card = models.ForeignKey(Card, related_name='card')
    collect = models.ForeignKey(User, related_name='collect')
    date_transaction = models.DateTimeField(auto_now=True)
    amount = models.IntegerField(blank=False, null=False)

    def __unicode__(self):
        return u'{0} - {1} - {2}'.format(self.card, self.collect, self.amount)
