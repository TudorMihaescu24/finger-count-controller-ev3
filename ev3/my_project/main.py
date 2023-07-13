import curses

screen = curses.initscr() # Get the curses window
curses.noecho()           # turn off echoing of keyboard to screen
curses.cbreak()           # no enter key require
screen.keypad(True)       # use special vlaues for cursor keys

try:
    # while loop
    while True:   
        # read a char from the screen 
        char = screen.getch()
        # when q key is pressed, case sensitly! small little of q
        if char == ord('q'):
            break
        # when UP key is pressed
        elif char == curses.KEY_UP:
            print ("up")
        # when DOWN key is pressed
        elif char == curses.KEY_DOWN:
            print ("down")
        # when RIGHT key is pressed
        elif char == curses.KEY_RIGHT:
            print ("right")
        # when LEFT key is pressed
        elif char == curses.KEY_LEFT:
            print ("left")
        elif char == 10:
            print ("stop" )   
                 
finally:
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()