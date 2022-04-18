from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings, urls

from django.contrib.auth import views as auth_views
from Authentication import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('auth/', include('Authentication.urls')),
    path('profile/', include('Profile.urls')),
    path('complaints/', include('Complaint.urls')),
    path('api/', include('API.urls')),

    path('password_reset/', v.passwordReset, name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),
         name="password_reset_complete"),
]

# if settings.DEBUG:
#     urlpatterns += [
#         urls.url(r'^media/(?P<path>.*)$',
#                  serve, {'document_root': settings.MEDIA_ROOT, }),
#     ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
