from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import (
    UtenteApplicativo, Medico, Paziente, Misurazione, 
    Soglia, Alert, NotaClinica, Report
)
from .serializers import (
    UtenteApplicativoSerializer, MedicoSerializer, PazienteSerializer, 
    MisurazioneSerializer, SogliaSerializer, AlertSerializer, 
    NotaClinicaSerializer, ReportSerializer
)

# --- UTENTI ---
@csrf_exempt
def utente_list(request):
    if request.method == 'GET':
        utenti = UtenteApplicativo.objects.all()
        serializer = UtenteApplicativoSerializer(utenti, many=True)
        return JsonResponse({'data': serializer.data})
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = UtenteApplicativoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, status=201)
        return JsonResponse({'errors': serializer.errors}, status=400)


# --- MEDICI ---
@csrf_exempt
def medico_list(request):
    if request.method == 'GET':
        medici = Medico.objects.all()
        serializer = MedicoSerializer(medici, many=True)
        return JsonResponse({'data': serializer.data})


# --- PAZIENTI ---
@csrf_exempt
def paziente_list(request):
    if request.method == 'GET':
        pazienti = Paziente.objects.all()
        serializer = PazienteSerializer(pazienti, many=True)
        return JsonResponse({'data': serializer.data})
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = PazienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, status=201)
        return JsonResponse({'errors': serializer.errors}, status=400)


@csrf_exempt
def paziente_detail(request, pk):
    try:
        paziente = Paziente.objects.get(pk=pk)
    except Paziente.DoesNotExist:
        return JsonResponse({'error': 'Paziente non trovato'}, status=404)

    if request.method == 'GET':
        serializer = PazienteSerializer(paziente)
        return JsonResponse({'data': serializer.data})
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = PazienteSerializer(paziente, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data})
        return JsonResponse({'errors': serializer.errors}, status=400)


# --- MISURAZIONI ---
@csrf_exempt
def misurazione_list(request):
    if request.method == 'GET':
        misurazioni = Misurazione.objects.all()
        serializer = MisurazioneSerializer(misurazioni, many=True)
        return JsonResponse({'data': serializer.data})
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = MisurazioneSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, status=201)
        return JsonResponse({'errors': serializer.errors}, status=400)


# --- SOGLIE ---
@csrf_exempt
def soglia_list(request):
    if request.method == 'GET':
        soglie = Soglia.objects.all()
        serializer = SogliaSerializer(soglie, many=True)
        return JsonResponse({'data': serializer.data})


# --- ALERTS ---
@csrf_exempt
def alert_list(request):
    if request.method == 'GET':
        alerts = Alert.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        return JsonResponse({'data': serializer.data})


# --- NOTE CLINICHE ---
@csrf_exempt
def nota_list(request):
    if request.method == 'GET':
        note = NotaClinica.objects.all()
        serializer = NotaClinicaSerializer(note, many=True)
        return JsonResponse({'data': serializer.data})
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = NotaClinicaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, status=201)
        return JsonResponse({'errors': serializer.errors}, status=400)


# --- REPORT ---
@csrf_exempt
def report_list(request):
    if request.method == 'GET':
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return JsonResponse({'data': serializer.data})