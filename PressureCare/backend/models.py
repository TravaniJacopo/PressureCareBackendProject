from django.db import models

# Create your models here.

class UtenteApplicativo(models.Model):
    id_utente = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    ruolo = models.CharField(max_length=50, null=False)
    attivo = models.BooleanField(default=True)
    mail = models.EmailField(blank=True, null=True)     # Opzionale
    telefono = models.CharField(max_length=20, blank=True, null=True) # Opzionale


class Medico(models.Model):
    id_medico = models.OneToOneField(
        UtenteApplicativo, 
        on_delete=models.CASCADE, 
        primary_key=True, 
        db_column='id_medico'
    )
    nome = models.CharField(max_length=100, null=False)
    cognome = models.CharField(max_length=100, null=False)


class Paziente(models.Model):
    id_paziente = models.OneToOneField(
        UtenteApplicativo, 
        on_delete=models.CASCADE, 
        primary_key=True, 
        db_column='id_paziente'
    )
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True, db_column='id_medico') # Può essere null se non ha ancora un medico assegnato
    nome = models.CharField(max_length=100, null=False)
    cognome = models.CharField(max_length=100, null=False)
    sesso = models.CharField(max_length=10, null=False)
    cf = models.CharField(max_length=16, unique=True, null=False)
    data_nascita = models.DateField(null=False)
    consensi = models.BooleanField(default=False)


class ParametroVitale(models.Model):
    id_parametrovitale = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)


class Soglia(models.Model):
    id_soglia = models.AutoField(primary_key=True)
    parametro_vitale = models.ForeignKey(ParametroVitale, on_delete=models.CASCADE, null=False, db_column='id_parametrovitale')
    paziente = models.ForeignKey(Paziente, on_delete=models.CASCADE, null=True, blank=True, db_column='id_paziente') # Null se è una soglia generale di sistema
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True, blank=True, db_column='id_medico')     # Null se è una soglia di default non impostata da un medico specifico
    valore_min = models.FloatField(null=False)
    valore_max = models.FloatField(null=False)


class Misurazione(models.Model):
    id_misurazione = models.AutoField(primary_key=True)
    paziente = models.ForeignKey(Paziente, on_delete=models.CASCADE, null=False, db_column='id_paziente')
    timestamp = models.DateTimeField(null=False)


class MisurazioneParametroVitale(models.Model):
    id_misuraz_param_vitale = models.AutoField(primary_key=True)
    misurazione = models.ForeignKey(Misurazione, on_delete=models.CASCADE, null=False, db_column='id_misurazione')
    parametro_vitale = models.ForeignKey(ParametroVitale, on_delete=models.CASCADE, null=False, db_column='id_parametrovitale')
    valore = models.FloatField(null=False)


class Alert(models.Model):
    id_alert = models.AutoField(primary_key=True)
    soglia = models.ForeignKey(Soglia, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_soglia') # Può essere null se la soglia originaria viene eliminata ma vogliamo tenere lo storico dell'alert
    misurazione_param_vitale = models.ForeignKey(MisurazioneParametroVitale, on_delete=models.CASCADE, null=False, db_column='id_misuraz_param_vitale')
    tipo = models.CharField(max_length=100, null=False)
    severita = models.CharField(max_length=50, null=False)
    stato = models.CharField(max_length=50, null=False)
    motivazione = models.TextField(blank=True, null=True) # Spesso vuota, compilata magari dopo dal medico che "chiude" l'alert


class Report(models.Model):
    id_report = models.AutoField(primary_key=True)
    paziente = models.ForeignKey(Paziente, on_delete=models.CASCADE, null=False, db_column='id_paziente')
    data_creazione = models.DateTimeField(auto_now_add=True, null=False)
    periodo_dal = models.DateField(null=False)
    periodo_al = models.DateField(null=False)
    pdf = models.FileField(upload_to='reports_pdf/', null=False)


class NotaClinica(models.Model):
    id_nota = models.AutoField(primary_key=True)
    paziente = models.ForeignKey(Paziente, on_delete=models.CASCADE, null=False, db_column='id_paziente')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=False, db_column='id_medico')
    testo = models.TextField(null=False)
    data_creazione = models.DateTimeField(auto_now_add=True, null=False)
    data_modifica = models.DateTimeField(auto_now=True, null=False)