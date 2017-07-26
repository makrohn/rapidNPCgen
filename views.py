from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rpcg_web import character
import json
import collections

def create_npc(request):
    classname = request.POST['Class']
    race = request.POST['Race']
    level = int(request.POST['Level'])
    name = request.POST['Name']
    if 'Subrace' in request.POST:
        subrace = request.POST['Subrace']
        new_npc = character.NPC(name, classname, race, level, subrace)
    else:
        new_npc = character.NPC(name, classname, race, level)
    npc_sheet = new_npc.sheet
    template = loader.get_template('create_npc.html')
    npc_sheet["spell_level_counter"] = 1
    return HttpResponse(template.render(npc_sheet, request))
    # return HttpResponse(npc_json)

def index(request):
    subrace_list = {}
    for race in character.races.RACE_LIST:
        race_def = character.races.load_race_file(race)
        if "Subraces" in race_def:
            subrace_list[race] = race_def["Subraces"]
    context = {
        "Races": character.races.RACE_LIST,
        "Classes": character.classes.CLASS_LIST,
        "Subrace_List": subrace_list,
        }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))
