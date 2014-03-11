from django.db import models
from django.contrib.auth.models import User


class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(deleted=False)

class Student(User):
    GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    roll_no = models.CharField(max_length=11, unique= True)
    cclass = models.ForeignKey('Class', related_name='students')
    group = models.ForeignKey('Group')
    deleted = models.BooleanField(default=False)

    # Model managers
    objects = StudentManager()
    objects_all = models.Manager()

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
        app_label = 'app'
        permissions = (
            ('has_student_perms', 'Has student permissions'),
        )

    def __unicode__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return "/dashboard/student/%i/" % self.id
