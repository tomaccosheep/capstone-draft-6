from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from .models import Game_Num
#from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from regexapp import node_lister, card_manager, regex_maker
from django.views.decorators.csrf import csrf_exempt
import json
import re

    
def index(request, game_id):
    gm = Game_Num.objects.get(unique_id=game_id)
    context_dict = {'well_being': gm.well_being,
                    'money': gm.money,
                    'popularity': gm.popularity,
                    'veg': gm.veg,
                    'pizza': gm.pizza,
                    'pizzar': gm.pizzar,
                    'shoe': gm.shoe,
                    'partner': gm.partner,
                    'veg_cost_money': gm.veg_cost_money,
                    'pizza_cost_money': gm.pizza_cost_money,
                    'pizzar_cost_money': gm.pizzar_cost_money,
                    'shoes_cost_money': gm.shoes_cost_money,
                    'partner_cost_money': gm.partner_cost_money,
                    'partner_cost_pop': gm.partner_cost_pop,
                    'cs_demand': gm.cs_demand,
                    }
    print(gm.money)
    return render(request, 'regexapp/index.html', context=context_dict)

def question_hw(request, game_id):
    gm = Game_Num.objects.get(unique_id=game_id)
    cm = card_manager.Card_Manager()
    cm.choose_node()
    out_homework = cm.request_homework()
    print(out_homework)
    gm.repeat_me = out_homework
    print(gm.repeat_me)
    data = {'homework': out_homework,}
    gm.save()
    return JsonResponse(data)

def question_check_hw(request, game_id):
    gm = Game_Num.objects.get(unique_id=game_id)
    if request.method == 'POST':
        str_request = request.body.decode('utf-8')
        json_data = json.loads(str_request)
        print(json_data['repeat_me'])
        print(gm.repeat_me)
        if json_data['repeat_me'] == gm.repeat_me:
            correct = True
        else:
            correct = False
    data = {'correct': correct,}
    return JsonResponse(data)

def question_test(request, game_id):
    gm = Game_Num.objects.get(unique_id=game_id)
    rx = regex_maker.Regexer()
    data1, data2, data3, data4 = rx.regex_question()
    print(str(data1) + '\n' + str(data2) + '\n' + str(data3) + '\n' + str(data4))
    gm.select_me = json.dumps(data2)
    gm.full_string = data4
    data = {'nonselect': data1, 'selectme': data2,}
    gm.save()
    return JsonResponse(data)

def question_check_test(request, game_id):
    gm = Game_Num.objects.get(unique_id=game_id)
    if request.method == 'POST':
        str_request = request.body.decode('utf-8')
        json_data = json.loads(str_request)
        if json.loads(gm.select_me) == re.findall(json_data['answer_guess'], gm.full_string):
            correct = True
        else:
            correct = False
    data = {'correct': correct}
    return JsonResponse(data)

def new_game(request):
    game = Game_Num()
    unique_id = game.unique_id
    game.save()
    return HttpResponseRedirect('/index/{}/'.format(unique_id))


@csrf_exempt
def save(request, game_id):
    gm = Game_Num.objects.get(unique_id=game_id)
    if request.method == 'POST':
        str_request = request.body.decode('utf-8')
        json_data = json.loads(str_request)
        gm.well_being = json_data['well_being']
        gm.money = json_data['money']
        gm.popularity = json_data['popularity']
        gm.veg = json_data['veg']
        gm.pizza = json_data['pizza']
        gm.pizzar = json_data['pizzar']
        gm.shoe = json_data['shoe']
        gm.partner = json_data['partner']
        gm.veg_cost_money = json_data['veg_cost_money']
        gm.pizza_cost_money = json_data['pizza_cost_money']
        gm.pizzar_cost_money = json_data['pizzar_cost_money']
        gm.shoes_cost_money = json_data['shoes_cost_money']
        gm.partner_cost_money = json_data['partner_cost_money']
        gm.partner_cost_pop = json_data['partner_cost_pop']
        gm.cs_demand = json_data['cs_demand']
        gm.save()
        print(gm.money)
    return JsonResponse({'views_money': gm.money })
