from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Patient, MedicalRecord
from .serializers import PatientSerializer, MedicalRecordSerializer
import pandas as pd
import plotly.express as px 
from django.http import JsonResponse


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'age', 'gender']
    search_fields = ['name', 'contact_info']


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()    
    serializer_class = MedicalRecordSerializer
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['diagnosis', 'date']
    search_fields = ['diagnosis', 'treatment_plan']


def medical_data_chart(request): 
    records = MedicalRecord.objects.all()

    data = [
        {'patient': r.patient.name, 'diagnosis': r.diagnosis, 'date': r.date}
        for r in records
    ]

    df = pd.DataFrame(data)
    fig = px.bar(df, x='date', y='diagnosis', color='patient')

    graph_json = fig.to_json()
    return JsonResponse(graph_json, safe=False)


def patient_data_analytics(request):
    patients = Patient.objects.all().values('name', 'age', 'gender')
    records = MedicalRecord.objects.all().values('diagnosis', 'date', 'patient__name')

    patient_df = pd.DataFrame(list(patients))
    record_df = pd.DataFrame(list(records))

    total_patients = patient_df.shape[0]

    average_age = patient_df['age'].mean()

    coomon_diagnosis = record_df['diagnosis'].value_counts().idxmax()

    total_records = record_df.shape[0] 

    fig = px.pie(patient_df, names='gender', title='Gender Distribution')

    graph_json = fig.to_json()

    analytics = {
        "total_patients": total_patients,
        "average_age": average_age,
        "common_diagnosis": coomon_diagnosis,
        "total_records": total_records,
        "gender_distribution_chart": graph_json,
    }
    return JsonResponse(analytics)
