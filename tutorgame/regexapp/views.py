from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from .models import Game_Num
#from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from regexapp import node_lister
from django.views.decorators.csrf import csrf_exempt
import json

    
def index(request, game_id):
    gm = Game_Num.objects.get(unique_id=game_id)
    context_dict = {'money': gm.money}
    print(gm.money)
    return render(request, 'regexapp/index.html', context=context_dict)

def question_hw(request, game_id):
    return JsonResponse(data)
# Create your views here.

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

'''
def check_homework(request):
            addr.name = request.POST.get('name', None)

'''  
