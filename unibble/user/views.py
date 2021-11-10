from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from .models import Unibber,User
from rest_framework.authtoken.models import Token

