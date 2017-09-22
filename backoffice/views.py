# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render


def home(request):

    """ Exemple de page HTML, non valide pour que l'exemple soit concis """

    text = """<h1>WOLOLOLOLOLO !!</h1>"""

    return HttpResponse(text)
