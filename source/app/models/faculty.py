from django.db import models
from django.contrib.auth.models import User


class Teacher(User):
    GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
    SPECIALITY_CHOICES = (('anatomy', 'Anatomy'), ('physiology', 'Physiology'))

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    speciality = models.CharField(max_length=10, choices=SPECIALITY_CHOICES)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        app_label = 'app'

    def __unicode__(self):
        return self.get_full_name()

    def get_absolure_url(self):
        return "/teacher/%i/" % self.id
