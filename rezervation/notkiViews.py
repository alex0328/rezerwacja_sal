elif request.method == "GET" and 'Data' in request.GET:
data = request.GET['Data']
combinerki = data + "-23-59"
date_n = datetime.datetime.strptime(combinerki, '%Y-%m-%d-%H-%M')
if date_n < today_date:
    return render(request, 'error3.html', locals())
elif request.method == "GET" and 'Pojemność' in request.GET:
    cap = Room.objects.all().order_by('capacity')
return render(request, 'abrak3.html', locals())


<section id="rooms" class="main">
        <h1 class="lista_title">Wyniki wyszukiwania</h1>
<h3>Szukana fraza:</h3>
    <p class="sala_data"> {{ nazwa }}</p>
        <div class="rooms_list">
            <ul>
                {% for sala in name %}
                    <li>
                        <h4>Nazwa sali:</h4>
                        <p class="sala_data">{{ sala.name }}</p>
                        <h4>Ta sala pomieści: </h4>
                        <p class="sala_data">{{ sala.capacity }} osób.</p>
                        {%  if sala.projector == True %}
                            <p class = "projector_true">Dostępny rzutnik</p>
                            {% else %}
                            <p class = "projector_false">Brak możliwości skorzystania z rzutnika</p>
                        {%  endif %}
                    <h4></h4>
                    {% if sala.id in lista_rezerwacji %}
                    <p class="projector_false">Ta sala na dziś jest zarezerwowana.</p>
                    {% else %}
                    <p class="projector_true">Sala dziś jest wolna</p>
                    {% endif %}
                        <a href="{% url 'modify' sala.id %}" >Edytuję dane sali</a>
                        <a href="{% url 'delete' sala.id %}" >Usuwam salę</a>
                        <a href="{% url 'see_more' sala.id %}">Rezerwacja</a>
                    </li>
                    {% endfor %}
            </ul>
        </div>
    <section>




form_date = SearchDate()
        form_capacity = SearchCapacity()
        form_projector = SearchProjector()

{ %
for sss in zmienna %}
< h2


class ="present_data" > Dane wybranej sali:<

    / h2 >
< h3 > Nazwa: < / h3 >
< p


class ="sala_data" > {{sss.name}} < / p >

< h3 > Pojemność
sali: < / h3 >
< p


class ="sala_data" > {{sss.capacity}} < / p >


{ % if sss.projector == True %}
< p


class = "projector_true" > Dostępny rzutnik < / p >


{ % else %}
< p


class = "projector_false" > Brak możliwości skorzystania z rzutnika < / p >


{ % endif %}
< p > {{res}} < / p >
{ % endfor %}