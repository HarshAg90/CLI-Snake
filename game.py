import curses
from curses import wrapper
from random import randint
import time
from curses.textpad import rectangle

#Just need to fix some bugs, rest is done

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_RED)
    
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(3)
    WHITE_AND_RED = curses.color_pair(4)
    try:
        counter_win = curses.newwin(21,20,2,31)
        rectangle(stdscr,1,30, 23, 51)
        
        li=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        stdscr.nodelay(True)

        dir = "KEY_RIGHT"
        inp = "KEY_RIGHT"
        x_head,y_head= 0, 0
        snake = [[y_head,x_head]]

        r_x,r_y = randint(0,19),randint(0,19)
        li[r_x][r_y] = 2 
        stdscr.addstr(8,1,"food at "+ str(r_x)+", "+str(r_y),GREEN_AND_BLACK)

        snake_dead = False
        stdscr.addstr(5,1,"press any key to quit")
        while True:
            stdscr.addstr(6,1,"snake lenght "+str(len(snake)))
            counter_win.clear()
            food=False
            try:
                inp = stdscr.getkey()
            except:
                pass
            if dir == "KEY_RIGHT":
                if inp == "KEY_LEFT":
                    pass
                else:
                    dir = inp
                if x_head+1>19:
                    x_head-=20
                if li[x_head+1][y_head] == 1:
                    snake_dead=True
                    print("snake dead by Right")
                    print(*snake)
                    print([x_head+1,y_head])
                    break
                x_head+=1
                
            elif dir == "KEY_LEFT":
                if inp == "KEY_RIGHT":
                    pass
                else:
                    dir = inp
                if x_head-1<0:
                    x_head+=20
                if li[x_head-1][y_head] == 1:
                    print("snake dead by left")
                    print(*snake)
                    print([x_head-1,y_head])
                    snake_dead=True
                    break
                x_head-=1
            
            elif dir == "KEY_UP":
                if inp == "KEY_DOWN":
                    pass
                else:
                    dir = inp
                if y_head-1<0:
                    y_head+=20
                if li[x_head][y_head-1] == 1:
                    print("snake dead by up")
                    print(*snake)
                    print([x_head,y_head-1])
                    snake_dead=True
                    break
                y_head-=1
            
            elif dir == "KEY_DOWN":
                if inp == "KEY_UP":
                    pass
                else:
                    dir = inp
                if y_head+1>19:
                    y_head-=20
                if li[x_head][y_head+1] == 1:
                    print("snake dead by Down")
                    print(*snake)
                    print([x_head,y_head+1])
                    snake_dead=True
                    break
                y_head+=1
            elif inp == "c":
                break
            else:
                pass 

            if li[x_head][y_head] == 2:
                food = True
            
            snake.append([x_head,y_head])
            li[x_head][y_head] = 1
            li[snake[0][0]][snake[0][1]] = 0


            if not(food):
                snake.pop(0)
            else:
                food = False
                while True:
                    r_x,r_y = randint(0,19),randint(0,19)
                    if [r_y,r_x] in snake:
                        continue
                    else:
                        li[r_y][r_x] = 2
                        stdscr.addstr(8,1,"food at "+ str(r_x)+", "+str(r_y),GREEN_AND_BLACK)
                        break


            # rendering the board
            for x in range(20):
                for y in range(20):
                    if li[x][y] == 1:
                        counter_win.addstr(y,x," ",WHITE_AND_RED)
                    elif li[x][y] == 2:
                        counter_win.addstr(y,x,"o",GREEN_AND_BLACK)
                    else:
                        counter_win.addstr(y,x," ")
            time.sleep(0.1)
            counter_win.refresh()    
        if(snake_dead):
            stdscr.addstr(9,2,"Snake ded💀", RED_AND_WHITE)
            pause
        else:
            stdscr.addstr(9,2,"code ded💀", RED_AND_WHITE)
            counter_win.getch()
    except: 
        stdscr.addstr(1,10,'Please make sure ur terminal is atleast 20 char tall and 50 char wide')
        stdscr.addstr(2,20,'re run this program if it is')
    stdscr.clear()
    stdscr.refresh()
    stdscr.getch()
 
wrapper(main)