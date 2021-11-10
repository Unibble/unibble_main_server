from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/',include("authentication.urls")),
    path('user/',include("user.urls")),
    path('bubble/',include("bubble.urls")),
]
# django all-auth
urlpatterns += path('account/', include('allauth.urls')),