from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand=load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
movetime=0
beforex=x
beforey=y
handx, handy = random.randint(50, 900), random.randint(50, 900)
i=0
while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if movetime%10==0:
        t = i / 100
        x = (1 - t) * beforex + t * handx
        y = (1 - t) * beforey + t * handy
        i += 2
        if i>100:
            handx, handy = random.randint(50, 900), random.randint(50, 900)
            beforex = x
            beforey = y
            i = 0

    if beforex<=handx:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', x, y, 100, 100)

    hand.draw(handx, handy)
    update_canvas()
    frame = (frame + 1) % 8
    movetime+=1
    handle_events()

close_canvas()




