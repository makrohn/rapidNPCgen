from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rpcg_web import character
import json
import collections

def index(request):
    return HttpResponse("Hello World")

def create_npc(request):
    new_npc = character.NPC("Arik", "Bard", "Dwarf", 4, "Hill")
    npc_sheet = new_npc.sheet
    template = loader.get_template('create_npc.html')
    return HttpResponse(template.render(npc_sheet, request))
    # return HttpResponse(npc_json)