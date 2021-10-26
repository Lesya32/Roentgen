from django.urls import path
from . import views


urlpatterns = [
    path('', views.PatientView.as_view(), name='PatientView'),
    path('<pk>/history', views.Records, name='RecordsView'),
    path('<pk>/ChoiceRecord', views.ChoiceRecord, name='СhoiceRecord'),
    path('search/', views.Search, name='Search'),
]
