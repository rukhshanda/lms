from django.db import models

#
# class StudentFeedbackCourse(models.Model):
#     student = models.ManyToManyField('Student')
#     course = models.ManyToManyField('Course')
#     date = models.DateField()
#     text = models.TextField(max_length=5000)
#
#     class Meta:
#         verbose_name = 'result'
#         verbose_name_plural = 'results'
#         app_label = 'app'
#
#
# class SubjectResult(models.Model):
#     result = models.ForeignKey('Result', related_name='subjects')
#     subject = models.CharField(max_length=40)
#     mcqs = models.FloatField()
#     seqs = models.FloatField()
#     total = models.FloatField()
#     ospe = models.FloatField()
#     grandtotal = models.FloatField()

