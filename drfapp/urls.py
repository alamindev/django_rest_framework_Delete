from django.contrib import admin
from django.urls import path, include
from drfapp.views import *
from.import views


 


urlpatterns = [
    path('api/', include(('drfapp.api.urls', 'drfapp'), namespace='drfapp_url')),
    path('Article/', views.get_article, name="article"),
     
    # path('api/<int:id>/', include(router.urls))
]