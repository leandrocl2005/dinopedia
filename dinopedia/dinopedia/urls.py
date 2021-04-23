from dinosaurs.views import HomeDinosaurs, ListDinosaurs
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/dinosaurs/', ListDinosaurs.as_view()),
    path('', HomeDinosaurs.as_view())
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
