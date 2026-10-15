from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Rotta per accedere al pannello di amministrazione di Django
    path('admin/', admin.site.urls),

    # Reindirizza tutte le chiamate che iniziano con /api/ al file backend/urls.py
    path('api/', include('backend.urls')),
]

# Permette di visualizzare/scaricare i file multimediali (es. i PDF dei report) in ambiente di sviluppo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)