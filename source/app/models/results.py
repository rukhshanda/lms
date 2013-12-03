from django.db import models


class Result(models.Model):
    student = models.ManyToManyField('Student')
    course = models.ManyToManyField('Course')
    date = models.DateField()
    score_total = models.FloatField()
    score_percentage = models.FloatField()

    class Meta:
        verbose_name = 'result'
        verbose_name_plural = 'results'
        app_label = 'app'


class SubjectResult(models.Model):
    result = models.ForeignKey('Result', related_name='subjects')
    subject = models.CharField(max_length=40)
    mcqs = models.FloatField()
    seqs = models.FloatField()
    total = models.FloatField()
    ospe = models.FloatField()
    grandtotal = models.FloatField()

    class Meta:
        verbose_name = 'subject_result'
        verbose_name_plural = 'subject_results'
        app_label = 'app'
