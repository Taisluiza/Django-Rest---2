from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from escola.throttles import MatriculaAnonRateThrottle


class EstudanteViewSet(viewsets.ModelViewSet):

    queryset = Estudante.objects.all().order_by("id")
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer

    
class MatriculaViewSet(viewsets.ModelViewSet):
    
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]




# PARA SELECIONAR APENAS UMA MATRICA DE UM ESTUDANTE
class ListaMatriculaEstudante(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")
          # FILTRA PARA PEGAR APENAS 1, PELA CHAVE PRIMARIA
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer


class ListaMatriculaCurso(generics.ListAPIView):
   
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListaMatriculasCursoSerializer