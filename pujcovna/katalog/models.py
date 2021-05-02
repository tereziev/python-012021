from django.db import models

class Auto(models.Model):
    registracni_znacka = models.CharField(max_length=10)
    znacka_typ = models.CharField(max_length=100)
    ujeto_km = models.IntegerField()
    technicka = models.DateField()

class Zakaznik(models.Model):
    jmeno_prijmeni = models.CharField(max_length=100)
    cislo_ridicaku = models.IntegerField()
    datum_narozeni = models.DateField()

class Vypujcka(models.Model):
    datum_a_cas_zacatku_vypujcky = models.DateTimeField()
    datum_a_cas_konce_vypujcky  = models.DateTimeField()
    cena_vypujcky = models.IntegerField()