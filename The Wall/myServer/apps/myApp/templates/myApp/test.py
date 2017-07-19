"josh_baseball_players": League.objects.filter(name__contains="Atlantic Federation").Player.objects.filter(first_name__contains="Joshua"),


Team.objects.filter(player__first_name='Joshua')
