from pico2d import *

open_canvas()
run_character = load_image('robot_run.png')

def handle_events():
    global running
    global x

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x += 10
            elif event.key == SDLK_LEFT:
                x -= 10
            elif event.key == SDLK_ESCAPE:
                running = False

running = True
x = 800 // 2
y = 600 // 2
frame = 0

while running:
    clear_canvas()
    run_character.clip_draw(frame*63, 0, 60, 70, x, y)
    update_canvas()
    handle_events()
    frame = (frame+1) % 8
    delay(0.05)


close_canvas()

