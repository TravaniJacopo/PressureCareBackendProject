from django.urls import path
from . import views

urlpatterns = [
    # Utenti e Medici
    path('utenti/', views.utente_list),
    path('medici/', views.medico_list),

    # Pazienti
    path('pazienti/', views.paziente_list),
    path('pazienti/<int:pk>/', views.paziente_detail),

    # Misurazioni
    path('misurazioni/', views.misurazione_list),

    # Soglie
    path('soglie/', views.soglia_list),

    # Alert
    path('alerts/', views.alert_list),

    # Note Cliniche
    path('note-cliniche/', views.nota_list),

    # Report
    path('reports/', views.report_list),
]