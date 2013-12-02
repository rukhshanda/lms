from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField()
    members = models.ManyToManyField('Student', through='CourseMembership')

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        app_label = 'app'

    def __unicode__(self):
        return self.name


class CourseMembership(models.Model):
    student = models.ForeignKey('Student')
    course = models.ForeignKey('Course')

    class Meta:
        verbose_name = 'coursemembership'
        verbose_name_plural = 'coursememberships'
        app_label = 'app'
