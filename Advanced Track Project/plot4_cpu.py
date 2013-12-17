# to build a two player plot4 game
from plot4_graphics import *
import random

def start():                            # to start the game
    for i in xrange(6):
        for j in xrange(7):
            arr[i][j]='O'
    
    
    start_chance[0]=start_chance[0]*-1
    res_rect.draw(win)
    res_msg.draw(win)                       
    
    if start_chance[0]==1:                  # to alternate the first chance
        player1()
    else :
        player2()   
            
def player1() :                     # P1 function
    if checkflag('Y',0)==-1:            # check for draw
        printtext('Game ends in a draw',225,400,'black')
        f=gameover()
        if f>0:
            diff[0]=f
            start()
    col = getmouse('Player','red')      # input from user
    if col==-1:                     # for reset
        erase_circle()
        start() 
    
    else:
    
        if arr[0][col]=='O' :               # check for space in column 
            for i in range(5,-1,-1):
                if arr[i][col]=='O':
                    arr[i][col]='R'
                    dropcircle(i,col,'red') #dropping circle in window
                    break
            flag=checkflag('R',1)
            if flag==1:                 # checking whether p1 has won
                printtext('Player Wins !!',225,400,'black')
                winarr[0]+=1
                redwincount(redwin,winarr[0])
                f=gameover()
                if f>0:
                    diff[0]=f
                    start()
            elif    flag==-1:
                printtext('Game ends in a draw',225,400,'black')
                f=gameover()
                c
            
            else:
                player2()               # if not then calling P2
        
        else :
            player1()                   # if column if full then calling P1 again
        
def player2() : 
    dif=diff[0]     
    #print dif               # CPU
    playerturn.setText('CPU')
    playerturn.setFill('yellow')
    ran=random.randint(0,1)                         # randomization
    if make4('Y',1)==1:
        printtext('CPU wins ! ',225,400,'black')
        winarr[1]+=1
        yelwincount(yelwin,winarr[1])
        
        f=gameover()
        if f>0:
            diff[0]=f
            start()
    elif stop4()==1:                    # to stop opponents four
        player1()
    elif dif==3 and forced()==1:                    # check for forced column
        player1()   
    elif dif==2 and make3()==1:
        player1()
    elif    dif==2 and stop3()==1:
        player1()   
    elif dif==3 and ran==0 and make3()==1 or stop3()==1:        # random make3 or stop3
        player1()
    elif dif==3 and ran==1 and stop3()==1 or make3()==1:
        player1()
    elif dif==1 and rand_add()==1:
        player1()   
    elif center_add(1)==1:                  # center add without making 4
        player1()
    elif dif==3 and center_add(2)==1:       #centerforblockedcolumn                                         
        player1()
    elif center_add(-1)==1:             # forced center add
        player1()
    elif center_add(0)==1:              # forced center add
        player1()   
    else:               # checking if array is full
        printtext('Game ends in a draw',250,500,'black')
        f=gameover()
        if f>0:
            diff[0]=f
            start()

def rand_add():
    ran=random.randint(0,7)
    for i in xrange(7):
        col=(ran+i)%7
        for j in range(5,-1,-1):
            if arr[j][col]=='O':
                arr[j][col]='Y'
                dropcircle(j,col,'yellow')
                return 1
                
    return 0                            

def make4(ch,flag):                 # method to check whether cpu can make 4
    for j in xrange(7):             # flag 0-for just check ,1-for printing as well
        for i in range(5,-1,-1):
            if arr[i][j]=='O':
                arr[i][j]=ch    
                f=checkflag(ch,0)
                if f==1:
                    if flag==0:
                        arr[i][j]='O'
                        return 1                    # checking in a particular column
                    dropcircle(i,j,'yellow')    # if yes then add circle
                    f=checkflag('Y',1)      # printing winning line
                    return 1
                arr[i][j]='O'           # if no then reset the position to 'O'
                break   
    return 0        


def stop4():
    for j in xrange(7):
        for i in range(5,-1,-1):
            if arr[i][j]=='O':
                arr[i][j]='R'   
                f=checkflag('R',0)
                if f==1:    
                    arr[i][j]='Y'           # checking in a particular column
                    dropcircle(i,j,'yellow')    # if yes then add circle
                            
                    return 1
                
                arr[i][j]='O'           # if no then reset the position to 'O'
                break   
    return 0                        
                    
def make3():                                    # to make 3 in a row if possible
    sign=1
    col=3
    for j in xrange(7):
        sign=sign*-1    
        col=col+j*sign
        
        for i in range(5,-1,-1):
            
            if arr[i][col]=='O':
                arr[i][col]='Y'
                
                flag_oppwin=make4('R',0)        # check whether opponent wins on playing
                flag_selfwin=make4('Y',0)
                flag_make3=check3(i,col,'Y')        # check whether 3 in a row is possible
                if flag_make3==1 and flag_oppwin==0 and flag_selfwin==0:
                    dropcircle(i,col,'yellow')
                    return 1
                arr[i][col]='O'     
                break 
                
    return 0
    
def stop3():                                # to stop 3 in a row of opponent
    sign=1
    col=3
    for j in xrange(7):
        sign=sign*-1    
        col=col+j*sign
        for i in range(5,-1,-1):
            if arr[i][col]=='O':
                arr[i][col]='R'
                flag=check3(i,col,'R')
                arr[i][col]='Y'         # checking whether 3 in a row is poss.
                flag_oppwin=make4('R',0)
                arr[i][col]='X'
                flag_selfwin=make4('Y',0)       # checking whether self or opp win after playing
                if flag==1 and flag_oppwin==0 and flag_selfwin==0:
                    arr[i][col]='Y'
                    dropcircle(i,col,'yellow')
                    return 1
                arr[i][col]='O' 
                break
    return 0    


def useful_check3(i,j,inew,jnew,ch):            # check for useful 3 in a line
    arr[i][j]='O'
    arr[inew][jnew]=ch
    flag=checkflag(ch,0)
    arr[i][j]=ch
    arr[inew][jnew]='O'
    return flag
    

def check3(i,j,ch):
    if 0<i<4 :                              # vertical check
        if arr[i+1][j]==ch and arr[i+2][j]==ch :
             flag=useful_check3(i,j,i-1,j,ch)
             if flag==0:
                return 1    
            
    for col in xrange(7):                       # horizontal check
        if arr[i][col]=='O':
            arr[i][col]=ch
            if hor(i,ch,0)==1:
                flag=useful_check3(i,j,i,col,ch)    
                if flag==0:
                    arr[i][col]='O'
                    return 1
            arr[i][col]='O'
    
    for count in range(-3,4):                       # diagonal check
        if -1<i+count<6 and -1<j+count<7 and arr[i+count][j+count]=='O' :   # down diag
            arr[i+count][j+count]=ch
            if diag3(i,j,ch,1)==1:
                flag=useful_check3(i,j,i+count,j+count,ch)      
                if flag==0:
                    arr[i+count][j+count]='O'               # check for wasteful 3 
                    return 1
            arr[i+count][j+count]='O'   
            
        if -1<i-count<6 and -1<j+count<7 and arr[i-count][j+count]=='O' :   # up diag
            arr[i-count][j+count]=ch
            if diag3(i,j,ch,-1)==1:
                flag=useful_check3(i,j,i-count,j+count,ch)
                if flag==0:
                    arr[i-count][j+count]='O'
                    return 1    
            arr[i-count][j+count]='O'       
    return 0                                    



def diag3(i,j,c,shift):                             # check for 3 in a row for diag.
    while 0<i-shift<5 and 0<j-1<6 and arr[i-shift][j-1]==c :
        i=i-shift
        j=j-1
    if shift==1:
        if diagdown(i,c,0)==1:
            return 1
    elif diagup(i,c,0)==1:
        return 1
    return 0    
                

def forced():                                   # to check for forced win in a column
    for j in xrange(7):
        for i in range(5,0,-1):
            if arr[i][j]=='O':
                arr[i][j]='R'
                oppflag=checkflag('R',0)
                if oppflag==1:
                    arr[i][j]='O'
                    break
                arr[i][j]='Y'
                flag1=checkflag('Y',0)
                arr[i][j]='O'
                arr[i-1][j]='Y'
                flag2=checkflag('Y',0)
                arr[i-1][j]='O'
                if flag1==1 and flag2==1:
                    for row in range(5,0,-1):
                        if arr[row][j]=='O':
                            dropcircle(row,j,'yellow')
                            arr[row][j]='Y'
                            return 1
    return 0                        
                                    
        

def center_add(flag):                           # to add close to center line   with random side (left or right)
    sign=random.randint(0,1)
    if sign==0:
        sign=-1                         # flag - for selective adding
    col=3                                   # 0-free add
    for j in xrange(7):                         # 1-for non-blocked col
        sign=sign*-1                        # 2-for non make4
        col=col+j*sign                      # -1 - forced play in own make4
        for i in range(5,-1,-1):
            if arr[i][col]=='O':
                arr[i][col]='Y'
                if flag>0 :
                    flag_oppwin=make4('R',0)    # check for opp. win    
                    flag_selfwin=make4('Y',0)   # check for self win
                    if flag_oppwin==1 or flag_selfwin==1:
                        arr[i][col]='O'
                        break               # if any of above is true, then break
                if flag==1:
                    if block_col(col)==1:       # check if col. is blocked
                        arr[i][col]='O'
                        break;          # if yes then break
                if flag==-1:
                    if make4('Y',0)==0:     # when no choice, then play make own 4
                        arr[i][col]='O'
                        break
                            
                dropcircle(i,col,'yellow')      # else drop circle
                return 1    
                
    return 0        
                                         
def block_col(col):             # method to check for blocked col.
    for i in range(5,-1,-1):
        if arr[i][col]=='O':
            arr[i][col]='X'
            if checkflag('Y',0)==1 and checkflag('R',0)==1 :
                return 1
    for i in range(5,-1,-1):
        if arr[i][col]=='X':            # reverting changes made to array
            arr[i][col]='O'         
    return 0                                    
    
        

def checkflag (ch,line) :                   # function to check whether a player has won
    flag=0
    for i in range(5,-1,-1):
        if hor(i,ch,line)==1 or diagup(i,ch,line)==1 or diagdown(i,ch,line)==1 or vert(i,ch,line)==1 :# sending for diff checks
            flag=1
            break
    if flag==0:
        flag=-1
        for i in xrange(7):             # for draw condition
            if arr[0][i]=='O':
                flag=0
                break   
    
    return flag                     # returning result of check

def hor (i,c,line):             # function for horizontal check
    for j in xrange(4) :
        if arr[i][j]==c and arr[i][j+1]==c and arr[i][j+2]==c and arr[i][j+3]==c :
            if line==1:
                winline(i,j,0,2)
            return 1
    return 0                            

def diagup (i,c,line):
                    # function for up diagonal check
        if 2<i<6 :
            for j in xrange(4) :
                if arr[i][j]==c and arr[i-1][j+1]==c and arr[i-2][j+2]==c and arr[i-3][j+3]==c :
                    if line==1:
                        winline(i,j,-2,2)
                    return 1
        return 0
                    
def diagdown(i,c,line):                 
        if -1<i<3:              # function for down diagonal check
            for j in xrange(4) :
                if arr[i][j]==c and arr[i+1][j+1]==c and arr[i+2][j+2]==c and arr[i+3][j+3]==c :
                    if line==1:
                        winline(i,j,2,2)
                    return 1            
        return 0

def vert (i,c,line):                # function for vertical check
    if i>2 :
        for j in xrange(7) :
            if arr[i][j]==c and arr[i-1][j]==c and arr[i-2][j]==c and arr[i-3][j]==c :
                if line==1:
                    winline(i,j,-2,0)
                return 1
    return 0    

    
arr = [['O' for x in xrange(7)] for x in xrange(6)] # initializing array
winarr=[0 for x in xrange(2)]
Con4_msg=Text(Point(225,150),'Connect 4')
Con4_msg.setSize(32)
Con4_msg.setFill(color_rgb(150,50,220))
Con4_msg.draw(win)
printtext('About',400,25,'black')
diff=[1 for x in xrange(1)]
diff[0]=diff_level()
Con4_msg.undraw()
main()                              # for graphics
start_chance=[-1 for x in xrange(1)]    
                        
start()
                    
                    # starting game by calling start() func.
                    

