# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings 


class CoinsAvailableModel(models.Model):
    coin = models.IntegerField()
    
    def __unicode__(self):
        return str(self.coin)

    class Meta:
        verbose_name_plural = "Coins"


class CoinsDeterminedModel(models.Model):
    number = models.IntegerField()
    num_coins = models.IntegerField()
