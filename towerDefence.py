######################
###Tower Defense V1###
######################

###Imports###

import Tkinter
import math

###Variables###

root = Tkinter.Tk()
tower = Tkinter.IntVar()
cash = 500
life = 100
count = 0
wavec = 90
enemiesl = 0
timespeed = 1
orange = []
a = [1,1,2,5]
b = [1,1,2,5]
c = [1,1,2,5]
d = [1,1,2,5]
e = [1,1,2,5]
f = [1,1,2,5]
g = [1,1,2,5]
h = [1,1,2,5]
i = [1,1,2,5]
j = [1,1,2,5]
enemies = [a,b,c,d,e,f,g,h,i,j]
t1 = []
t2 = []
t3 = []

###Functions

def tower1D(event):
    y=canvas.create_rectangle(event.x-18,event.y-6,event.x+18,event.y+6, fill="green", outline="green")
    x=canvas.create_rectangle(event.x-12,event.y-12,event.x+12,event.y+12, fill="#00ff00", outline="#00ff00")
    z=canvas.create_polygon(event.x-3,event.y-20,event.x+3,event.y-20,event.x+3,event.y,event.x-3,event.y, fill="#ff0000", outline="#ff0000")
    return [x,1,40,100,0,0,0,y,z]

def tower2D(event):
    b=canvas.create_rectangle(event.x-18,event.y-4,event.x+18,event.y+6, fill="grey", outline="grey")
    a=canvas.create_rectangle(event.x-14,event.y-10,event.x+14,event.y+12, fill="#a52a2a", outline="#a52a2a")
    c=canvas.create_polygon(event.x-10,event.y+4,event.x+10,event.y+4,event.x+10,event.y+10,event.x-10,event.y+10, fill="#006400", outline="#006400")
    d=canvas.create_polygon(event.x-8,event.y-20,event.x-2,event.y-20,event.x-2,event.y+2,event.x-8,event.y+2, fill="red", outline="red")
    e=canvas.create_polygon(event.x+2,event.y-20,event.x+8,event.y-20,event.x+8,event.y+2,event.x+2,event.y+2, fill="red", outline="red")
    return [a,1,21,75,0,0,0,b,c,d,e]

def tower3D(event):
    a=canvas.create_oval(event.x-18,event.y-18,event.x+18,event.y+18, fill="black", outline="black")
    b=canvas.create_polygon(event.x-2,event.y-2,event.x-16,event.y-2,event.x-10,event.y-12, fill="yellow", outline="yellow")
    c=canvas.create_polygon(event.x+2,event.y-2,event.x+16,event.y-2,event.x+10,event.y-12, fill="yellow", outline="yellow")
    d=canvas.create_polygon(event.x,event.y+2,event.x-8,event.y+12,event.x+8,event.y+12, fill="yellow", outline="yellow")
    e=canvas.create_polygon(event.x,event.y+16,event.x-8,event.y+12,event.x+8,event.y+12, fill="yellow", outline="yellow")
    f=canvas.create_polygon(event.x-6,event.y-32,event.x+6,event.y-32,event.x+6,event.y+8,event.x-6,event.y+8, fill="blue", outline="blue")
    return [a,5,40,150,0,0,0,b,c,d,e,f]

def upD():
    global t1
    global t2
    global t3
    global orange
    global cash
    tf = 1
    try:
        x1,y1,x2,y2=canvas.coords(orange[-1])
        x=int((x1+x2)/2)
        y=int((y1+y2)/2)
        for n in range(len(t1)):
            if(t1[n][0] in canvas.find_overlapping(x-1,y-1,x+1,y+1)):
                if(cash>=10 and t1[n][4] < 10): 
                    t1[n][1] = t1[n][1] + 1
                    cash = cash - 10
                    t1[n][4] = t1[n][4] + 1
                    updamage.config(text="Ugrade damage\nUpgraded: " + str(t1[n][4]) + "\nDamage: " + str(t1[n][1]))
                tf = 0
        if(tf != 0):
            for n in range(len(t2)):
                if(t2[n][0] in canvas.find_overlapping(x-1,y-1,x+1,y+1)):
                    if(cash>=10 and t2[n][4] < 10): 
                        t2[n][1] = t2[n][1] + 1
                        cash = cash - 10
                        t2[n][4] = t2[n][4] + 1
                        updamage.config(text="Ugrade damage\nUpgraded: " + str(t2[n][4]) + "\nDamage: " + str(t2[n][1]))
                    tf = 0
        if(tf != 0):
            for n in range(len(t3)):
                if(t3[n][0] in canvas.find_overlapping(x-1,y-1,x+1,y+1)):
                    if(cash>=20 and t3[n][4] < 10): 
                        t3[n][1] = t3[n][1] + 5
                        cash = cash - 20
                        t3[n][4] = t3[n][4] + 1
                        updamage.config(text="Ugrade damage\nUpgraded: " + str(t3[n][4]) + "\nDamage: " + str(t3[n][1]))
                    tf = 0
    except:
        pass

def upR():
    global t1
    global t2
    global t3
    global orange
    global cash
    tf = 1
    try:
        x1,y1,x2,y2=canvas.coords(orange[-1])
        x=int((x1+x2)/2)
        y=int((y1+y2)/2)
        for n in range(len(t1)):
            if(t1[n][0] in canvas.find_overlapping(x-1,y-1,x+1,y+1)):
                if(cash>=10 and t1[n][5] < 10): 
                    t1[n][2] = t1[n][2] - 1
                    cash = cash - 10
                    t1[n][5] = t1[n][5] + 1
                    uprate.config(text="Ugrade rate\nUpgraded: " + str(t1[n][5]) + "\nRate: " + str(t1[n][2]))
                tf = 0
        if(tf != 0):
            for n in range(len(t2)):
                if(t2[n][0] in canvas.find_overlapping(x-1,y-1,x+1,y+1)):
                    if(cash>=10 and t2[n][5] < 10): 
                        t2[n][2] = t2[n][2] - 2
                        cash = cash - 10
                        t2[n][5] = t2[n][5] + 1
                        uprate.config(text="Ugrade rate\nUpgraded: " + str(t2[n][5]) + "\nRate: " + str(t2[n][2]))
                    tf = 0
        if(tf != 0):
            for n in range(len(t3)):
                if(t3[n][0] in canvas.find_overlapping(x-1,y-1,x+1,y+1)):
                    if(cash>=10 and t3[n][5] < 10): 
                        t3[n][2] = t3[n][2] - 1
                        cash = cash - 10
                        t3[n][5] = t3[n][5] + 1
                        uprate.config(text="Ugrade rate\nUpgraded: " + str(t3[n][5]) + "\nRate: " + str(t3[n][2]))
                    tf = 0
    except:
        pass

def upRG():
    global t1
    global t2
    global t3
    global orange
    global cash
    tf = 1
    try:
        x1,y1,x2,y2=canvas.coords(orange[-1])
        x=int((x1+x2)/2)
        y=int((y1+y2)/2)
        for n in range(len(t1)):
            if(t1[n][0] in canvas.find_overlapping(x-1,y-1,x+1,y+1)):
                if(cash>=10 and t1[n][6] < 10): 
                    t1[n][3] = t1[n][3] + 5
                    cash = cash - 10
                    t1[n][6] = t1[n][6] + 1
                    uprange.config(text="Ugrade range\nUpgraded: " + str(t1[n][6]) + "\nRange: " + str(t1[n][3]))
                tf = 0
        if(tf != 0):
            for n in range(len(t2)):
                if(t2[n][0] in canvas.find_overlapping(x-1,y-1,x+1,y+1)):
                    if(cash>=10 and t2[n][6] < 10): 
                        t2[n][3] = t2[n][3] + 5
                        cash = cash - 10
                        t2[n][6] = t2[n][6] + 1
                    uprange.config(text="Ugrade range\nUpgraded: " + str(t2[n][6]) + "\nRange: " + str(t2[n][3]))
                    tf = 0
        if(tf != 0):
            for n in range(len(t3)):
                if(t3[n][0] in canvas.find_overlapping(x-1,y-1,x+1,y+1)):
                    if(cash>=10 and t3[n][6] < 10): 
                        t3[n][3] = t3[n][3] + 5
                        cash = cash - 10
                        t3[n][6] = t3[n][6] + 1
                    uprange.config(text="Ugrade range\nUpgraded: " + str(t3[n][6]) + "\nRange: " + str(t3[n][3]))
                    tf = 0
    except:
        pass

def click(event):
    global cash
    global life
    global t1
    global t2
    global t3
    global wavec
    if(len(canvas.find_overlapping(event.x-18,event.y-20,event.x+18,event.y+12)) == 0):
        if(tower.get() == 1 and cash >= 10):
            cash = cash - 10
            t1.append(tower1D(event))
        elif(tower.get() == 2 and cash >= 20):
            cash = cash - 20
            t2.append(tower2D(event))
        elif(tower.get() == 3 and cash >= 30 and len(canvas.find_overlapping(event.x-18,event.y-32,event.x+18,event.y+18)) == 0):
            cash = cash - 30
            t3.append(tower3D(event))
        updamage.config(text="Ugrade damage")
        uprate.config(text="Ugrade rate")
        uprange.config(text="Ugrade range")
        try:
            if(len(orange) > 0):
                canvas.delete(orange[-1])
                orange.pop[-1]
        except:
            pass
    elif(len(canvas.find_overlapping(event.x-1,event.y-1,event.x+1,event.y+1)) >= 0):
        try:
            if(len(orange) > 0):
                canvas.delete(orange[-1])
                orange.pop[-1]
        except:
            pass
        updamage.config(text="Ugrade damage")
        uprate.config(text="Ugrade rate")
        uprange.config(text="Ugrade range")
        for z in range(len(t1)):
            if(t1[z][0] in canvas.find_overlapping(event.x-1,event.y-1,event.x+1,event.y+1)):
                x1,y1,x2,y2 = canvas.coords(t1[z][0])
                x=(x1+x2)/2
                y=(y1+y2)/2
                orange.append(canvas.create_oval(x-t1[z][3],y-t1[z][3],x+t1[z][3],y+t1[z][3],fill="#808080",stipple="gray1"))
                updamage.config(text="Ugrade damage\nUpgraded: " + str(t1[z][4]) + "\nDamage: " + str(t1[z][1]))
                uprate.config(text="Ugrade rate\nUpgraded: " + str(t1[z][5]) + "\nRate: " + str(t1[z][2]))
                uprange.config(text="Ugrade range\nUpgraded: " + str(t1[z][6]) + "\nRange: " + str(t1[z][3]))
        for z in range(len(t2)):
            if(t2[z][0] in canvas.find_overlapping(event.x-1,event.y-1,event.x+1,event.y+1)):
                x1,y1,x2,y2 = canvas.coords(t2[z][0])
                x=(x1+x2)/2
                y=(y1+y2)/2
                orange.append(canvas.create_oval(x-t2[z][3],y-t2[z][3],x+t2[z][3],y+t2[z][3],fill="#808080",stipple="gray25"))
                updamage.config(text="Ugrade damage\nUpgraded: " + str(t2[z][4]) + "\nDamage: " + str(t2[z][1]))
                uprate.config(text="Ugrade rate\nUpgraded: " + str(t2[z][5]) + "\nRate: " + str(t2[z][2]))
                uprange.config(text="Ugrade range\nUpgraded: " + str(t2[z][6]) + "\nRange: " + str(t2[z][3]))
        for z in range(len(t3)):
            if(t3[z][0] in canvas.find_overlapping(event.x-1,event.y-1,event.x+1,event.y+1)):
                x1,y1,x2,y2 = canvas.coords(t3[z][0])
                x=(x1+x2)/2
                y=(y1+y2)/2
                orange.append(canvas.create_oval(x-t3[z][3],y-t3[z][3],x+t3[z][3],y+t3[z][3],fill="#808080",stipple="gray25"))
                updamage.config(text="Ugrade damage\nUpgraded: " + str(t3[z][4]) + "\nDamage: " + str(t3[z][1]))
                uprate.config(text="Ugrade rate\nUpgraded: " + str(t3[z][5]) + "\nRate: " + str(t3[z][2]))
                uprange.config(text="Ugrade range\nUpgraded: " + str(t3[z][6]) + "\nRange: " + str(t3[z][3]))
    money.config(text="Cash: " + str(cash) + "\nLife: " + str(life) + "\nWave: " + str(wavec) + "\nEnemies left: " + str(enemiesl))

def wave():
    global wavec
    global enemies
    global enemiesl
    global life
    TF = 1
    for z in range(len(enemies)):
        if(len(enemies[z]) != 4):
            TF = 0
            break
    if(TF == 1):
        if(wavec>=100):
            print("You win!")
        elif(life <= 0):
            print("Game Over!")
        else:
            wavec += 1
            for n in range(10):
                enemies[n].insert(0,canvas.create_rectangle((n*-30)-13,58,(n*-30)-1,70,fill="black",outline="black"))
                enemies[n][1] = 1
                enemies[n][2] = 1
                enemies[n][3] = int(wavec/5)*.2 + 1
                enemies[n][4] = wavec
                canvas.itemconfig(enemies[n][0], fill=color(n))
                enemiesl += 1

def change():
    global enemies
    global enemiesl
    global life
    global cash
    global wavec
    for z in range(len(enemies)):
        if(enemies[z][0] in canvas.find_overlapping(-400,-1000,-1,80)):
            enemies[z][1] = 1
            enemies[z][2] = 1
            x1,y1,x2,y2 = canvas.coords(enemies[z][0])
            canvas.move(enemies[z][0], 0, 58-y1)
        elif(enemies[z][0] in canvas.find_overlapping(739,64,740,66)):
            enemies[z][1] = 2
            enemies[z][2] = 1
        elif(enemies[z][0] in canvas.find_overlapping(734,739,736,740)):
            enemies[z][1] = 1
            enemies[z][2] = -1
        elif(enemies[z][0] in canvas.find_overlapping(61,734,60,736)):
            enemies[z][1] = 2
            enemies[z][2] = -1
        elif(enemies[z][0] in canvas.find_overlapping(64,580,66,581)):
            enemies[z][1] = 1
            enemies[z][2] = 1
        elif(enemies[z][0] in canvas.find_overlapping(589,584,590,586)):
            enemies[z][1] = 2
            enemies[z][2] = -1
        elif(enemies[z][0] in canvas.find_overlapping(584,210,586,211)):
            enemies[z][1] = 1
            enemies[z][2] = -1
        elif(enemies[z][0] in canvas.find_overlapping(110,214,111,216)):
            enemies[z][1] = 2
            enemies[z][2] = 1
        elif(enemies[z][0] in canvas.find_overlapping(114,340,116,341)):
            enemies[z][1] = 1
            enemies[z][2] = 1
        elif(enemies[z][0] in canvas.find_overlapping(470,334,471,336)):
            enemies[z][1] = 2
            enemies[z][2] = 1
        elif(enemies[z][0] in canvas.find_overlapping(464,470,466,471)):
            enemies[z][1] = 1
            enemies[z][2] = -1
        elif(enemies[z][0] in canvas.find_overlapping(-10,460,0,470)):
            life = life - enemies[z][4]
            money.config(text="Cash: " + str(cash) + "\nLife: " + str(life) + "\nWave: " + str(wavec) + "\nEnemies left: " + str(enemiesl))
            canvas.delete(enemies[z][0])
            enemies[z].remove(enemies[z][0])
            enemiesl = enemiesl - 1
    
def movement():
    global enemies
    global timespeed
    for z in range(len(enemies)):
        speed = timespeed * enemies[z][2] * enemies[z][3]
        if(enemies[z][1] == 1):
            velocity_x = speed
            velocity_y = 0
        elif(enemies[z][1] == 2):
            velocity_y = speed
            velocity_x = 0
        if(len(enemies[z]) == 5):
            canvas.move(enemies[z][0], velocity_x, velocity_y)

def rotate(Object, ObjectC, pivot_point, enemy):
    #
    # This is a function used to find the angle from (0,0) to a given point 
    #
    def quad(point): 
        angle = 0
        
        try: # The try/except is requried because of the possibilty that the math.atan()
             # on the line below will be undefined (in the case is is 90 or 270)
            angle = math.atan(float(point[1]) / float(point[0])) * 180 / math.pi
            #print angle
            if (angle == 0): # In the case of 180 and 0 degrees it will be 0
                if (point[0] < 0): # If x coord is left of the origin
                    angle = 180
            elif (point[0] < 0): # If x coord is left of the origin
                angle += 180
            elif (point[0] > 0 and point[1] < 0): # If x is right and y is below the origin
                angle += 360
                
        except: # In case the value returned from math.atan() is undefined
            if (point[1] > 0): # If above the origin
                angle = 90
            else: # If below the origin
                angle = 270
                
        return angle

    current = [ObjectC[0][0] - ObjectC[3][0],ObjectC[0][1] - ObjectC[3][1]]
    enemy = [enemy[0] - pivot_point[0], enemy[1] - pivot_point[1]]  # Subtract
    theta = quad(enemy) - quad(current) # Subtracts 90 from the angle becaue the nutural position is 90 degrees
    #
    # The next line and the for loop translate the enemy and the object
    # so that the pivot point becomes the origin
    #
    coordinates = []
    for coordinate in ObjectC:
        x = coordinate[0] - pivot_point[0] # Subtract
        y = coordinate[1] - pivot_point[1] # Subtract
        coordinates.append([x, y])
    #print coordinates
    
    #
    # Rotates each point in the "coordinates" list and puts it into
    # the "new" list
    #
    new = []
    for coordinate in coordinates:
        d = math.sqrt(coordinate[0] ** 2 + coordinate[1] ** 2) # Finds the distance
        angle = quad(coordinate) # Finds the angle from the origin
        
        angle += theta # Changes it by theta
        
        # The next two lines convert polar coordinates to rectangular
        x = d * math.cos(math.radians(angle)) # Calculates the x coord
        y = d * math.sin(math.radians(angle)) # Calculates the y coord
        
        new.append([x + pivot_point[0],y + pivot_point[1]]) # Puts it in the new list and translates it back to original position
    canvas.coords(Object,new[0][0],new[0][1],new[1][0],new[1][1],new[2][0],new[2][1],new[3][0],new[3][1])


def attack():
    global count
    global cash
    global wavec
    global enemiesl
    global timespeed
    for tower in range(len(t1)):
        if(count % (t1[tower][2]/timespeed) == 0):
            for enemie in range(len(enemies)):
                try:
                    x1,y1,x2,y2 = canvas.coords(enemies[enemie][0])
                    x3,y3,x4,y4 = canvas.coords(t1[tower][0])
                    x = ((x1+x2)/2) - ((x3+x4)/2)
                    y = ((y1+y2)/2) - ((y3+y4)/2)
                    if(int((x**2 + y**2)**.5) < t1[tower][3]):
                        x5,y5,x6,y6,x7,y7,x8,y8 = canvas.coords(t1[tower][8])
                        rotate(t1[tower][8],[[x5,y5],[x6,y6],[x7,y7],[x8,y8]],[x3+12,y3+12],[(x1+x2)/2,(y1+y2)/2])
                        enemies[enemie][4] = enemies[enemie][4] - t1[tower][1]
                        if(enemies[enemie][4] <= 0):
                            canvas.delete(enemies[enemie][0])
                            enemies[enemie].remove(enemies[enemie][0])
                            enemiesl = enemiesl - 1
                            cash = cash + 1
                        else:
                            canvas.itemconfig(enemies[enemie][0],fill=color(enemie))
                        break
                except:
                    pass
    for tower in range(len(t2)):
        if(t2[tower][2] == 0):
            t2[tower][2] = 1
        if(count % (t2[tower][2]/timespeed) == 0):
            for enemie in range(len(enemies)):
                try:
                    x1,y1,x2,y2 = canvas.coords(enemies[enemie][0])
                    x3,y3,x4,y4 = canvas.coords(t2[tower][0])
                    x = ((x1+x2)/2) - ((x3+x4)/2)
                    y = ((y1+y2)/2) - ((y3+y4)/2)
                    if(int((x**2 + y**2)**.5) < t2[tower][3]):
                        x5,y5,x6,y6,x7,y7,x8,y8 = canvas.coords(t2[tower][8])
                        rotate(t2[tower][8],[[x5,y5],[x6,y6],[x7,y7],[x8,y8]],[x3+18,y3+4],[(x1+x2)/2,(y1+y2)/2])
                        x5,y5,x6,y6,x7,y7,x8,y8 = canvas.coords(t2[tower][9])
                        rotate(t2[tower][9],[[x5,y5],[x6,y6],[x7,y7],[x8,y8]],[x3+18,y3+4],[(x1+x2)/2,(y1+y2)/2])
                        x5,y5,x6,y6,x7,y7,x8,y8 = canvas.coords(t2[tower][10])
                        rotate(t2[tower][10],[[x5,y5],[x6,y6],[x7,y7],[x8,y8]],[x3+18,y3+4],[(x1+x2)/2,(y1+y2)/2])
                        enemies[enemie][4] = enemies[enemie][4] - t2[tower][1]
                        if(enemies[enemie][4] <= 0):
                            canvas.delete(enemies[enemie][0])
                            enemies[enemie].remove(enemies[enemie][0])
                            enemiesl = enemiesl - 1
                            cash = cash + 1
                        else:
                            canvas.itemconfig(enemies[enemie][0],fill=color(enemie))
                        break
                except:
                    pass
    for tower in range(len(t3)):
        if(count % (t3[tower][2]/timespeed) == 0):
            for enemie in range(len(enemies)):
                try:
                    x1,y1,x2,y2 = canvas.coords(enemies[enemie][0])
                    x3,y3,x4,y4 = canvas.coords(t3[tower][0])
                    x = ((x1+x2)/2) - ((x3+x4)/2)
                    y = ((y1+y2)/2) - ((y3+y4)/2)
                    if(int((x**2 + y**2)**.5) < t3[tower][3]):
                        x5,y5,x6,y6,x7,y7,x8,y8 = canvas.coords(t3[tower][11])
                        rotate(t3[tower][11],[[x5,y5],[x6,y6],[x7,y7],[x8,y8]],[x3+18,y3+18],[(x1+x2)/2,(y1+y2)/2])
                        enemies[enemie][4] = enemies[enemie][4] - t3[tower][1]
                        if(enemies[enemie][4] <= 0):
                            canvas.delete(enemies[enemie][0])
                            enemies[enemie].remove(enemies[enemie][0])
                            enemiesl = enemiesl - 1
                            cash = cash + 1
                        else:
                            canvas.itemconfig(enemies[enemie][0],fill=color(enemie))
                        break
                except:
                    pass
    money.config(text="Cash: " + str(cash) + "\nLife: " + str(life) + "\nWave: " + str(wavec) + "\nEnemies left: " + str(enemiesl))

def color(n):
    global enemies
    r = enemies[n][4] * 17
    g = 0
    b = 0
    if(r > 256):
        g = g + (int(r/255) * 17)
        r = r - (int(g/17)*255)
    if(g > 256):
        b = b + (int(g/255) * 17)
        g = g - (int(b/17)*255)
        print(b,g)
    if(b > 255):
        b = 255
    rh = (hex(r))[2:]
    if(len(rh)==1):
        rh = '0' + rh
    gh = (hex(g))[2:]
    if(len(gh)==1):
        gh = '0' + gh
    bh = (hex(b))[2:]
    if(len(bh)==1):
        bh = '0' + bh
    return "#"+rh+gh+bh

def locate():
    global enemies
    for n in range(len(enemies)):
        if(len(enemies[n]) != 4):
            print(canvas.coords(enemies[n][0]))

def cashstart(event):
    global cash
    if(cash == -1):
        try:
            cashs = int(cashbox.get())
            cash = cashs
        except:
            pass

def timec():
    global timespeed
    if(timespeed == 1):
            timespeed = 2
    elif(timespeed == 2):
        timespeed = 1

def press1(event):
    tower1.invoke()

def press2(event):
    tower2.invoke()

def press3(event):
    tower3.invoke()

def upD2(event):
    upD()

def upR2(event):
    upR()

def upRG2(event):
    upRG()

def callwave(event):
    wave()

###GUI Set Up###

canvas = Tkinter.Canvas(root, width=800, height=800, background='#000000')
canvas.grid(row=0, rowspan=7, column=1, columnspan=4)

tower1 = Tkinter.Radiobutton(root, text="Tower 1:", variable=tower, value=1)
tower1.grid(row=1, column=0)

tower2 = Tkinter.Radiobutton(root, text="Tower 2:", variable=tower, value=2)
tower2.grid(row=2, column=0)

tower3 = Tkinter.Radiobutton(root, text="Tower 3:", variable=tower, value=3)
tower3.grid(row=3, column=0)

money = Tkinter.Label(root, text="Cash: " + str(cash) + "\nLife: " + str(life) + "\nEnemies left: " + str(enemiesl))
money.grid(row=0, column=0)

start = Tkinter.Button(root, text="Start", command=wave)
start.grid(row=7, column=0)

updamage = Tkinter.Button(root, text="Upgrade damage", command=upD)
updamage.grid(row=4, column=0)

uprate = Tkinter.Button(root, text="Upgrade rate", command=upR)
uprate.grid(row=5, column=0)

uprange = Tkinter.Button(root, text="Upgrade range", command=upRG)
uprange.grid(row=6, column=0)

cashbox = Tkinter.Entry(root, text="Starting cash:")
cashbox.grid(row=7,column=3)

time = Tkinter.Button(root, text="Increase speed", command=timec)
time.grid(row=7,column=4)

trouble = Tkinter.Button(root, text="troubleshoot", command=locate)

###Track Creation###

canvas.create_rectangle(0, 50, 750, 80, fill="#32cd32", outline="#32cd32")
canvas.create_rectangle(720, 80, 750, 750, fill="#32cd32",outline="#32cd32")
canvas.create_rectangle(50, 720, 750, 750, fill="#32cd32",outline="#32cd32")
canvas.create_rectangle(50, 600, 80, 720, fill="#32cd32",outline="#32cd32")
canvas.create_rectangle(50, 600, 600, 570, fill="#32cd32",outline="#32cd32")
canvas.create_rectangle(570, 200, 600, 600, fill="#32cd32",outline="#32cd32")
canvas.create_rectangle(100, 200, 570, 230, fill="#32cd32",outline="#32cd32")
canvas.create_rectangle(100, 230, 130, 350, fill="#32cd32",outline="#32cd32")
canvas.create_rectangle(130, 320, 480, 350, fill="#32cd32",outline="#32cd32")
canvas.create_rectangle(450, 350, 480, 480, fill="#32cd32",outline="#32cd32")
canvas.create_rectangle(0, 450, 450, 480, fill="#32cd32",outline="#32cd32")
canvas.create_rectangle(10,60,50,70, fill="red",outline="red")
canvas.create_polygon(50,55,50,75,67,65, fill="red",outline="red")

###Clicking###

canvas.bind('<Button-1>', click)
cashbox.bind('<Leave>', cashstart)
root.bind('1', press1)
root.bind('2', press2)
root.bind('3', press3)
root.bind('q', upD2)
root.bind('w', upR2)
root.bind('e', upRG2)
root.bind('s', callwave)

###Animation###

def animate():
    global count
    change()
    movement()
    attack()
    count += 1
    canvas.after(5, animate)

animate()

root.mainloop()