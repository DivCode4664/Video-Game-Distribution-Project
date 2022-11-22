from django.shortcuts import render
from gamingdistribution.models import Game
from gamingdistribution.models import Publisher
from django.contrib import messages
from django.http import HttpResponse
from gamingdistribution.forms import GameForms,PublisherForms
from django.db import connection

def homepage(request):
    return render(request,'homepage.html')

def showGame(request):
    showall = Game.objects.all()
    return render(request,'showGame.html',{"data":showall})

def showPublisher(request):
    showall = Publisher.objects.all()
    return render(request,'showPublisher.html',{"data":showall})

def InsertPublisher(request):
    if request.method == 'POST':
        if request.POST.get('pub_id') and request.POST.get('pub_name'):
            saverecord = Publisher()
            saverecord.pub_id = request.POST.get('pub_id')
            saverecord.pub_name = request.POST.get('pub_name')

            allval = Publisher.objects.all()

            for i in allval:
                if int(i.pub_id)==int(request.POST.get('pub_id')):
                    messages.warning(request,'Publisher already exists with this ID...!');
                    return render(request,'InsertPublisher.html')

            saverecord.save()
            messages.success(request, 'Publisher ' + saverecord.pub_name + ' Is Saved Successfully')
            return render(request ,'InsertPublisher.html')
    else:
        return render(request, 'InsertPublisher.html')

def InsertGame(request):
    if request.method == 'POST':
        request.POST.get('game_id') and request.POST.get('pub_id') and request.POST.get('game_name') and request.POST.get('genre') and request.POST.get('release_date') and request.POST.get('last_update') and request.POST.get('total_players') and request.POST.get('windows') and request.POST.get('macos') and request.POST.get('linux')
        saverecord = Game()
        saverecord.game_id = request.POST.get('game_id')
        saverecord.pub_id = request.POST.get('pub_id')
        saverecord.game_name = request.POST.get('game_name')
        saverecord.genre = request.POST.get('genre')
        saverecord.release_date = request.POST.get('release_date')
        saverecord.last_update = request.POST.get('last_update')
        saverecord.total_players = request.POST.get('total_players')
        saverecord.windows = request.POST.get('windows')
        saverecord.macos = request.POST.get('macos')
        saverecord.linux = request.POST.get('linux')

        allval = Game.objects.all()
        for i in allval:
                if int(i.game_id)==int(request.POST.get('game_id')):
                    messages.warning(request,'Game already exists with this ID....!');
                    return render(request,'InsertGame.html')
        
        allvl = Publisher.objects.all()
        x = False
        for i in allvl:
                if int(i.pub_id)==int(request.POST.get('pub_id')):
                    x = True
                    break
        
        if x == False:
            messages.warning(request,'Publisher with Publisher ID ' + saverecord.pub_id + ' does not exits...');
            return render(request,'InsertGame.html')

        saverecord.save()
        messages.success(request, 'Game ' + saverecord.game_name + ' Is Saved Successfully')
        return render(request ,'InsertGame.html')
        
    else:
        return render(request, 'InsertGame.html')

def EditGame(request,id):
    editGameObj=Game.objects.get(game_id=id)
    context={
        "Game":editGameObj
    }
    return render(request,'EditGame.html',context)

def updateGame(request,id):
    game_id=id
    pub_id=request.POST.get('pub_id')
    game_name=request.POST.get('game_name')
    genre=request.POST.get('genre')
    release_date=request.POST.get('release_date')
    last_update=request.POST.get('last_update')
    total_players=request.POST.get('total_players')
    windows=request.POST.get('windows')
    macos=request.POST.get('macOS')
    linux=request.POST.get('linux')
    NewGame = Game(game_id = game_id, pub_id = pub_id, game_name = game_name,genre = genre, release_date = release_date, last_update = last_update, total_players =total_players, windows = windows, macos = macos, linux = linux)
    game=Game.objects.get(game_id=id)
    game=NewGame
    game.save()
    context={
        "Game":game
    }
    messages.success(request, 'Game ' + game_name + ' Is Updated Successfully')
    return render(request,'EditGame.html',context)

def DelGame(request,id):
    delGameObj=Game.objects.get(game_id=id)
    context={
        "Game":delGameObj
    }
    return render(request,'DelGame.html',context)

def deletedGame(request,id):
    delGameObj=Game.objects.get(game_id=id)
    delGameObj.delete()
    showall=Game.objects.all()
    messages.success(request,'Game deleted succesfully!!')
    return render(request,'DelGame.html',{"Game": delGameObj})

def DelPublisher(request,id):
    delPubObj=Publisher.objects.get(pub_id=id)
    context={
        "Publisher":delPubObj
    }
    return render(request,'DelPublisher.html',context)

def deletedPublisher(request,id):
    delPubObj=Publisher.objects.get(pub_id=id)
    delPubObj.delete()
    showall=Publisher.objects.all()
    messages.success(request,'Record deleted succesfully!!')
    return render(request,'DelPublisher.html',{"Publisher": delPubObj})

def updatePublisher(request,id):
    pub_id = id
    pub_name=request.POST.get('pub_name')
    NewPublisher = Publisher(pub_id = pub_id,pub_name = pub_name)
    publisher=Publisher.objects.get(pub_id=id)
    publisher=NewPublisher
    publisher.save()
    context={
        "Publisher":publisher
    }
    messages.success(request, 'Publisher ' + pub_name + ' Is Saved Successfully')
    return render(request,'EditPublisher.html',context)

def EditPublisher(request,id):
    editPublisherObj=Publisher.objects.get(pub_id=id)
    context={
        "Publisher":editPublisherObj
    }
    return render(request,'EditPublisher.html',context)

def SortGame(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=Game.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'SortGame.html',context)
    else:
        return render(request,'SortGame.html')

def SortPublisher(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=Publisher.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'SortPublisher.html',context)
    else:
        return render(request,'SortPublisher.html')

def QueryforGame(request):
    query = "select * from \"Game\" where \"Game\".\"total_players\" > (select avg(\"Game\".\"total_players\") from \"Game\");"

    cursor = connection.cursor()
    cursor.execute(query)
    alldata=cursor.fetchall()

    return render(request,'QueryforGame.html',{'data':alldata})

def QueryforPublisher(request):
    query = "select \"Game\".\"game_id\",\"Game\".\"game_name\",\"Game\".\"genre\",\"Game\".\"release_date\",\"Game\".\"last_update\",\"Game\".\"total_players\",\"Game\".\"windows\",\"Game\".\"macOS\",\"Game\".\"Linux\" from \"Game\" JOIN \"Publisher\" on \"Publisher\".\"pub_id\" = \"Game\".\"pub_id\" where \"Publisher\".\"pub_name\" = 'Valve';"

    cursor = connection.cursor()
    cursor.execute(query)
    alldata=cursor.fetchall()

    return render(request,'QueryforPublisher.html',{'data':alldata})

def style(request):
    return render(request,'homepage.html')