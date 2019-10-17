import keyboard
import time
f = open("text.txt", "r")
F = f.readlines()
keyboard.wait("page up")
for x in F:
	keyboard.write(x)
	time.sleep(1)


