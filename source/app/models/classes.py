from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=4, unique= True)

    class Meta:
        verbose_name = 'class'
        verbose_name_plural = 'classes'
        app_label = 'app'

    def __unicode__(self):
        return self.name