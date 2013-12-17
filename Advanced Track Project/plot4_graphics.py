# graphics for plot4.1
# 500x600 window

from graphics import *
import time

def diff_rect(x1,y1,x2,y2):				# for difficulty rect objects
	obj=Rectangle(Point(x1,y1),Point(x2,y2))
	obj.setWidth(3)
	obj.setFill(color_rgb(200,210,200))
	obj.setOutline(color_rgb(50,100,50))
      
	return obj
	
win = GraphWin('Connect 4', 450, 600) # give title and dimensions
playerturn=Text(Point(225,450),'Player 1')
playerturn.setFill('red')			# to display the turn

res_rect=Rectangle(Point(175,500),Point(275,580))		# reset rect
res_rect.setOutline(color_rgb(50,100,50))
res_rect.setWidth(3)
res_rect.setFill(color_rgb(200,210,200))
res_msg=Text(Point(225,540),'Reset')			# reset msg

easy=diff_rect(25,450,100,550)				# diff rects
med=diff_rect(175,450,250,550)
hard=diff_rect(325,450,400,550)
    
easy_msg=Text(Point(62,500),'Easy')				# diff rect msgs
med_msg=Text(Point(212,500),'Medium')
hard_msg=Text(Point(362,500),'Hard')
diff_msg=Text(Point(225,400),'Choose Difficulty')
         
cirarr=[Circle(Point(0,0),0)]					# cir array
msgarr=[Text(Point(0,0),'')]					# msg array
linarr=[]								# win line array
redwin=Text(Point(100,400),'0')
yelwin=Text(Point(350,400),'0')
redwin.setSize(18)
yelwin.setSize(18)
redwin.setStyle('bold')
yelwin.setStyle('bold')



def diff_level():				# to take diff input from user
         
    
    diff_msg.draw(win)
    easy.draw(win)
    med.draw(win)
    hard.draw(win)
    easy_msg.draw(win)
    med_msg.draw(win)
    hard_msg.draw(win)
    
    flag=0
    while(flag==0):
    	choice=win.getMouse()
    	x=choice.x
    	y=choice.y
    	if 400<x<450 and 0<y<50:
    		about()
    	elif 25<x<100 and 450<y<550:
    		diff=1
    		flag=1
    	elif 175<x<250 and 450<y<550:
    		diff=2
    		flag=1
    	elif 325<x<400 and 450<y<550:
    		diff=3
    		flag=1
    
    diff_msg.undraw()
    easy.undraw()
    med.undraw()
    hard.undraw()	
    easy_msg.undraw()
    med_msg.undraw()
    hard_msg.undraw()
    return diff

def main():
    	
       
    
    back = Rectangle(Point(0, 0), Point(500,600) )
    back.setFill('gray')
    back.draw(win)
    playerturn.draw(win)
    rect = Rectangle(Point(50, 50), Point(400,350) )		 #outer rect
    bluecolor=color_rgb(50,50,200)
    rect.setOutline(bluecolor)
    rect.setFill(bluecolor)
    
    redwin.setFill('red')
    yelwin.setFill('yellow')
    redwin.draw(win)
    yelwin.draw(win)
    
    
    rect.draw(win)
    for i in xrange(26):
    	for j in xrange(26):
    		if i*i+j*j >=700:
    		  	win.plotPixel(75-i,75-j,'gray')    # top-left
    			win.plotPixel(375+i,75-j,'gray')	# top-right
    			win.plotPixel(375+i,325+j,'gray')	# down-right
    			win.plotPixel(75-i,325+j,'gray')    # down-left
    			
    
    for i in xrange(7):
    	for j in xrange(6):
    		cir=Circle(Point(75+50*i,75+50*j),20)
    		cir2=Circle(Point(75+50*i+2,75+50*j+2),20)
    		cir.setFill('gray')
    		cir2.setFill('black')
    		cir2.draw(win)
    		cir.draw(win)
    
     
    
     
def redwincount(wintext,count):						# score transition effect
	
	for i in xrange(101):
	    wintext.setFill(color_rgb(255-i,(int)(1.55*i),(int)(1.55*i)))
	    time.sleep(0.004)
	wintext.setText(count)
	for i in xrange(101):
	    wintext.setFill(color_rgb(155+i,155-(int)(1.55*i),155-(int)(1.55*i)))
	    time.sleep(0.004)
	    
def yelwincount(wintext,count):
	
	for i in xrange(101):
	    wintext.setFill(color_rgb(255-i,255-i,(int)(1.55*i)))
	    time.sleep(0.004)
	wintext.setText(count)
	for i in xrange(101):
	    wintext.setFill(color_rgb(155+i,155+i,155-(int)(1.55*i)))
	    time.sleep(0.004)		
	  
    	
def dropcircle(i,j,colour):			# to dropdown a circle
    	
    cir = Circle(Point(-20,25), 20)
    cir.setFill(colour)
    cir.draw(win)
    cirarr.append(cir)
    for k in xrange(75+50*j+20):			# horizontal movement
    	cir.move(1,0)
    	time.sleep(0.002)
    for k in xrange(50*(i+1)):			# vertical movement
    	cir.move(0,1)
    	time.sleep(0.002)
    for k in xrange(26):				# slight rebound
    	cir.move(0,0.25-10*0.002*k)
    	time.sleep(0.002)	
    	
 
def exitcircle():
	for i in xrange(100):
		for cir in cirarr:
			cir.move(0,i*i/100)
	
		time.sleep(0.002)	
	    	
	
def printtext(st,x,y,colour):    
   message = Text(Point(x, y), st)
   message.setFill(colour)
   
   message.draw(win)
   msgarr.append(message)
   
def close():
   win.getMouse()
   win.close()
   
def winline(j,i,dy,dx):
	x=75+50*i
	y=75+50*j
	line=Line(Point(x,y),Point(x+dx,y+dy))
	line.setWidth(3)
	
	linarr.append(line)
	for i in xrange(75):
		time.sleep(0.002)
		lin=line.clone()
		lin.move(i*dx,i*dy)
		lin.draw(win)
		linarr.append(lin)
	
def erase_circle():	
	res_rect.undraw()
	res_msg.undraw()					# to remove circles, messages
	playerturn.setText('')			
	exitcircle()
	for m in msgarr:
		m.setText('')
		del m	
	for cir in cirarr:
		del cir
	
					   
 
def gameover():
	playerturn.setText('')
	res_rect.undraw()
	res_msg.undraw()
	
	rect1=Rectangle(Point(25,450),Point(125,550))
	rect1.setOutline(color_rgb(50,100,50))
	rect1.setWidth(3)
	rect1.setFill(color_rgb(200,210,200))
	rect1.draw(win)   
	
	rect2=Rectangle(Point(325,450),Point(425,550))
	rect2.setOutline(color_rgb(75,100,75))
	rect2.setWidth(3)
	rect2.setFill(color_rgb(200,210,200))
	rect2.draw(win)
	
	printtext('New Game',75,500,'black')
	printtext('Exit',375,500,'black')
	
	while 1 :
		choice=win.getMouse()
		x=choice.x
		y=choice.y
		if(25<x<125 and 450<y<550):				# new game
			rect1.undraw()
			rect2.undraw()
			exitcircle()
			for m in msgarr:
				m.setText('')
				del m	
			for l in linarr:
				l.undraw()
				del l	
			for cir in cirarr:
				del cir
			diff=diff_level()	
			return diff
			break
			
		elif(325<x<425 and 450<y<550):			# exit
			close()
			return 0
			break	
 
def about():
    back = Rectangle(Point(0, 0), Point(500,600) )
    back.setFill('gray')
    back.draw(win)
    head=Text(Point(225,75),'About')
    head.setSize(24)
    head.draw(win)
    text=Text(Point(225,175),'Developed by Aditya Bhutra (12043) ')
    text2=Text(Point(225,200),'as an ESC101 Advanced Track Project.')
    text.draw(win)
    text2.draw(win)
    get=win.getMouse()
    del(text)
    del(text2)
    del(head)
    del(back)
      
def getmouse(text,colour):
	playerturn.setText(text)
	playerturn.setFill(colour)
	
	while (1):
		pt=win.getMouse()
		x=pt.x
		y=pt.y
		for i in xrange(7):
			if 50*(i+1)<x<50*(i+2) and y<350:			# return column
				return (i)  
			elif 175<x<275  and 500<y<580:			# reset
				return -1	

				 
   
   




