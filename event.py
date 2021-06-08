from  pgzero.builtins import Actor,Rect


class Event:
    def __init__(self):
        print("utworzono event")
        self.name='czas1'


        self.events=[] #do tej listy dodajemy początkowe obiekty
        #daję tu póki co dwa dowolne, będę potrzebował później współrzędnych

        newevent=Actor(self.name,(200,400))
        newevent.hidden=False #początkowo obiekty nie są ukryte
        self.events.append(newevent)

        newevent = Actor(self.name, (400, 600))
        newevent.hidden=False
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
        print(x,y)
        rect = Rect(x-35/2,y-35/2,35,35) #prostokąt w którym znajduje się gracz
        for event in self.events_to_draw(): #czy gracz ma kolizję z jakimś nieukrytym eventem
            if event.colliderect(rect):
                event.hidden=True











