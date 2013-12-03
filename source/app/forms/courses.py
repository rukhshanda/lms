from django.forms import ModelForm

from app.models.courses import Course, CourseMaterial, CoursePlan


class CourseForm(ModelForm):
    class Meta:
        model = Course


class CourseMaterialForm(ModelForm):
    class Meta:
        model = CourseMaterial


class CoursePlanForm(ModelForm):
    class Meta:
        model = CoursePlan
