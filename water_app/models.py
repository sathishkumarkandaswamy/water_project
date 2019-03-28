from django.db import models

class WaterParameter(models.Model):
    '''
    Water Model - Parameter fields
    Values for these Parameter shall be added in water testing.
    '''

    title = models.CharField(max_length=1024, unique=True, null=True, blank=True)
    description = models.CharField(max_length=1024, null=True, blank=True)
    coliform_bacteria = models.FloatField('Coliform Bacteria', null=True,  blank=True)
    nitrate = models.FloatField('Nitrate', null=True,  blank=True)
    ph = models.FloatField('pH', null=True,  blank=True)
    sodium = models.FloatField('Sodium', null=True,  blank=True)
    chloride = models.FloatField('Chloride', null=True,  blank=True)
    fluride = models.FloatField('Fluride', null=True,  blank=True)
    sulphate = models.FloatField('Sulphate', null=True,  blank=True)
    iron = models.FloatField('Iron', null=True,  blank=True)

    class Meta:
        verbose_name = "Water Parameter"
        verbose_name_plural = "Water Parameter List"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
