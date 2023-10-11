from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from . import views

@api_view(['GET'])
def getRoutes(request):
    routes = [
          'auth/',
          'admin/',
          'api-auth/',
          'article/'
    ]
    return Response(routes)




urlpatterns = [
    
    path('', getRoutes),
    path('auth/', views.MyTokenObtainPairView.as_view()),
    path('article/', views.LatestArticleAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


