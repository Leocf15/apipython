from django.contrib import admin
from django.urls import path
from escola.views import AlunoList, AlunoDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alunos/', AlunoList.as_view(), name='aluno-list'),
    path('api/alunos/<int:pk>/', AlunoDetail.as_view(), name='aluno-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
