from django.shortcuts import render
from .models import PatientModel, PatientRecordsModel
import xml.etree.ElementTree as ET
from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponseNotFound
import datetime

class PatientView(ListView):
    model = PatientRecordsModel
    PatientRecords = PatientRecordsModel.objects.values_list('idPatient', flat=True).filter(DateTime__gte=datetime.date.today() - datetime.timedelta(days=3), Department='Рентгеновское') #'2021-10-07'
    template_name = 'roentgen/Home.html'
    idPatientList = list(PatientRecords)
    queryset = PatientModel.objects.filter(idPatient__in=idPatientList).order_by('LastName')


#class RecordsView(ListView):
#    def get_queryset(self):
#        return PatientRecordsModel.objects.filter(idPatient=self.kwargs['pk'])
#    model = PatientRecordsModel
#    template_name = 'roentgen/ChoiceForDelete.html'


def Records(request, pk):
    if request.method == 'GET':
        Records = PatientRecordsModel.objects.filter(idPatient=pk).order_by('-DateTime')
        Patient = PatientModel.objects.get(idPatient=pk)
        return render(request, 'roentgen/ChoiceForDelete.html', {'object_list': Records, 'Patient': Patient})


def ChoiceRecord(request, pk):
    if request.method == 'GET':
        Record = PatientRecordsModel.objects.get(IdRecord=pk)
        root = ET.fromstring('<data> '+Record.ContentRec+' </data>')
        prot = ''
        for child in root:
            #print(child.tag, child.attrib)
            if child.tag == 'строка':
                prot = prot + "<br>"
            for char in child:
                prot = prot + char.attrib['значение']+' '
        Patient = PatientModel.objects.get(idPatient=Record.idPatient)
        return render(request, 'roentgen/DeleteRecords.html', {'Record': Record, 'prot': prot, 'Patient': Patient})
    if request.method == 'POST':
        try:
            Record = PatientRecordsModel.objects.get(IdRecord=pk)
            Record.delete()
            return HttpResponseRedirect('/' + str(Record.idPatient)+"/history")
        except Record.DoesNotExist:
            return HttpResponseNotFound("<h2>Ошибка при удалении. Запись не найдена</h2>")


def Search(request):
    if request.method == 'GET':
        Number = request.GET.get('CardNumber')
        if Number:
            Patient = PatientModel.objects.filter(CardNumber=Number )# + '/' + str(datetime.date.today().year)[2:4]
            if Patient:
                PatientRecords = PatientRecordsModel.objects.filter(idPatient=Patient[0].idPatient).order_by('-DateTime')
                Patient = PatientModel.objects.get(idPatient=Patient[0].idPatient)
                return render(request, 'roentgen/ChoiceForDelete.html', {'object_list': PatientRecords, 'Patient': Patient})
            else:
                return render(request, 'roentgen/Home.html')
        else:
            return render(request, 'roentgen/Home.html')