from rest_framework import serializers

from . import models


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
    course = CourseSerializers(many=True, read_only=True)

    class Meta:
        model = models.Studentdata
        fields = '__all__'
