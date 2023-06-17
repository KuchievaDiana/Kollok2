from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from games.models import Game, Player


@csrf_exempt
def games(request, game_id=None):
    # Requires Game ID
    if request.method == 'GET':
        if game_id:
            try:
                return HttpResponse(Game.objects.get(id=game_id))
            except:
                return HttpResponse('Invalid Game ID', 400)
        return HttpResponse('Id argument is missing', 400)
    # Requires Player ID List
    elif request.method == 'POST':
        players_ids = request.POST.get('players').split(',')
        if not players_ids:
            return HttpResponse('players argument is missing', 400)
        result = {}
        try:
            for player in players_ids:
                Player.objects.get(id=player)
                result[player] = 0
        except:
            return HttpResponse('There was an attempt to add absent player', 400)
        game = Game(players=result)
        game.save()
        return HttpResponse(game)
    # Requires Game ID & New Game State
    # Optional: Player ID & Its Score Increment
    elif request.method == 'PUT':
        if not game_id:
            return HttpResponse('Id argument is missing', 400)
        put_query = QueryDict(request.body)
        game_state = put_query.get('state')
        if not game_state:
            return HttpResponse('state argument is missing', 400)
        player_id = put_query.get('player_id')
        score = put_query.get('score')
        try:
            game = Game.objects.get(id=game_id)
            game.state = game_state
            if player_id:
                try:
                    Player.objects.get(id=player_id)
                except:
                    return HttpResponse('There was an attempt to edit an absent player', 400)
                if score:
                    game.players[player_id] += int(score)
                else:
                    return HttpResponse('score argument is missing', 400)
            game.save()
            return HttpResponse(game)
        except:
            return HttpResponse('Invalid Game ID', 400)
    return HttpResponse('Unknown Request', 405)


@csrf_exempt
def players(request, player_id=None):
    # Requires Player ID
    if request.method == 'GET':
        if player_id:
            try :
                player_games = Game.objects.filter(players__has_key=player_id)
                player = Player.objects.get(id=player_id)
                return HttpResponse(f'{Player.objects.get(id=player_id)} <br> {str(list(player_games)).replace("<", "").replace(">", "")}')
            except:
                return HttpResponse('Invalid player ID', 400)
        else:
            return HttpResponse('Id argument is missing', 400)
    elif request.method == 'POST':
        player = Player()
        player.save()
        return HttpResponse(player)
    return HttpResponse('Unknown Request', 404)