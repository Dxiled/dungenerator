from pygame import *
import generate
import recommendStats
import rollStats
import WTF

init()

centerButton = Rect(300,300,400,60)
backButton = Rect(50,500,400,50)
nextButton = Rect(550,500,400,50)

strSquare = Rect(200,50,100,100)
dexSquare = Rect(300,50,100,100)
conSquare = Rect(400,50,100,100)
intSquare = Rect(500,50,100,100)
wisSquare = Rect(600,50,100,100)
chaSquare = Rect(700,50,100,100)

titleFont = font.SysFont("copperplategothic",100)
Font = font.SysFont("calibri",40)

title = titleFont.render("Dungenerator",False,(255,255,255))
newChar = Font.render("Give me a character!",False,(0,0,100))

def renderTextCenteredAt(text, font, colour, x, y, screen, allowed_width):
    words = text.split()
    lines = []
    while len(words) > 0:
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break
        line = ' '.join(line_words)
        lines.append(line)
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)
        tx = x - fw / 2
        ty = y + y_offset
        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))
        y_offset += fh

def titleScreen(window,click):
    draw.rect(window,(0,0,200),centerButton)
    window.blit(title,(100,70))
    mousePos = mouse.get_pos()
    if centerButton.collidepoint(mousePos):
        draw.rect(window,(0,0,255),centerButton)
        if click:
            return 1
    window.blit(newChar,(330,310))
    return 0

def displayCharacter(window,click,characterIntro):
    draw.rect(window,(200,0,0),backButton)
    draw.rect(window,(0,0,200),nextButton)
    renderTextCenteredAt(characterIntro, Font, (255,255,255), 500, 200, window, 800)
    mousePos = mouse.get_pos()
    if backButton.collidepoint(mousePos):
        draw.rect(window,(255,0,0),backButton)
        if click:
            return 1
    elif nextButton.collidepoint(mousePos):
        draw.rect(window,(0,0,255),nextButton)
        if click:
            return 3
    renderTextCenteredAt("Give me a different one.", Font, (100,0,0), 250, 505, window, 400)
    renderTextCenteredAt("Let's roll the stats!", Font, (0,0,100), 750, 505, window, 400)
    return 2

def assignStats(window,click,drag,statList,boxList):
    strFull = -1
    dexFull = -1
    conFull = -1
    intFull = -1
    wisFull = -1
    chaFull = -1
    holding = -1
    mousePos = mouse.get_pos()
    if click:
        for i in range(6):
            if boxList[i].collidepoint(mousePos) and i not in [strFull,dexFull,conFull,intFull,wisFull,chaFull]:
                holding = i
    if not drag:
        if holding != -1:
            if strSquare.collidepoint(mousePos):
                if strFull == -1:
                    strFull = holding
            if dexSquare.collidepoint(mousePos):
                if dexFull == -1:
                    dexFull = holding
            if conSquare.collidepoint(mousePos):
                if dexFull == -1:
                    dexFull = holding
            if intSquare.collidepoint(mousePos):
                if intFull == -1:
                    intFull = holding
            if wisSquare.collidepoint(mousePos):
                if wisFull == -1:
                    wisFull = holding
            if chaSquare.collidepoint(mousePos):
                if chaFull == -1:
                    chaFull = holding
            holding = -1
    else:
        for i in range(6):
            if i not in [strFull,dexFull,conFull,intFull,wisFull,chaFull]:
                if boxList[i].collidepoint(mousePos):
                    if holding == -1:
                        holding = i
                    if holding == i:
                        boxList[i] = Rect(mousePos[0]-50,mousePos[1]-50,100,100)
    draw.rect(window,(100,100,100),strSquare,2)
    renderTextCenteredAt("STR", Font, (100,100,100), 250, 150, window, 100)
    draw.rect(window,(100,100,100),dexSquare,2)
    renderTextCenteredAt("DEX", Font, (100,100,100), 350, 150, window, 100)
    draw.rect(window,(100,100,100),conSquare,2)
    renderTextCenteredAt("CON", Font, (100,100,100), 450, 150, window, 100)
    draw.rect(window,(100,100,100),intSquare,2)
    renderTextCenteredAt("INT", Font, (100,100,100), 550, 150, window, 100)
    draw.rect(window,(100,100,100),wisSquare,2)
    renderTextCenteredAt("WIS", Font, (100,100,100), 650, 150, window, 100)
    draw.rect(window,(100,100,100),chaSquare,2)
    renderTextCenteredAt("CHA", Font, (100,100,100), 750, 150, window, 100)
    for i in range(6):
        draw.rect(window,(200,200,200),boxList[i])
        renderTextCenteredAt(str(statList[i]),Font,(0,0,0),boxList[i][0]+50,boxList[i][1]+50, window, 100)
    return 4

def main():
    screen = display.set_mode((1000,600))
    state = 0
    running = True
    clicking = False
    dragging = False
    while running:
        screen.fill((0,0,0))
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
            if evnt.type == MOUSEBUTTONDOWN:
                clicking = True
            if evnt.type == MOUSEBUTTONUP:
                dragging = False
        if state == 0:
            state = titleScreen(screen,clicking)
        elif state == 1:
            adjective = generate.adj()
            race = generate.rc()
            cclass = generate.pclass()
            location = generate.loc()
            backstory = generate.bstory()
            welcome = generate.intro(adjective,race,cclass,location,backstory)
            state = 2
        elif state == 2:
            state = displayCharacter(screen,clicking,welcome)
        elif state == 3:
            stats = rollStats.rollStats()
            stats = recommendStats.recommend(cclass,stats)
            rectList = []
            for i in range(6):
                rectList.append(Rect(100*i+200,250,100,100))
            state = 4
        elif state == 4:
            state = assignStats(screen,clicking,dragging,stats,rectList)
        else:
            running = False
        if clicking:
            clicking = False
            dragging = True
        display.flip()
    quit()

main()