from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views  import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('invite/', include('invitations.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('app/', include('app.urls')),
]


# es aris profile_pic-is default mnishvnelobistvis.amas jerjerobit marto django formebit gavtestav
# client-sidedanac sheidzleba, magram rac ar ici imas nu gaaketeb jer mainc ani (es ro gamaxsendes)
# testing : template+forms

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# admin.site.site_header = 'Time Management'
# admin.site.index_title = 'Service'   admin panelis cvlilebebi