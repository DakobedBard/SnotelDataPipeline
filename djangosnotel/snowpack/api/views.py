from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.http import HttpResponse
from django.db.models import Q

from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
User = get_user_model()
from aws.s3Client import s3Client

