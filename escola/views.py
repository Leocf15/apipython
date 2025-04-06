from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Aluno
from .serializers import AlunoSerializer

class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome', 'email']           # Permite buscar por nome ou email
    ordering_fields = ['nome', 'data_nascimento'] # Permite ordenar por nome ou data de nascimento

class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [IsAuthenticated]
