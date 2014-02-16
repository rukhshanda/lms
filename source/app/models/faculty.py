from django.db import models
from django.contrib.auth.models import User


class TeacherManager(models.Manager):
    def get_queryset(self):
        return super(TeacherManager, self).get_queryset().filter(deleted=False)

class Teacher(User):
    GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
    SPECIALITY_CHOICES = (('anatomy', 'Anatomy'), ('physiology', 'Physiology'))

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    speciality = models.CharField(max_length=10, choices=SPECIALITY_CHOICES)
    deleted = models.BooleanField(default=False)

    # Model managers
    objects = TeacherManager()
    objects_all = models.Manager()

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        app_label = 'app'
        permissions = (
            ('has_faculty_perms', 'Has faculty permissions'),
        )

    def __unicode__(self):
        return self.get_full_name()

    def get_absolure_url(self):
        return "/dashboard/teacher/%i/" % self.id
