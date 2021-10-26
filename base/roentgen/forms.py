from .models import PatientModel
from django.forms import  ModelForm, TextInput, DateTimeInput, Textarea


class PatientForm(ModelForm):
    class Meta:
        model = PatientModel
        fields = ['LastName', 'FirstName', 'MiddleName', 'Department', 'ReceiptDate', 'Diagnosis1', ] # , 'idPatient',
        #fields = '__all__'

        widgets = {
            "LastName": TextInput(attrs={
                'placeholder': 'Фамилия',
            }),
            "FirstName": TextInput(attrs={
                'placeholder': 'Имя',
            }),
             "MiddleName": TextInput(attrs={
                'placeholder': 'Отчество',
            }),
            "ReceiptDate": DateTimeInput(attrs={
                'placeholder': 'Дата поступления',
            }),

        }

        labels = {
            'LastName': 'Пациент',
            'FirstName': '',
            'MiddleName': '',
            'ReceiptDate': 'Дата поступления',
            'DateBirth': 'Дата рождения',
            'Department': 'Отделение',
            'Diagnosis1': 'Диагноз при поступлении',
        }
