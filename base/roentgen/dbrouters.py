from .models import PatientRecordsModel, PatientModel


class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        if model == PatientRecordsModel:
            return 'PatientRecords'
        return None

    def db_for_write(self, model, **hints):
        if model == PatientRecordsModel:
            return 'PatientRecords'
        return None