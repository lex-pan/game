# Screen and button variables
time = 50
homeScreen = True

buttonColor = color(0, 200, 200)
buttonColor2 = color(200, 200, 0)
buttonColor3 = color(255, 0, 0)
helpScreen = False
planeDraw = True
tankDraw = True
def setup():
    # Main screen setup
    size(1000, 500)
    global img
    img = createGraphics(1000, 500)
    img.beginDraw()
    img.background(255)
    img.fill(0, 0, 255)
    # obstacles on the map
    img.rect(100, 100, 100, 100)
    img.rect(500, 250, 100, 100)
    img.rect(300, 250, 50, 50)
    img.rect(750, 250, 50, 50)
    img.rect(600, 100, 50, 50)
    img.rect(850, 380, 50, 50)      
    img.rect(100, 350, 75, 75)
    img.rect(850, 100, 50, 50)
    img.rect(325, 100, 60, 60)
    

    img.endDraw()
    
# plane
fly = loadImage("plane.PNG")

plane = PVector(800, 200)
turn = 180
speed = PVector(0, 0)
# Moving plane
move = True
moveUp = False
moveBack = False
turnCCW = False
turnCW = False
# Bullet
bullet = PVector(800, 200)
shot = False
frag = False
bulletSpeed = PVector(0, 0)
# tank
tank = PVector(400, 200)
turn2 = 0
speed2 = PVector(0,0)
# Moving tank
move2 = True
moveUp2 = False
moveBack2 = False
turnCCW2 = False
turnCW2 = False
#Bullet 2
bullet2 = PVector(400, 200)
shot2 = False
frag2 = False
bulletSpeed2 = PVector(0,0)
blox = False
blox1 = False
blox2 = False
blox3 = False
blox4 = False
blox5 = False
super = False
super2 = False
# Score
score = 0
score2 = 0
tankDeath = False
planeDeath = False

def draw():
    fly = loadImage("plane.PNG")

    global blox
    global blox2
    global blox3
    global super
    global super2
    global img
    global home
    global homeScreen
    global helpScreen    
    global time
    global planeDraw
    global tankDraw
    # Scores
    global score
    global score2
    # plane Global
    global speed
    global turn
    global plane
    global move
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global bullet
    global shot
    global frag
    # tank Global
    global speed2
    global turn2
    global tank
    global move2
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global bullet2
    global shot2
    global frag2
    global tankDeath
    global planeDeath
    
    # Motion Control
    if move == False:
        moveUp = False
        moveBack = False
        turnCW = False
        turnCCW = False
    
    if move2 == False:
        moveUp2 = False
        moveBack2 = False
        turnCW2 = False
        turnCCW2 = False
    
    font = createFont("Ubuntu Mono Bold", 20)# PrimaryFont
    font2 = createFont("URW Bookman L Demi Bold", 20)# Decorative Font
    # Different settings for screens
    if homeScreen == True:
        planeDraw = False
        tankDraw = False
        background(0)
        global buttonColor
        global buttonColor2
        global buttonColor3
        background(150)
        noStroke()
        fill(0)
        #textFont(font2)
        textSize(90)
        # Main title
        text("Tank vs Plane", 200, 150)
        fill(buttonColor)
        rect(250, 210, 480, 220)
        fill(0)
        #textFont(font)
        textSize(150)
        text("PLAY", 310, 370)
        fill(buttonColor2)
        rect(20, 20, 150, 40)
        fill(0)
        textSize(24)
        text("How to play", 25, 45)
        # Selecting between screens and controls on the screens
        
        # planes stay still on home screen
        plane.sub(speed.mult(6))
        tank.sub(speed2.mult(3))
    elif helpScreen == True:
        planeDraw = False
        tankDraw = False
        background(255)
        text("Player 1: You are the plane! Fly over obstacles at high speed, but you turn slowly and cannot go backwards.", 100, 100)
        text("Use WASD to move, and Q to shoot.", 100, 180)
        text("Player 2: You are the plane! Sturdy and with powerful bullets, yet slow and limited by obstacles", 100, 280)
        text("Use the arrow keys to move, and M to shoot.", 100, 360)
        fill(buttonColor3)
        rect(0, 0, 30, 30)
        fill(0)
        textSize(30)
        text("X", 10, 30)
    # Main game screen
    else:
    
        background(img)
        stroke(0)
        strokeWeight(4)
        line(0, 425, 1000, 425)
        noStroke()
        textSize(40)
        fill(0, 255, 100)
        text(score, 250, 480)
        fill(255, 0, 100)
        text(score2, 700, 480)
        stroke(0)
        strokeWeight(1)
        

        # Bullets for plane
    speed = PVector.fromAngle(radians(turn))
    if super == True and planeDraw == True and tankDraw == True:
        noStroke()
        fill(random(1)*255, 0, 0)
        ellipse(bullet.x, bullet.y, 50, 50)
    elif planeDraw == True and tankDraw == True:
        fill(0)
        ellipse(bullet.x, bullet.y, 6, 6)
    if shot == False:
        bullet.set(plane)
        bulletSpeed.set(speed.mult(16))
        global bulletTime
        global breakTime
        bulletTime = 0
        breakTime = 0
    else:
        global bulletTime
        global breakTime
        bullet.add(bulletSpeed)
        if breakTime >= 10 and super == False:
            if get(int(bullet.x+10), int(bullet.y)) != -1:
                shot = False
            elif get(int(bullet.x-10), int(bullet.y)) != -1:
                shot = False
            if get(int(bullet.x), int(bullet.y+10)) != -1:
                shot = False
            elif get(int(bullet.x), int(bullet.y-10)) != -1:
                shot = False
        bulletTime += 1
        breakTime += 1    
    
    if super == True:
        bulletSpeed.set(speed.mult(4))
        if shot == True:
            if (bullet.x <= 0 or bullet.x >= 1000) and (bullet.y <= 0 or bullet.y >= 500):
                super = False
                shot = False
        
            """
            v1 = PVector(tank.x-bullet.x, tank.y-bullet.y)
            v2 = v1.heading()
            bulletPoint = bulletSpeed.fromAngle(v2)
            angle1 = bulletSpeed.heading()
            angle2 = bulletPoint.heading()
            angle1 = degrees(angle1)
            angle2 = degrees(angle2)
            if angle1 > -90 and angle1 < 0 and angle2 < 90 and angle2 > 0:
                print("")
            elif angle1 <= 0:
                angle1 += 360
            if angle2 > -90 and angle2 < 0 and angle1 < 90 and angle1 > 0:
                print("")
            elif angle2 <= 0:
                angle2 += 360
            if angle1 > angle2:
                angle1 -= 5
            if angle2 > angle1:
                angle1 += 5
            bulletSpeed.set(PVector.fromAngle(radians(angle1)))
            
            bulletSpeed.mult(2.5)
"""
        
            
    # Bullets for tank
    fill(0)
    speed2 = PVector.fromAngle(radians(turn2))
    if super2 == True and planeDraw == True and tankDraw == True:
        noStroke()
        fill(random(1)*255, 0, 0)
        ellipse(bullet2.x, bullet2.y, 10, 10)
    elif planeDraw == True and tankDraw == True:
        ellipse(bullet2.x, bullet2.y, 6, 6)
    if shot2 == False:
        bullet2.set(tank)
        bulletSpeed2.set(speed2.mult(18))
        global bulletTime2
        global breakTime2
        breakTime2 = 0
        bulletTime2 = 0
    else:
        global bulletTime2
        global breakTime2
        bullet2.add(bulletSpeed2)
        if breakTime2 >= 5 and super2 == False:
            if get(int(bullet2.x+1), int(bullet2.y)) != -1:
                shot2 = False
            elif get(int(bullet2.x-1), int(bullet2.y)) != -1:
                shot2 = False
            if get(int(bullet2.x), int(bullet2.y+1)) != -1:
                shot2 = False
            elif get(int(bullet2.x), int(bullet2.y-1)) != -1:
                shot2 = False
        bulletTime2 += 1
        breakTime2 += 1    
        if bulletTime2 >= 600:
            shot2 = False
            super2 = False

    safety = False
    if super2 == True:
        bulletSpeed2.set(speed.mult(50))
        if shot2 == True:
            
            global bulletTime2
            
            bulletTime2 += 1
            if bulletTime2 < 90:
                fill(0, 0, 255)
                rect(tank.x-75, tank.y-75, 150, 150)
                fill(255)
                rect(tank.x-70, tank.y-70, 140, 140)
                safety = True
            elif bulletTime2 >= 210:
                shot2 = False
                super2 = False
                bulletTime2 = 0
                
            elif bulletTime2 >= 90:
                translate(tank.x, tank.y)
                rotate(radians(turn2))
                noFill
                fill(random(255), random(255), random(255))
                triangle(0, 0, 1200, 50, 1200, -50)
                resetMatrix()
                safety = False
                turnCW2 = False
                turnCCW2 = False
            
            
            """
            v12 = PVector(plane.x-bullet2.x, plane.y-bullet2.y)
            v22 = v12.heading()
            bulletPoint2 = bulletSpeed2.fromAngle(v22)
            angle3 = bulletSpeed2.heading()
            angle4 = bulletPoint2.heading()
            angle3 = degrees(angle3)
            angle4 = degrees(angle4)
            if angle3 > -90 and angle3 < 0 and angle4 < 90 and angle4 > 0:
                print("")
            elif angle3 <= 0:
                angle3 += 360
            if angle4 > -90 and angle4 < 0 and angle3 < 90 and angle3 > 0:
                print("")
            elif angle4 <= 0:
                angle4 += 360
            if angle3 > angle4:
                angle3 -= 5
            if angle4 > angle3:
                angle3 += 5
    
            bulletSpeed2.set(PVector.fromAngle(radians(angle3)))
            bulletSpeed2.mult(2.5)
"""
        
    b = 38.65980825 # IMPORTANT NUMBER!!!
    
    # Edge detection
    UL = PVector.fromAngle(radians(turn+180+b)).mult(33) # Upper Left corner
    LL = PVector.fromAngle(radians(turn+180-b)).mult(33) # Lower Left corner
    UR = PVector.fromAngle(radians(turn-b)).mult(33) # Upper Right corner
    LR = PVector.fromAngle(radians(turn+b)).mult(33) # Lower Right corner

    speed = PVector.fromAngle(radians(turn))
    speed.mult(3)

    # Edge detection for player 2
    UL2 = PVector.fromAngle(radians(turn2+180+b)).mult(33)
    LL2 = PVector.fromAngle(radians(turn2+180-b)).mult(33)
    UR2 = PVector.fromAngle(radians(turn2-b)).mult(33)
    LR2 = PVector.fromAngle(radians(turn2+b)).mult(33)

    speed2 = PVector.fromAngle(radians(turn2))
    noFill()

    speed2.mult(3)
    if get(int(tank.x+speed2.x*14),int(tank.y+speed2.y*14)) != -1:
        tank.sub(speed2)
    if get(int(tank.x+UL2.x),int(tank.y+UL2.y)) != -1:
        tank.add(speed2)
        turnCCW2 = False
    elif get(int(tank.x+LL2.x),int(tank.y+LL2.y)) != -1:
        tank.add(speed2)
        turnCW2 = False
    if get(int(tank.x+UR2.x),int(tank.y+UR2.y)) != -1:
        tank.sub(speed2)
        turnCCW2 = False
    elif get(int(tank.x+LR2.x),int(tank.y+LR2.y)) != -1:
        tank.sub(speed2)
        turnCW2 = False
    stroke(0)
    # plane
    
    translate(plane.x, plane.y)
    rotate(radians(turn))
    
    if planeDraw == True:
        imageMode(CORNER)
        rotate(radians(90))
        image(fly, -43.5, -49, 87, 98)
        
        resetMatrix()
        translate(plane.x, plane.y)
        fill(0, 255, 100)
        textFont(font)
        text("P1", -10, 5)
    #Turning plane
    speed = PVector.fromAngle(radians(turn))
    # plane movement
    if plane.x >= 1000 :
        plane.x = 999
    elif plane.x <= 0:
        plane.x = 1
    elif plane.y >= 500:
        plane.y = 499
    elif plane.y <= 0:
        plane.y = 1
    elif moveUp == True:
        plane.add(speed.mult(7))
    #elif moveBack == True:
     #   plane.sub(speed.mult(6))
    if turnCCW == True:
        turn -= 3
    elif turnCW == True:
        turn += 3
    speed = PVector.fromAngle(radians(turn))
    resetMatrix()
#######################################################################################    

    # tank
    translate(tank.x, tank.y)
    rotate(radians(turn2))
    if tankDraw == True:
        fill(50, 50, 50)
        rect(-25, -20, 50, 40)
        rect(-25, -15, 50, 30)
        if super2 == True:
            rect(0, -6, 45, 12)
        else:
            rect(0, -3, 40, 6)
        ellipse(0, 0, 25, 25)
        resetMatrix()
        translate(tank.x, tank.y)
        fill(255, 0, 100)
        textFont(font)
        text("P2", -10, 5)
    # Turning tank
    speed2 = PVector.fromAngle(radians(turn2))
    # tank movement
    if tank.x >= 1000 :
        tank.x = 999
    elif tank.x <= 0:
        tank.x = 1
    elif tank.y >= 500 :
        tank.y = 499
    elif tank.y <= 0:
        tank.y = 1
    elif moveUp2 == True:
        tank.add(speed2.mult(3))
    elif moveBack2 == True:
        tank.sub(speed2.mult(3))
    if turnCCW2 == True:
        turn2 -= 4
    elif turnCW2 == True:
        turn2 += 4
    speed2 = PVector.fromAngle(radians(turn2))
#########################################################################################################################3
    resetMatrix()
    planeDraw = True
    tankDraw = True
    move = True
    move2 = True
    # Bullet Kills

    if super == True and bullet.x-tank.x <= 70 and bullet.x-tank.x >= -70 and bullet.y-tank.y <= 70 and bullet.y-tank.y >= -70:
        tankDeath = True
    
    elif bullet.x-tank.x <= 20 and bullet.x-tank.x >= -20 and bullet.y-tank.y <= 20 and bullet.y-tank.y >= -20:
        tankDeath = True
    
            
    if tankDeath == True:
        if time <= 150:
            move2 = False
            move = False
            bullet.set(plane)

            noStroke()
            fill(255, 255, 0)
            ellipse(tank.x, tank.y, time, time)
            tankDraw = False
            time+=4
        elif time <= 250:
            bullet.set(tank)
            tankDraw = False
            noStroke()
            fill(255, 255, 0, 255-(time-150))
            ellipse(tank.x, tank.y, time, time)
            time+=4
        elif time <= 400:
            tankDraw = True
            move2 = True
            move = True
            tank.set(random(800), random(300))
            turn2 = random(360)
            turn = random(360)
            plane.set(random(800), random(300))
            tankDeath = False
            shot = False
            shot2 = False
            super = False
            super2 = False
            score += 1
            time = 50
    else:
        planeDraw = True
        TankDraw = True

    angleMeasure1 = PVector.fromAngle(radians(turn2))
    angleMeasure1.mult(100)
    
    angleMeasure2 = PVector(plane.x-tank.x, plane.y-tank.y)


    
 
    if super2 == True and shot2 == True and safety == False and (degrees(angleMeasure2.heading()) - degrees(angleMeasure1.heading()) < 5 and degrees(angleMeasure2.heading()) - degrees(angleMeasure1.heading()) > -5):
        planeDeath = True
    if bullet2.x-plane.x <= 30 and bullet2.x-plane.x >= -30 and bullet2.y-plane.y <= 40 and bullet2.y-plane.y >= -40:
        planeDeath = True
        
    if planeDeath == True:
        if time <= 150:
            move2 = False
            move = False
            bullet.set(plane)

            noStroke()
            fill(255, 255, 0)
            ellipse(plane.x, plane.y, time, time)
            planeDraw = False
            time+=4
        elif time <= 250:
            bullet.set(plane)
            planeDraw = False
            noStroke()
            fill(255, 255, 0, 255-(time-150))
            ellipse(plane.x, plane.y, time, time)
            time+=4
        elif time <= 400:
            planeDraw = True
            move2 = True
            move = True
            tank.set(random(800), random(300))
            turn2 = random(360)
            turn = random(360)
            plane.set(random(800), random(300))
            planeDeath = False
            shot = False
            shot2 = False
            super = False
            super2 = False
            score2 += 1
            time = 50
    else:
        planeDraw = True
        TankDraw = True
        


                               
################################################################################################################################
    
    resetMatrix()
    RNJesus = int(random(200))
    if RNJesus == 5:                   
        blox = True
    if blox == True:                
        fill(140)
        rect(230, 120, 40, 40)
        fill(0)
        ellipse(250, 140, 18, 18) 
        if ((tank.x - 230)**2 <= 400 or (tank.x - 270)**2 <= 400) and ((tank.y - 120)**2 <= 400 or (tank.y - 160)**2 <= 400):                                                
            blox = False
            super2 = True
        elif ((plane.x - 230)**2 <= 400 or (plane.x - 270)**2 <= 400) and ((plane.y - 120)**2 <= 400 or (plane.y - 160)**2 <= 400):                                                
            blox = False
            super = True
    if RNJesus == 69:                   
        blox2 = True
    if blox2 == True:                
        fill(140)
        rect(830, 240, 40, 40)
        fill(0)
        ellipse(850, 260, 18, 18) 
        if ((tank.x - 830)**2 <= 400 or (tank.x - 870)**2 <= 400) and ((tank.y - 240)**2 <= 400 or (tank.y - 280)**2 <= 400):                                                
            blox2 = False
            super2 = True
        elif ((plane.x - 830)**2 <= 400 or (plane.x - 870)**2 <= 400) and ((plane.y - 240)**2 <= 400 or (plane.y - 280)**2 <= 400):                                                
            blox2 = False
            super = True


        
                        
def mouseMoved():
    global buttonColor
    global buttonColor2
    global buttonColor3
    global helpScreen
    global homeScreen
   # Makes the buttons shange when mouse hovers over
    if mouseX <= 710 and mouseX >= 250 and mouseY <= 400 and mouseY >= 180:
        buttonColor = color(55, 255, 255)
    else:
        buttonColor = color(0, 200, 200)
    if mouseX >= 20 and mouseX <= 170 and mouseY >= 20 and mouseY <= 60:
        buttonColor2 = color(255, 255, 55)
    else:
        buttonColor2 = color(200, 200, 0)
    if mouseX <= 30 and mouseY <= 30:
        buttonColor3 = color(255, 100, 100)
    else:
        buttonColor3 = color(255, 0, 0)
def mouseClicked():
    global homeScreen
    global helpScreen
    #moves to game screen
    if mouseX <= 710 and mouseX >= 250 and mouseY <= 400 and mouseY >= 180:
        homeScreen = False
    #moves to instructions screen
    if mouseX <= 170 and mouseX >= 20 and mouseY >=20 and mouseY <= 60:
        helpScreen = True
        homeScreen = False
    # Moves back to home screen from help screen
    if helpScreen == True and mouseX <= 30 and mouseY <= 30:
        helpScreen = False
        homeScreen = True
def keyPressed():
    # plane
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    global shot
    #controls for plane
    if key == "w":
        moveUp = True
        moveBack = False
    if key == "s":
        moveBack = True
        moveUp = False
    if key == "a":
        turnCCW = True
        turnCW = False
    if key == "d":
        turnCW = True
        turnCCW = False
    if key == "q":
        shot = True
    # tank
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    global shot2
    #controls for tank
    if keyCode == UP:
        moveUp2 = True
        moveBack2 = False
    if keyCode == DOWN:
        moveBack2 = True
        moveUp2 = False
    if keyCode == LEFT:
        turnCCW2 = True
        turnCW2 = False
    if keyCode == RIGHT:
        turnCW2 = True
        turnCCW2 = False
    if key == "m":
        shot2 = True
def keyReleased():
    # plane
    global moveUp
    global moveBack
    global turnCCW
    global turnCW
    if key == "w":
        moveUp = False
    if key == "s":
        moveBack = False
    if key == "a":
        turnCCW = False
    if key == "d":
        turnCW = False
    # tank
    global moveUp2
    global moveBack2
    global turnCCW2
    global turnCW2
    if keyCode == UP:
        moveUp2 = False
    if keyCode == DOWN:
        moveBack2 = False
    if keyCode == LEFT:
        turnCCW2 = False
    if keyCode == RIGHT:
        turnCW2 = False
