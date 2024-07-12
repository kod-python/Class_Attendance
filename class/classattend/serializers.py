from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'firstName', 'lastName', 'email', 'course', 'created', 'updated']
       
       
         
    def validate_csrf_token(self, value):
        if value != 'expected_csrf_token': 
            raise serializers.ValidationError("Invalid CSRF token")
        return value

    def validate_email(self, value):
        if Attendance.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value


    



