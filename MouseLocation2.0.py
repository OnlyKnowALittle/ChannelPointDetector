from pynput import mouse

#I want to make it so when you click, the coordinates of that click are put into a list.

Click_Locations = []
ClickXY = []

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    Click_Locations.append((x,y))
    if not pressed:
        #after mouse released - print clicking finished then delete an extra coo-rdinate not needed
        #then print the location list
        print("CLICKING FINISHED")
        Click_Locations.pop()
        print(Click_Locations)
        #MouseWatching()
        #print(Click_Locations[0])
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

def MouseWatching():

    # Collect events until released
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)
    listener.start()

MouseWatching()