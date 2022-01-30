from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
import numpy as np

# Create your views here.
def index(request):
    rooms=Rooms.objects.all()
    context={
        'rooms': rooms,
    }

    return render(request,'index.html', context)

@csrf_exempt
def create(request):
    if request.method == 'POST':
        matrix = np.array([])
        matrix = handle_uploaded_file(request.FILES['file'])
        room = Rooms.objects.create(name=request.POST['name'], rows=len(matrix), columns=len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] == 1):
                    Walls.objects.create(row=i, column=j, room_id=room.id)
        showLightbulb(matrix, room)
        return HttpResponse("Se han realizado los cambios")

    else:
        raise Http404("Metodo no valido")

def show(request, id):
    room = Rooms.objects.get(pk=id)
    matrix = [[0 for x in range(room.columns)] for y in range(room.rows)]
    walls = Walls.objects.filter(room_id=id)
    lightBulbs = Lightbulbs.objects.filter(room_id=id)
    for i in walls:
        matrix[i.row][i.column] = 1
    
    for i in lightBulbs:
        matrix[i.row][i.column] = 3

    context={
        'room': room,
        'matrix': matrix
    }
    return render(request,'show.html', context)

def handle_uploaded_file(f):
    matrix = []
    for line in f:
        values = list(line.decode('ascii').replace(" ", "").rstrip('\r\n'))
        values = list(map(int, values))
        matrix.append(values)
    
    return np.asarray(matrix)

def showLightbulb(matrix, room):
    while 0 in matrix:
        x, y = getPosition(matrix)
        Lightbulbs.objects.create(row=x, column=y, room_id=room.id)
        matrix = updateLighted(matrix, x, y)
        matrix[x , y] = 3

def getPosition(matrix):
    max = -1
    x = 0
    y = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            lightBulbs = 0
            if matrix[row,col] == 0:
                lists = [matrix[row+1:,col], matrix[:row,col][::-1], matrix[row,col+1:], matrix[row,:col][::-1]]
                for i in lists:
                    for j in i:
                        if j != 0:
                            break
                        lightBulbs += 1
                if lightBulbs > max:
                    x, y = row,col
                    max = lightBulbs
    return x,y

def updateLighted(matrix, x, y):
    movement = -1
    while movement <= 1:
        row = x + movement
        while row>=0 and row<len(matrix):
            if(matrix[row][y] != 0):
                break
            matrix[row][y] = 2
            row += movement
        movement += 2
    movement = -1
    while movement <= 1:
        col = y + movement
        while col>=0 and col<len(matrix[x]):
            if(matrix[x][col] != 0):
                break
            matrix[x][col] = 2
            col += movement
        movement += 2
    return matrix