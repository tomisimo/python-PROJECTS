#print ("IRD BE A KERESETT NEVET") # message to type in the name
from tkinter import*
def januariFOnevnapok():
    januarnevek ={'Alpar':'Januar 1,Marcius 27,Junius 14,Szeptember 5',
                 'Fruzsina':'Januar 1,Szeptember 25',
                 'Bazil':'Januar 1',
                 'Abel':'Januar 2','Gergely':'Januar 2','Vazul':'Januar 2',
                 'Benjamin':'Januar 3','Genoveva':'Januar 3','Gyongyver':'Januar 3,Januar 8','Dzsenifer':'Januar 3',
                 'Leona':'Januar 4','Titusz':'Januar 4','Angela':'Januar 4,Januar 27',
                 'Simon':'Januar 5','Emilia':'Januar 5',
                 'Boldizsar':'Januar 6','Menyhert':'Januar 6','Gaspar':'Januar 6',
                 'Attila':'Januar 7','Ramona':'Januar 7','Etele':'Januar 7','Rajmund':'Januar 7','Balint':'Januar 7',
                 'Keve':'Januar 8','Szeverin':'Januar 8','Szoreny':'Januar 8',
                 'Marcell':'Januar 9,Januar 16','Julianusz':'Januar 9',
                 'Melania':'Januar 10','Vilmos':'Januar 10','Vilma':'Januar 10',
                 'Agota':'Januar 11,Februar 5','Honorata':'Januar 11',
                 'Erno':'Januar 12','Erneszta':'Januar 12','Tatjana':'Januar 12',
                 'Veronika':'Januar 12,Januar 13,Januar 19,Januar 24,Februar 4,Julius 9','Csongor':'Januar 13','Yvett':'Januar 13',
                 'Bodog':'Januar 14','Felix':'Januar 14',
                 'Lorand':'Januar 15','Lorant':'Januar 15','Pal':('Januar 15','Januar 18','Januar 25','Februar 10','Februar 22','Aprilis 1','Aprilis 28','Junius 26','Junius 29','Junius 30','Oktober 19'),
                 'Gusztav':'Januar 16',
                 'Antal':'Januar 17','Antonia':'Januar 17',
                 'Piroska':'Januar 18','Margit':'Januar 18',
                 'Mario':'Januar 19','Sara':'Januar 19','Marta':'Januar 19',
                 'Fabian':'Januar 20','Sebestyen':'Januar 20',
                 'Agnes':'Januar 21','Agneta':'Januar 21',
                 'Artur':'Januar 22','Vince':'Januar 22',
                 'Rajmund':'Januar 23','Zelma':'Januar 23','Emerencia':'Januar 23','Emese':'Januar 23',
                 'Timot':'Januar 24','Ferenc':'Januar 24',
                 'Henrik':'Januar 25',
                 'Vanda':'Januar 26','Paula':'Januar 26','Timoteusz':'Januar 26',
                 'Angelika':'Januar 27',
                 'Karoly':'Januar 28','Karola':'Januar 28,Februar 2,Majus 9,November 4','Tamas':'Januar 28',
                 'Adel':'Januar 29','Valer':'Januar 29','Etelka':'Januar 29,Februar 5,Junius 11,Junius 12,Oktober 8,December 16',
                 'Martina':'Januar 30','Gerda':'Januar 30','Jacinta':'Januar 30',
                 'Marcella':'Januar 31','Janos':'Januar 31',}
    
    nev = mezo1a.get()
    if nev in januarnevek.keys():
        mezo2.delete(0,END)
        mezo2.insert(0,januarnevek[nev])
    else:
        mezo3.delete(0,END)
        mezo3.insert(0,"Nem talalhato a JANUAR honapban !")

def februariFOnevnapok():
    februarnevek = {'Ignac':'Februar 1',
                    'Karolina':'Februar 2','Aida':'Februar 2',
                    'Balazs':'Februar 3',
                    'Rahel':'Februar 4','Csenge':'Februar 4',
                    'Ingrid':'Februar 5','Agota':'Februar 5',
                    'Dorottya':'Februar 6','Dora':'Februar 6',
                    'Todor':'Februar 7','Romeo':'Februar 7',
                    'Aranka':'Februar 8',
                    'Abigel':'Februar 9','Alex':'Februar 9',
                    'Elvira':'Februar 10',
                    'Bertold':'Februar 11','Marietta':'Februar 11',
                    'Livia':'Februar 12','Lidia':'Februar 12',
                    'Ella':'Februar 13','Linda':'Februar 13',
                    'Balint':'Februar 14','Valentin':'Februar 14',
                    'Kolos':'Februar 15','Georgina':'Februar 15',
                    'Julianna':'Februar 16','Lilla':'Februar 16',
                    'Donat':'Februar 17',
                    'Bernadett':'Februar 18',
                    'Zsuzsanna':'Februar 19',
                    'Aladar':'Februar 20','Almos':'Februar 20',
                    'Eleonora':'Februar 21',
                    'Gerzson':'Februar 22',
                    'Alfred':'Februar 23',
                    'Matyas':'Februar 24',
                    'Geza':'Februar 25',
                    'Edina':'Februar 26',
                    'Akos':'Februar 27','Bator':'Februar 27',
                    'Elemer':'Februar 28'}
    
    nev = mezo1b.get()      
    if nev in februarnevek.keys():
        mezo2.delete(0,END)
        mezo2.insert(0,februarnevek[nev])
    else:
        mezo3.delete(0,END)
        mezo3.insert(0,"Nem talalhato a FEBRUAR honapban !")

def marciusiFOnevnapok():
    marciusnevek = {}

    nev = mezo1c.get()
    if nev in marciusnevek.keys():
        mezo2.delete(0,END)
        mezo2.insert(0,marciusnevek[nev])
    else:
        mezo3.delete(0,END)
        mezo3.insert(0,"Nem talalhato a MARCIUS honapban !")

def aprilisFOnevnapok():
    aprilisnevek = {}

    nev = mezo1d.get()
    if nev in aprilisnevek.keys():
        mezo2.delete(0,END)
        mezo2.insert(0,aprilisnevek[nev])
    else:
        mezo3.delete(0,END)
        mezo3.insert(0,"Nem talalhato az APRILIS honapban !")

def majusFOnevnapok():
    majusnevek = {}

    nev = mezo1e.get()
    if nev in majusnevek.keys():
        mezo2.delete(0,END)
        mezo2.insert(0,majusnevek[nev])
    else:
        mezo3.delete(0,END)
        mezo3.insert(0,"Nem talalhato a MAJUS honapban !")

def juniusFOnevnapok():
    juniusnevek = {}

    nev = mezo1f.get()
    if nev in juniusnevek.keys():
        mezo2.delete(0,END)
        mezo2.insert(0,juniusnevek[nev])
    else:
        mezo3.delete(0,END)
        mezo3.insert(0,"Nem talalhato a JUNIUS honapban !")

def juliusFOnevnapok():
    juliusnevek = {}

    nev = mezo1g.get()
    if nev in juliusnevek.keys():
        mezo2.delete(0,END)
        mezo2.insert(0,juliusnevek[nev])
    else:
        mezo3.delete(0,END)
        mezo3.insert(0,"Nem talalhato a JULIUS honapban !")

def augusztusFOnevnapok():
    augusztusnevek = {}

    nev = mezo1h.get()
    if nev in augusztusnevek.keys():
        mezo2.delete(0,END)
        mezo2.insert(0,augusztusnevek[nev])
    else:
        mezo3.delete(0,END)
        mezo3.insert(0,"Nem talalhato az AUGUSZTUS honapban !")

def szeptemberFOnevnapok():
    szeptembernevek = {}

    nev = mezo1i.get()
    if nev in szeptembernevek.keys():
        mezo2.delete(0,END)
        mezo2.insert(0,szeptembernevek[nev])
    else:
        mezo3.delete(0,END)
        mezo3.insert(0,"Nem talalhato a SZEPTEMBER honapban !")

def oktoberFOnevnapok():
    oktobernevek = {}

    nev = mezo1j.get()
    if nev in oktobernevek.keys():
        mezo2.delete(0,END)
        mezo2.insert(0,oktobernevek[nev])
    else:
        mezo3.delete(0,END)
        mezo3.insert(0,"Nem talahato az OKTOBER honapban !")

def novemberFOnevnapok():
    novembernevek = {}

    nev = mezo1k.get()
    if nev in novembernevek.keys():
        mezo2.delete(0,END)
        mezo2.insert(0,novembernevek[nev])
    else:
        mezo3.delete(0,END)
        mezo3.insert(0,"Nem talalhato a NOVEMBER honapban !")

def decemberFOnevnapok():
    decembernevek = {}

    nev = mezo1l.get()
    if nev in decembernevek.keys():
        mezo2.delete(0,END)
        mezo2.insert(0,decembernevek[nev])
    else:
        mezo3.delete(0,END)
        mezo3.insert(0,"Nem talalhato a DECEMBER honapban !")
    


def reset():
    mezo3.delete(first = 0 , last = 200)
    mezo2.delete(first = 0 , last = 200)
    mezo1a.delete(first = 0 , last = 200)
    mezo1b.delete(first = 0 , last = 200)
    mezo1c.delete(first = 0 , last = 200)
    mezo1d.delete(first = 0 , last = 200)
    mezo1e.delete(first = 0 , last = 200)
    mezo1f.delete(first = 0 , last = 200)
    mezo1g.delete(first = 0 , last = 200)
    mezo1h.delete(first = 0 , last = 200)
    mezo1i.delete(first = 0 , last = 200)
    mezo1j.delete(first = 0 , last = 200)
    mezo1k.delete(first = 0 , last = 200)
    mezo1l.delete(first = 0 , last = 200)

ablak = Tk()

cimke0 = Label(ablak,text = "N E V N A P O K    A Z    E V B E N")
cimke1a = Label(ablak,text = "-- NEVET IRD BE JANUAR ----------------->")
cimke1b = Label(ablak,text = "-- NEVET IRD BE FEBRUAR ---------------->")
cimke1c = Label(ablak,text = "-- NEVET IRD BE MARCIUS ---------------->")
cimke1d = Label(ablak,text = "-- NEVET IRD BE APRILIS ---------------->")
cimke1e = Label(ablak,text = "-- NEVET IRD BE MAJUS ------------------>")
cimke1f = Label(ablak,text = "-- NEVET IRD BE JUNIUS ----------------->")
cimke1g = Label(ablak,text = "-- NEVET IRD BE JULIUS ----------------->")
cimke1h = Label(ablak,text = "-- NEVET IRD BE AUGUSZTUS -------------->")
cimke1i = Label(ablak,text = "-- NEVET IRD BE SZEPTEMBER ------------->")
cimke1j = Label(ablak,text = "-- NEVET IRD BE OKTOBER ---------------->")
cimke1k = Label(ablak,text = "-- NEVET IRD BE NOVEMBER --------------->")
cimke1l = Label(ablak,text = "-- NEVET IRD BE DECEMBER --------------->")
cimke2 = Label(ablak,text = "-- talalhato ------------->")
cimke3 = Label(ablak,text = "-- nem talalhato --------->")

mezo1a = Entry(ablak)
mezo1b = Entry(ablak)
mezo1c = Entry(ablak)
mezo1d = Entry(ablak)
mezo1e = Entry(ablak)
mezo1f = Entry(ablak)
mezo1g = Entry(ablak)
mezo1h = Entry(ablak)
mezo1i = Entry(ablak)
mezo1j = Entry(ablak)
mezo1k = Entry(ablak)
mezo1l = Entry(ablak)

mezo2 = Entry(ablak)
mezo3 = Entry(ablak)

gomb1 = Button(ablak, text = "ELLENORIZ", command = januariFOnevnapok)
gomb2 = Button(ablak, text = "ELLENORIZ", command = februariFOnevnapok)
gomb3 = Button(ablak, text = "ELLENORIZ", command = marciusiFOnevnapok)
gomb4 = Button(ablak, text = "ELLENORIZ", command = aprilisFOnevnapok)
gomb5 = Button(ablak, text = "ELLENORIZ", command = majusFOnevnapok)
gomb6 = Button(ablak, text = "ELLENORIZ", command = juniusFOnevnapok)
gomb7 = Button(ablak, text = "ELLENORIZ", command = juliusFOnevnapok)
gomb8 = Button(ablak, text = "ELLENORIZ", command = augusztusFOnevnapok)
gomb9 = Button(ablak, text = "ELLENORIZ", command = szeptemberFOnevnapok)
gomb10 = Button(ablak, text = "ELLENORIZ", command = oktoberFOnevnapok)
gomb11 = Button(ablak, text = "ELLENORIZ", command = novemberFOnevnapok)
gomb12 = Button(ablak, text = "ELLENORIZ", command = decemberFOnevnapok)

gombreset = Button(ablak, text = "RESET",command=reset)

cimke0.grid(row = 1 , column = 2)

cimke1a.grid(row = 2 , sticky = W)
cimke1b.grid(row = 3 , sticky = W)
cimke1c.grid(row = 4 , sticky = W)
cimke1d.grid(row = 5 , sticky = W)
cimke1e.grid(row = 6 , sticky = W)
cimke1f.grid(row = 7 , sticky = W)
cimke1g.grid(row = 8 , sticky = W)
cimke1h.grid(row = 9 , sticky = W)
cimke1i.grid(row = 10 , sticky = W)
cimke1j.grid(row = 11 , sticky = W)
cimke1k.grid(row = 12 , sticky = W)
cimke1l.grid(row = 13 , sticky = W)

cimke2.grid(row = 16 , sticky = W)
cimke3.grid(row = 17 , sticky = W)

mezo1a.grid(row = 2 , column = 3)
mezo1b.grid(row = 3 , column = 3)
mezo1c.grid(row = 4 , column = 3)
mezo1d.grid(row = 5 , column = 3)
mezo1e.grid(row = 6 , column = 3)
mezo1f.grid(row = 7 , column = 3)
mezo1g.grid(row = 8 , column = 3)
mezo1h.grid(row = 9 , column = 3)
mezo1i.grid(row = 10 , column = 3)
mezo1j.grid(row = 11 , column = 3)
mezo1k.grid(row = 12 , column = 3)
mezo1l.grid(row = 13 , column = 3)

mezo2.grid(row = 16 , column = 2 , ipady = 3 , ipadx = 250)
mezo3.grid(row = 17 , column = 2 , ipadx = 50 , ipady = 2)

gomb1.grid(row = 2 , column = 2)
gomb2.grid(row = 3 , column = 2)
gomb3.grid(row = 4 , column = 2)
gomb4.grid(row = 5 , column = 2)
gomb5.grid(row = 6 , column = 2)
gomb6.grid(row = 7 , column = 2)
gomb7.grid(row = 8 , column = 2)
gomb8.grid(row = 9 , column = 2)
gomb9.grid(row = 10 , column = 2)
gomb10.grid(row = 11 , column = 2)
gomb11.grid(row = 12 , column = 2)
gomb12.grid(row = 13 , column = 2)

gombreset.grid(row = 19)

ablak.mainloop()
                             
'''from tkinter import*
def beirtnev():
    
    nev = mezo1.get()#input(" A NEV AZ : ") # input method
    if nev == "Alpar":# verifying methods and print message
        mezo2.insert(0,"Januar 1")
        #print("Januar 1")
    elif nev == "Fruzsina":
        mezo2.insert(0,"Januar 1")
    #print("Januar 1")
    elif nev == "Bazil":
        mezo2.insert(0,"Januar 1")
    #print("Januar 1")
        
    elif nev == "Abel":
        mezo2.insert(0,"Januar 2")
    #print("Januar 2")
    elif nev == "Gergely":
        mezo2.insert(0,"Januar 2")
    #print("Januar 2")
    elif nev == "Vazul":
        mezo2.insert(0,"Januar 2")
    #print("Januar 2")
        
    elif nev == "Benjamin":
        mezo2.insert(0,"Januar 3")
    #print("Januar 3")
    elif nev == "Genoveva":
        mezo2.insert(0,"Januar 3")
    #print("Januar 3")
    elif nev == "Gyongyver":
        mezo2.insert(0,"Januar 3 \n Januar 8")
    #print(" Januar 3 \n Januar 8")
    elif nev == "Dzsenifer":
        mezo2.insert(0,"Januar 3")
    #print("Januar 3")
        
    elif nev == "Leona":
        mezo2.insert(0,"Januar 4")
    #print("Januar 4")
    elif nev == "Titusz":
        mezo2.insert(0,"Januar 4")
    #print("Januar 4")
    elif nev == "Angela":
        mezo2.insert(0,"Januar 4 \n Januar 27")
    #print("Januar 4 \n Januar 27")
        
    elif nev == "Simon":
        mezo2.insert(0,"Januar 5")
    #print("Januar 5")
    elif nev == "Emilia":
        mezo2.insert(0,"Januar 5")
    #print("Januar 5")
        
    elif nev == "Boldizsar":
        mezo2.insert(0,"Januar 6")
    #print("Januar 6")
    elif nev == "Menyhert":
        mezo2.insert(0,"Januar 6")
    #print("Januar 6")
    elif nev == "Gaspar":
        mezo2.insert(0,"Januar 6")
    #print("Januar 6")
        
    elif nev == "Attila":
        mezo2.insert(0,"Januar 7")
    #print("Januar 7")
    elif nev == "Ramona":
        mezo2.insert(0,"Januar 7")
    #print("Januar 7")
    elif nev == "Etele":
        mezo2.insert(0,"Januar 7")
    #print("Januar 7")
    elif nev == "Rajmund":
        mezo2.insert(0,"Januar 7")
    #print("Januar 7")
    elif nev == "Balint":
        mezo2.insert(0,"Januar 7")
    #print("Januar 7")
  
    elif nev == "Keve":
        mezo2.insert(0,"Januar 8")
    #print("Januar 8")
    elif nev == "Szeverin":
        mezo2.insert(0,"Januar 8")
    #print("Januar 8")
    elif nev == "Szoreny":
        mezo2.insert(0,"Januar 8")
    #print("Januar 8")
    elif nev == "Marcell":
        mezo2.insert(0,"Januar 9 \n Januar 16")
    #print("Januar 9 \n Januar 16")
    elif nev == "Julianusz":
        mezo2.insert(0,"Januar 9")
    #print("Januar 9")
    
    elif nev == "Melania":
        mezo2.insert(0,"Januar 10")
    #print("Januar 10")
    elif nev == "Vilmos":
        mezo2.insert(0,"Januar 10")
    #print("Januar 10")
    elif nev == "Vilma":
        mezo2.insert(0,"Januar 10")
    #print("Januar 10")
    
    elif nev == "Agota":
        mezo2.insert(0,"Januar 11")
    #print("Januar 11")
    elif nev == "Honorata":
        mezo2.insert(0,"Januar 11")
    #print("Januar 11")
    
    elif nev == "Erno":
        mezo2.insert(0,"Januar 12")
    #print("Januar 12")
    elif nev == "Erneszta":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 12")
    #print("Januar 12")
    elif nev == "Tatjana":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 12")
    #print("Januar 12")
    
    elif nev == "Veronika":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 13")
    #print("Januar 13")
    elif nev == "Csongor":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 13")
    #print("Januar 13")
    elif nev == "Yvett":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 13")
    #print("Januar 13")
    
    elif nev == "Bodog":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 14")
    #print("Januar 14")
    elif nev == "Felix":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 14")
    #print("Januar 14")
    
    elif nev == "Lorand":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 15")
    #print("Januar 15")
    elif nev == "Lorant":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 15")
    #print("Januar 15")
    elif nev == "Pal":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 15 \n Januar 25")
    #print("Januar 15 \n Januar 25")
    
    elif nev == "Gusztav":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 16")
    #print("Januar 16")
    
    elif nev == "Antal":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 17")
    #print("Januar 17")
    elif nev == "Antonia":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 17")
    #print("Januar 17")
    
    elif nev == "Piroska":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 18")
    #print("Januar 18")
    elif nev == "Margit":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 18")
    #print("Januar 18")
    elif nev == "Mario":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 19")
    #print("Januar 19")
    elif nev == "Sara":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 19")
    #print("Januar 19")
    elif nev == "Marta":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 19")
    #print("Januar 19")
    
    elif nev == "Fabian":
        mezo2.delete(0,END)
        mezo2.insert(0,"Jnauar 20")
    #print("Januar 20")
    elif nev == "Sebestyen":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 20")
    #print("Januar 20")
    
    elif nev == "Agnes":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 21")
    #print("Januar 21")
    elif nev == "Agneta":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 21")
    #print("Januar 21")
    
    elif nev == "Artur":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 22")
    #print("Januar 22")
    elif nev == "Vince":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 22")
    #print("Januar 22")
    
    elif nev == "Rajmund":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 23")
    #print("Januar 23")
    elif nev == "Zelma":
        mezo2.delete(0,END)
        mezo2.insert(0,"Januar 23")
    #print("Januar 23")
    elif nev == "Emerencia":
        mezo2.insert(0,"Januar 23")
    #print("Januar 23")
    elif nev == "Emese":
        mezo2.insert(0,"Januar 23")
    #print("Januar 23")
    
    elif nev == "Timot":
        mezo2.insert(0,"Januar 24")
    #print("Januar 24")
    elif nev == "Ferenc":
        mezo2.insert(0,"Januar 24")
    #print("Januar 24")
    
    elif nev == "Henrik":
        mezo2.insert(0,"Januar 25")
    #print("Januar 25")
    
    elif nev == "Vanda":
        mezo2.insert(0,"Januar 26")
    #print("Januar 26")
    elif nev == "Paula":
        mezo2.insert(0,"Januar 26")
    #print("Januar 26")
    elif nev == "Timoteusz":
        mezo2.insert(0,"Januar 26")
    #print("Januar 26")
    
    elif nev == "Angelika":
        mezo2.insert(0,"Januar 27")
    #print("Januar 27")
    elif nev == "Karoly":
        mezo2.insert(0,"Januar 28")
    #print("Januar 28")
    elif nev == "Karola":
        mezo2.insert(0,"Januar 28")
    #print("Januar 28")
    elif nev == "Tamas":
        mezo2.insert(0,"Januar 28")
    #print("Januar 28")
    elif nev == "Adel":
        mezo2.insert(0,"Januar 29")
    #print("Januar 29")
    elif nev == "Valer":
        mezo2.insert(0,"Januar 29")
    #print("Januar 29")
    elif nev == "Martina":
        mezo2.insert(0,"Januar 30")
    #print("Januar 30")
    elif nev == "Gerda":
        mezo2.insert(0,"Januar 30")
    #print("Januar 30")
    elif nev == "Jacinta":
        mezo2.insert(0,"Januar 30")
    #print("Januar 30")
    elif nev == "Marcella":
        mezo2.insert(0,"Januar 31")
    #print("Januar 31")
    elif nev == "Janos":
        mezo2.insert(0,"Januar 31")
    #print("Januar 31")
    else:
        mezo3.insert(0,"Nincs a Januar honapban a keresett nev!")
        
    #print("Nincs a Januar honapban a keresett nev")
def reset():
    mezo3.delete(first=0,last=100)
    mezo2.delete(first=0,last=50)
    mezo1.delete(first=0,last=30)
    
abl1=Tk()
cimke0 = Label(abl1, text = " NEVEK NAPJAI JANURABAN ")
cimke1 = Label(abl1,text="-- NEVET IRD BE --> ")
cimke2 = Label(abl1,text="-- talalhato --> ")
cimke3 = Label(abl1,text="-- nem talalhato --> ")
mezo1 = Entry(abl1)
mezo2 = Entry(abl1)
mezo3 = Entry(abl1)
gomb1 = Button(abl1, text = "ELLENORIZ", command = beirtnev)
gomb2 = Button(abl1, text = 'RESET', command = reset)
cimke0.grid(row = 1,column = 2)
cimke1.grid(row = 2, sticky = W)
gomb1.grid(row = 3)
gomb2.grid(row = 6)
cimke2.grid(row = 4, sticky = W)
cimke3.grid(row = 5, sticky = W)
mezo1.grid(row = 2, column = 2)
mezo2.grid(row = 4, column = 2)
mezo3.grid(row = 5,column = 2,ipadx = 50, ipady = 2)
abl1.mainloop()'''





































































    
