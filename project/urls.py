from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]


# es aris profile_pic-is default mnishvnelobistvis.amas jerjerobit marto django formebit gavtestav
# client-sidedanac sheidzleba, magram rac ar ici imas nu gaaketeb jer mainc ani (es ro gamaxsendes)
# testing : template+forms

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# admin.site.site_header = 'Time Management'
# admin.site.index_title = 'Service'   admin panelis cvlilebebi