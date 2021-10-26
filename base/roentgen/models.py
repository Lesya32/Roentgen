from django.db import models


class PatientModel(models.Model):
    Department_Choices = (
        ['приемное', 'приемное'],
        ['отказные', 'отказные'],
        ['терапевтическое', 'терапевтическое'],
        ['ифекционное', 'ифекционное'],
        ['для больных с ОНМК', 'для больных с ОНМК'],
    )
    idPatient = models.IntegerField(db_column='ИдПациент', primary_key=True, unique=True)
    LastName = models.CharField(db_column='Фамилия', max_length=50, blank=True, null=True)
    FirstName = models.CharField(db_column='Имя', max_length=15, blank=True, null=True)
    MiddleName = models.CharField(db_column='Отчество', max_length=30, blank=True, null=True)
    CardNumber = models.CharField(db_column='НомКарты', max_length=10, blank=True, null=True)
    ReceiptDate = models.DateTimeField(db_column='ДатаПоступления', blank=True, null=True)
    Department = models.CharField(db_column='Отделение', choices=Department_Choices, default='приемное', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ПациентыСтационара'

    def __str__(self):
        return self.LastName + " " + self.FirstName + " " + self.MiddleName# + " " + str(self.DateBirth)

    def get_absolute_url(self):
        return f'/{self.idPatient}/update'
        #return f'/'


class PatientRecordsModel(models.Model):
    IdRecord = models.IntegerField(db_column='IdRecord', primary_key=True, unique=True)
    idPatient = models.IntegerField(db_column='IdPacient', unique=True)
    TypeRecord = models.CharField(db_column='TypeRecord', max_length=50, blank=True, null=True)
    Department = models.CharField(db_column='Otdelenie', max_length=50, blank=True, null=True)
    ContentRec = models.TextField(db_column='ContentRec', blank=True, null=True)
    DateTime = models.DateTimeField(db_column='DateTime', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ElectrMedRecords'

    def __str__(self):
        return self.TypeRecord