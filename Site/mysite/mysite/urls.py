from django.contrib import admin
from django.urls import include, path


from polls import views #NEEEWWWW

urlpatterns = [
    path('', views.home, name='home'),  # NEEEWWWW
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]