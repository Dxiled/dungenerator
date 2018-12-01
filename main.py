from pygame import *
import generate
import recommendStats
import rollStats
import WTF

init()

centerButton = Rect(300,300,400,60)
backButton = Rect(50,500,400,50)
nextButton = Rect(550,500,400,50)

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
            state = 4
        elif state == 4:
            pass
        else:
            running = False
        if clicking:
            clicking = False
            dragging = True
        display.flip()
    quit()

main()