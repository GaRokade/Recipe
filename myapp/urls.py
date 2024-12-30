"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home.views import*
from vege.views import*
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    
    path('delete-receipe/<id>/',delete_receipe,name="delete-receipe"),
    path('update-receipe/<id>/',update_receipe,name="update-receipe"),
    path('',receipes,name='receipes'),
     path('contact/',contact,name='contact'),
      path('about/',about,name='about'),
       path('base/',base,name='base'),
        path('Login/',Login,name='Login'),
        path('student-page/',student_page,name='student_page'),
        path('Logout/',logout_page,name='Logout'),
         path('Register/',register,name='Register'),
         path('seemarks/<student_id>/',see_marks,name='seemarks'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
    urlpatterns+=staticfiles_urlpatterns()