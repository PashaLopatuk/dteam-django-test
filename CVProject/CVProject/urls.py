
"""
URL configuration for CVProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from api.cv.views import CVListCreateView, CVDetailView
from django.contrib import admin
from django.urls import path

from main.views import CVListView, CVInfoView, CVInfoPdfView, RequestLogListView, SendPdfToEmailView, SettingsPageView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("settings/", SettingsPageView.as_view(), name="settings_page"),
    
    path("", CVListView.as_view(), name="cv_list"),
    path("cv/<int:cv_id>", CVInfoView.as_view(), name="cv_info"),
    path("cv/<int:cv_id>/pdf", CVInfoPdfView.as_view(), name="cv_info/pdf"),
    path("cv_send_pdf_email", SendPdfToEmailView.as_view(), name="cv_info/send_to_email"),
    
    path("logs/", RequestLogListView.as_view(), name="logs_list"),
    
    path("api/cv", CVListCreateView.as_view(), name="api/cv_list"),
    path("api/cv/<int:pk>", CVDetailView.as_view(), name="api/cv_detail"),
]
