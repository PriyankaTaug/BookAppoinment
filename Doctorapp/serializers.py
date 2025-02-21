from rest_framework import serializers
from Doctorapp.models import *


class DoctorSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class NurseSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = "__all__"

class EmployeeSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class AppoinmentSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Appoinment
        fields = "__all__"


class AttendanceSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"