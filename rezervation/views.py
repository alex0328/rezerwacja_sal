from django.shortcuts import render
from django.http import HttpResponse
from rezervation.models import Room, Reservation
from rezervation.forms import Add_form,Delete_form, DateRangeForm, SearchName, SearchDate, SearchCapacity, SearchProjector
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import datetime
from datetime import date

# Create your views here.
@csrf_exempt
def home(reqest):
    today_date = datetime.datetime.today()
    rooms = Room.objects.all().order_by('id')
    reserv = Reservation.objects.filter(date=today_date)
    lista_rezerwacji = []
    for sss in reserv:
        lista_rezerwacji.append(sss.room_id)
    return render(reqest,'lista_sal.html',locals())

@csrf_exempt
def add_room(request):
    if request.method == "GET":
        form = Add_form()
        return render(request, 'dodawanie_sal.html', locals())
    if request.method == "POST":
        n = request.POST['nazwa']
        y = request.POST['pojemnosc_sali']
        try:
            int(y)
            a = False
            if 'rzutnik' in request.POST:
                a = True
            try:
                s = Room.objects.create(name=n, capacity=y, projector=a)
                return render(request, 'dodano.html', locals())
            except IntegrityError:
                error = n
                return render(request, 'error.html', locals())
        except ValueError:
            return render(request, 'error.html', locals())



@csrf_exempt
def modify(request, room):
    rooms = Room.objects.all()
    if request.method == "GET":
        form = Add_form()
        roomid = room
        dane_sali = Room.objects.filter(id=room)
        return render(request, 'modify.html', locals())
    if request.method == "POST":
        n = request.POST['nazwa']
        y = request.POST['pojemnosc_sali']
        a = False
        if 'rzutnik' in request.POST:
            a = True
        w = Room.objects.get(id = room)
        w.name = n
        w.capacity = y
        w.projector = a
        w.save()
        return render(request, 'zmodyfikowano.html', locals())

@csrf_exempt
def delete(request, room):
    del_form = Delete_form()
    if request.method == "GET":
        dane_sali = Room.objects.filter(id=room)
        return render(request, 'delete.html', locals())
    if request.method == "POST":
        if 'Usuwam' in request.POST:
            w = Room.objects.get(id=room)
            w.delete()
            return render(request, 'usunieto.html', locals())
        else:
            return render(request, 'niezdecydowany.html', locals())

@csrf_exempt
def see_more(request, room):
    today_date = datetime.datetime.today()
    today_2 = datetime.date.today()
    if request.method == "GET":
        reserv_dates = Reservation.objects.filter(room = room).order_by('date')
        dates_list = []
        list_empty = False
        for aaa in reserv_dates:
            if aaa.date >= today_2:
                dates_list.append(aaa.date)
        if dates_list == []:
            list_empty = True
        room_nr = room
        rooma_id = Room.objects.filter(id = room)
        reservations = Reservation.objects.filter(date=today_date, room=room)
        if reservations:
            res = "Zarezerwowana na dziś. Nie możesz już dokonać rezerwacji na dzisiejszy dzień"
        else:
            res = "Wolna na dziś"
        Res_form = DateRangeForm()
        return render(request, 'details.html', locals())
    if request.method == "POST":
        reservations = Reservation.objects.filter(date=today_date, room=room)
        w = Room.objects.get(id=room)
        n = request.POST['Rezerwuje']
        y = request.POST['Uwagi']
        u = room
        try:
            r = Reservation.objects.filter(date=n, room_id=room)
        except:
            return render(request, 'error2.html', locals())
        innn = False
        for www in r:
            innn = True
        combinerki = n+"-23-59"
        date_n = datetime.datetime.strptime(combinerki, '%Y-%m-%d-%H-%M')
        if innn == False:
            if today_date <= date_n:
                t1 = Reservation.objects.create(date=n, room_id=u, comment=y)
                t1.save()
                return render(request, 'zarezerwowano.html', locals())
            return render(request, 'brak_rezerwacji.html', locals())
        else:
            return render(request, 'istnieje.html', locals())
    else:
        return render(request, 'refresh.html', locals())

@csrf_exempt
def szukaj(request):
    today_date = datetime.datetime.today()
    if request.method == "GET" and 'Nazwa' in request.GET:
        nazwa = request.GET['Nazwa']
        if nazwa is not None and nazwa != '':
            found_query_set_name = Room.objects.filter(name=nazwa)
            if found_query_set_name != None:
                zmienna = found_query_set_name
                return render(request, 'found.html', locals())
        elif request.method == "GET" and 'Data' in request.GET:
            data = request.GET['Data']
            if data is not None and nazwa != '':
                try:
                    combinerki = data + "-23-59"
                    date_n = datetime.datetime.strptime(combinerki, '%Y-%m-%d-%H-%M')
                except:
                    return render(request, 'error3.html', locals())
                if date_n < today_date:
                    return render(request, 'error3.html', locals())
                else:
                    name2 = Room.objects.all().order_by('name')
                    data = Reservation.objects.filter(date=data)
                    lista_rezerwacji_na_dzien = []
                    for asd in data:
                        lista_rezerwacji_na_dzien.append(asd.room_id)
                    return render(request, 'abrak2.html', locals())
            elif request.method == "GET" and 'cap' in request.GET:
                pojemn = request.GET["cap"]
                pojemnosc = int(pojemn)
                cap = Room.objects.all().order_by('capacity')
                return render(request, 'abrak3.html', locals())
    else:
        form_name = SearchName()
        form_date = SearchDate()
        cap = SearchCapacity()
        return render(request, 'szukaj.html', locals())









