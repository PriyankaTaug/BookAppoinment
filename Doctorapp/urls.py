from django.urls import path
from Doctorapp.views import *


app_name = "Doctorapp"

urlpatterns = [
    path('DoctorCreate/',DoctorCreate.as_view(),name='DoctorCreate'),
    path('NurseCreate/',NurseCreate.as_view(),name='NurseCreate'),
    path('AppoinmentCreate/',AppoinmentCreate.as_view(),name='AppoinmentCreate'),
    path('AtendanceCreate/',AtendanceCreate.as_view(),name='AtendanceCreate'),
    path('AttednanceReport/',AttednanceReport.as_view(),name='AttednanceReport'),
    path('TodayAppoinment/',TodayAppoinment.as_view(),name='TodayAppoinment'),

]
