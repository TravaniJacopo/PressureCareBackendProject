from rest_framework import serializers
from .models import (
    UtenteApplicativo, Medico, Paziente, ParametroVitale,
    Soglia, Misurazione, MisurazioneParametroVitale,
    Alert, Report, NotaClinica
)

class UtenteApplicativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtenteApplicativo
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class PazienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paziente
        fields = '__all__'
        # Il medico viene assegnato automaticamente dal backend, il frontend non deve inviarlo
        read_only_fields = ['id_medico'] 

    def validate(self, data):
        # Se la richiesta è di creazione (POST) e i consensi sono False, blocca tutto.
        request = self.context.get('request')
        if request and request.method == 'POST':
            if not data.get('consensi'):
                raise serializers.ValidationError(
                    {"consensi": "L'accettazione dei consensi privacy è obbligatoria per registrare il paziente."}
                )
        return data

class ParametroVitaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametroVitale
        fields = '__all__'

class SogliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soglia
        fields = '__all__'
        read_only_fields = ['id_medico'] # Inserito automaticamente dal backend come autore della modifica

class MisurazioneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Misurazione
        fields = '__all__'
        read_only_fields = ['id_paziente'] # Assegnato dal backend in base all'utente loggato

class MisurazioneParametroVitaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MisurazioneParametroVitale
        fields = '__all__'

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'
        # Molti campi dell'alert sono generati dal sistema, l'utente può modificare solo lo stato e la motivazione (RF5.5)
        read_only_fields = ['id_soglia', 'id_misuraz_param_vitale', 'tipo', 'severita']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ['data_creazione']

class NotaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaClinica
        fields = '__all__'
        read_only_fields = ['id_medico', 'data_creazione', 'data_modifica']