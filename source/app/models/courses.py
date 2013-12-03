from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField()
    exam_date = models.DateTimeField()
    evaluation_date = models.DateField()
    published = models.BooleanField(default=False)
    _class = models.ForeignKey('Class')
    teachers = models.ManyToManyField('Teacher', through='CourseTeachers')

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        app_label = 'app'

    def __unicode__(self):
        return self.name

    def get_absolure_url(self):
        return "/course/%i/" % self.id


class CourseMaterial(models.Model):
    title = models.CharField(max_length=100L)
    file = models.FileField(upload_to='/course/material/')
    course = models.ForeignKey('Course')

    class Meta:
        verbose_name = 'coursematerial'
        verbose_name_plural = 'coursematerials'
        app_label = 'app'

    def get_absolure_url(self):
        return "/course/material/%i/" % self.id


class CoursePlan(models.Model):
    course = models.ForeignKey('Course')
    teacher = models.ForeignKey('Teacher')
    week = models.IntegerField()
    contents = models.TextField(max_length=5000)

    class Meta:
        verbose_name = 'courseplan'
        verbose_name_plural = 'courseplans'
        app_label = 'app'

    def get_absolure_url(self):
        return "/course/plan/%i/" % self.id


class CourseTeachers(models.Model):
    course = models.ForeignKey('Course')
    teacher = models.ForeignKey('Teacher')
    course_coordinator = models.BooleanField()

    class Meta:
        verbose_name = 'courseteacher'
        verbose_name_plural = 'courseteachers'
        app_label = 'app'
