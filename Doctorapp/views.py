from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from Doctorapp.serializers import *
from datetime import datetime as dt
# Create and view Doctor.

class DoctorCreate(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = DoctorSerialzier(data = data)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse({"status":"Successfully created doctor"},safe=False)
        except Exception as e:
            return JsonResponse({"status":"Error"},safe=False)
        
    def get(self,request):
        try:
            data = Doctor.objects.all()
            serializer = DoctorSerialzier(data,many=True)
            return JsonResponse(serializer.data,safe=False)
        except Exception as e:
            return JsonResponse({"status":"Error"},safe=False)


class NurseCreate(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = NurseSerialzier(data = data)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse({"status":"Successfully created nurse"},safe=False)
        except Exception as e:
            return JsonResponse({"status":"Error"},safe=False)
        
    def get(self,request):
        try:
            data = Nurse.objects.all()
            serializer = NurseSerialzier(data,many=True)
            return JsonResponse(serializer.data,safe=False)
        except Exception as e:
            return JsonResponse({"status":"Error"},safe=False)
        


class AppoinmentCreate(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = AppoinmentSerialzier(data = data)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse({"status":"Successfully created an appoinment"},safe=False)
        except Exception as e:
            return JsonResponse({"status":"Error"},safe=False)
        
    def get(self,request):
        try:
            data = Appoinment.objects.all()
            serializer = AppoinmentSerialzier(data,many=True)
            return JsonResponse(serializer.data,safe=False)
        except Exception as e:
            return JsonResponse({"status":"Error"},safe=False)
        

class AtendanceCreate(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = AttendanceSerialzier(data = data)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse({"status":"Successfully created an Attendance"},safe=False)
        except Exception as e:
            return JsonResponse({"status":"Error"},safe=False)
        
   
'''Today attendance'''
class AttednanceReport(APIView):
    def get(self,request):
        try:
            total_doctor = Doctor.objects.all().count()
            total_nurse = Nurse.objects.all().count()
            total_employee = Employee.objects.all().count()
            att_date = dt.now().date
            doctor_data = Attendance.objects.filter(role="Doctor",att_date=att_date).count()
            nurse_data = Attendance.objects.filter(role="Nurse",att_date=att_date).count()
            employee_data = Attendance.objects.filter(role="Employee",att_date=att_date).count()
            data ={
                  "doctor_data":doctor_data,
                   "total_doctor":total_doctor,
                   "nurse_data":nurse_data,
                   "total_nurse":total_nurse,
                   "employee_data":employee_data,
                   "total_employee":total_employee,
            }
            return JsonResponse({"status":data},safe=False)
        
        except Exception as e:
            return JsonResponse({"status":str(e)},safe=False)
        

'''Today's appoinment'''

class TodayAppoinment(APIView):
    def get(self,request):
        try:
            att_date = dt.now().date
            completed_data = Appoinment.objects.filter(status="Completed",app_date=att_date).count()
            pending_data = Appoinment.objects.filter(role="Pending",app_date=att_date).count()
            cancelled_data = Appoinment.objects.filter(role="Canceled",app_date=att_date).count()
            data ={
                "completed_data":completed_data,
                "pending_data":pending_data,
                "cancelled_data":cancelled_data
            }
            return JsonResponse({'status':data},safe=False)
        except Exception as e:
            return JsonResponse({'status':'error'},safe=False)