from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from core.login.views import LoginFormView

urlpatterns = [
    path('', LoginFormView.as_view(), name='index'),
    path('login/', include('core.login.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('core.dashboard.urls')),
    path('users/', include('core.user.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
