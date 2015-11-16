# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.
class Group(models.Model):
    __tablename__ = 'cp_group'

    name_group = models.CharField(max_length=50)
    url = models.CharField(max_length=160, verbose_name='Url Web')
    
    def __str__(self):
        return self.name_group


class User(models.Model):
    __tablename__ = 'cp_user'
    
    USER = 'USER'
    ADMI = 'ADMI'
    ROL_CHOICES = (
        (USER, 'User'),
        (ADMI, 'Administrator'),
    )
    
    name = models.CharField(max_length=60, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    
    rol = models.CharField(max_length=4,
                                      choices=ROL_CHOICES,
                                      default=USER,
                                      blank=False,
                                      )
    
    group = models.ForeignKey('Group')
    phone = models.CharField(max_length=18, blank=False)
    address = models.CharField(max_length=220)
    email = models.CharField(max_length=180, blank=False)
    
    
    def full_name(self):
        return '{} {}'.format(self.name, self.last_name)

    def __str__(self):
        return u'{} {}'.format(self.name, self.last_name)


class Message(models.Model):
    __tablename__ = 'cp_message'

    text = models.CharField(max_length=512)
    user = models.ForeignKey('User')
    ts_send = models.DateTimeField()
    ts_received = models.DateTimeField()



class Payment(models.Model):
    __tablename__ = 'cp_payment'

    year = models.IntegerField()
    month = models.IntegerField()
    user = models.ForeignKey('User')
    f_payment = models.DateTimeField()
    amount = models.FloatField(default=0.0)
    

class Device(models.Model):
    __tablename__ = 'cp_device'
    
    NFC = 'nfc'
    MAC = 'mac'
    DEVICE_CHOICES = (
        (NFC, 'NFC'),
        (MAC, 'MAC'),
    )

    user = models.ForeignKey('User')
    kind = models.CharField(max_length=3,
                                      choices=DEVICE_CHOICES,
                                      default=NFC,
                                      blank=False,
                                      )
    code = models.CharField(max_length=64, blank=False)
    
    def __str__(self):
        return 'Device {}:{}'.format(self.kind, self.code)


class Log(models.Model):
    __tablename__ = 'cp_log'

    user = models.ForeignKey('User')
    ts_input = models.DateTimeField()
    ts_output = models.DateTimeField()
    
    