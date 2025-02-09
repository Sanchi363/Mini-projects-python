#Greet good morning,good evening and afternoon as per time
import time
timestamp=time.strftime('%H:%M:%S')  #this is a string.
print(timestamp)
timestamp=time.strftime('%H')        #timestamp is string.
if(int(timestamp)>=6 and int(timestamp)<12): # since timestamp is a string we can not compare it with integer so we have to typecast.
    print("Good Morning")
elif(int(timestamp)>=12 and int(timestamp)<17):
    print("Good Afternoon")
elif(int(timestamp)>=17 and int(timestamp)<20):
    print("Good Evening")
else:
    print("Good Night")            
