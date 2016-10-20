'''
    Break reminder that pops up the web browser reminding the student to 
    take breaks  
'''
import time
import webbrowser
# Every two hours for a total of 3 breaks, a pop up browser will 
# play Rihanna's song "work" to remind 
# the student to take a break!
total_breaks = 3
break_count = 0
 
while (break_count < total_breaks):
  time.sleep(120)
  webbrowser.open("https://www.youtube.com/watch?v=6ma3y4yz2mw")
  break_count = break_count + 1