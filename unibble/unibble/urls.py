from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('account/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('authentication/',include("authentication.urls")),
    path('user/',include("user.urls")),
    path('bubble/',include("bubble.urls")),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)