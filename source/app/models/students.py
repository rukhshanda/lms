from django.db import models
from django.contrib.auth.models import User


class Student(User):
    GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    roll_no = models.CharField(max_length=11, unique= True)
    _class = models.ForeignKey('Class')
    group = models.ForeignKey('Group')

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
        app_label = 'app'

    def __unicode__(self):
        return self.get_full_name()