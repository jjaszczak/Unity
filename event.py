from  pgzero.builtins import Actor,Rect


class Event:
    def __init__(self):
        #na razie trzy ikonki i trzy typy
        self.time_name='czas'
        self.life_name='serce'
        self.unknown_name='unknown'


        self.events=[] #do tej listy dodajemy początkowe obiekty

        newevent=Actor(self.time_name,(414,540))
        newevent.hidden=False #początkowo obiekty nie są ukryte
        newevent.type=1
        self.events.append(newevent)

        newevent = Actor(self.life_name, (683, 466))
        newevent.hidden=False
        newevent.type=2
        self.events.append(newevent)

        newevent = Actor(self.unknown_name, (298, 64))
        newevent.hidden = False
        newevent.type=3
        self.events.append(newevent)

    def events_to_draw(self): #zwraca listę z obiektami, które nie zostały jeszcze zebrane
        left_events=[]
        for event in self.events:
            if not event.hidden: #jeśli nie jest ukryty, dodajemy
                left_events.append(event)
        return left_events

    def draw(self):
        for event in self.events_to_draw(): #rysuje tylko te, które nie zostały jeszcze zebrane
            event.draw()

    def kolizja(self,gracz): #sprawdzanie kolizji
        x,y=gracz.x,gracz.y
        #print(x,y)
        rect = Rect(x-35/2,y-35/2,35,35) #prostokąt w którym znajduje się gracz
        for event in self.events_to_draw(): #czy gracz ma kolizję z jakimś nieukrytym eventem
            if event.colliderect(rect):
                event.hidden = True  #ukrywamy obiekt i sprawdzamy, jakiego był typu
                if event.type==1:
                    return "time"
                if event.type==2:
                    return "life"
                if event.type==3:
                    return "unknown"
        return "None"











