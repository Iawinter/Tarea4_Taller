from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import requests
import json
import base64
from . models import Mensajes
from . serializers import MensajesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#import pandas as pd
from collections import defaultdict
#import gspread
#from gspread_dataframe import set_with_dataframe
from datetime import date

lista = []

@api_view(['POST', 'GET'])
def suscripcion(request):
    url = 'https://tarea4taller.herokuapp.com/'
    body = {"url": url}
    body = json.dumps(body)
    r = requests.post(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-4-notifications/subscriptions/26425', headers={"Content-type": "application/json"}, data = body)
    r = r.json()
    return Response(r, status=status.HTTP_200_OK)

@api_view(['DELETE', 'GET'])
def eliminar_sus(request):
    r = requests.delete(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-4-notifications/subscriptions/26425')
    return Response(r, status=status.HTTP_200_OK)


def index(request):
    return render(request, 'index.html')


class MensajesList(APIView):

    def get(self, request):
        mensajes = Mensajes.objects.all()
        serializer = MensajesSerializer(mensajes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        info = request.data
        lista.append(info['message']['data'])
        print(lista)
        yo = 'https://tarea4taller.herokuapp.com/'
        nuevo_mensaje = Mensajes.objects.create(id=info['message']['data'])
        nuevo_mensaje.self = yo
        nuevo_mensaje.save()
        serializer = MensajesSerializer(nuevo_mensaje)
        return Response(serializer.data, status=status.HTTP_200_OK)



#Create your views here.
#df = pd.DataFrame(data=lista).T

#gc = gspread.service_account(filename='taller-proyecto-331020-6c7b557c5aa0.json')
#sh = gc.open_by_key('6c7b557c5aa0742aa2eb6eb22a90431192dc9740')
#worksheet = sh.get_worksheet(0) #-> 0 - first sheet, 1 - second sheet etc.

# APPEND DATA TO SHEET
#set_with_dataframe(worksheet, df) #-> THIS EXPORTS YOUR DATAFRAME TO THE GOOGLE SHEET