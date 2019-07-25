# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import BoardSerializer
from .models import BillBoard

# Create your views here.
class listboards(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = BillBoard.objects.all()

    def list(self, request):
        queryset = BillBoard.objects.all()
        serializer = BoardSerializer(queryset, many=True)
        return Response(serializer.data)