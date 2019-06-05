from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import DetailView


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.all()


class TodoApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'templates/home.html'

    def get(self, request):
        queryset = Todo.objects.all().order_by('-id')
        return Response({'profiles': queryset, 'user_name':request.user})





