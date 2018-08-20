from django.db import models

class Paradigms(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Languages(models.Model):
    name        = models.CharField(max_length=50)
    paradigm    = models.ForeignKey(Paradigms, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Programmers(models.Model):
    name        = models.CharField(max_length=50)
    languages   = models.ManyToManyField(Languages)

    def __str__(self):
        return self.name;


