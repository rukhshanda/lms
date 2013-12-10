from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=10, unique= True)
    start_date = models.DateField()
    end_date = models.DateField()
    cclass = models.ForeignKey('Class')
    representative = models.ForeignKey('Student', related_name='representative', null=True, blank=True)

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        app_label = 'app'

    def __unicode__(self):
        return self.name

    def get_absolure_url(self):
        return "/dashboard/group/%i/" % self.id
