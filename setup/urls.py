from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante, ListaMatriculaCurso


router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas',MatriculaViewSet,basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/',ListaMatriculaEstudante.as_view()), # MOSTRA QUE É UMA URLS DE VISUALIZAÇÃO
    path('cursos/<int:pk>/matriculas/',ListaMatriculaCurso.as_view()),
]