from gpiozero import Button

button1 = Button(24)
button2 = Button(12)
button3 = Button(18)

print("all set up")
button2.wait_for_press()
print("The button was pressed")
