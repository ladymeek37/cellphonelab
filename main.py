# 1. Print the cell phone’s contacts to the terminal
# 2. Send two new messages to the phone through the receive text message method
# 3. Print the cell phone’s messages to the terminal
# 4. Call the create text message method to create a new message
# 5. Toggle the cell phones ringer to vibrate
# 6. Print the cell phone’s current ringer/vibrate setting to the terminal

from cellphone import CellPhone
my_phone = CellPhone("Apple iPhone 13")

print("CONTACTS:", my_phone.contacts)

my_phone.receive_text("Hi, Lady!")
my_phone.receive_text("Wanna skate?")

my_phone.create_send_messge()

my_phone.toggle_vibrate()


