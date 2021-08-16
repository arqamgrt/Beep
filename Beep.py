#importing winsound module.
import winsound
import time
print("Hello! Welcome to this little effert by Arqam Mehmood.")
time.sleep(0.5)
print("You can play some stupid beeps by entering the number.")
time.sleep(0.1)
print("after every beep, pitch and time of playing of every beep will increase.")
time.sleep(0.2)
print("So, are You ready?")
time.sleep(0.2)
input("Press Enter to play.")
def loop():
 freq = 50
 dur = 50
 node = input("Please enter the number which you would like to play the nodes?")

 for i in range(0, int(node)):
  winsound.Beep(freq, dur)
  freq += 50
  dur += 50
  time.sleep(0.2)

loop()


while 'n':
 exit = input("Please press Y if you want to play again, otherwise, press n to exit.")
 if exit == 'y' or exit == 'Y':
  loop()
 elif exit == 'n' or exit == 'N':
  print("Exiting the program... Thanks for Playing.")
  time.sleep(1)
  break
 else:
  print("Wrong! Please press y or n to proceed.")
