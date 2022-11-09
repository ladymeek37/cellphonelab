class CellPhone:
    def __init__(self, model):
        self.model = model
        self.phone_number = "2103741613"
        self.contacts ={
            "Chace" : "2104008559",
            "Mama" : "2103942445",
            "Charli" : "2102677252"
            }
        self.messages = ["Hello!", "How are you?", "I love you."]
        self.vibrate_off = True

    def receive_text(self, message):
        self.messages.append(message)
        print ("New message:", message)

    def toggle_vibrate(self):
        self.vibrate_off = not self.vibrate_off
        if self.vibrate_off == True:
            print("Vibrate is off.")
        else:
            print("Vibrate is on.")

    def create_send_messge(self):
        self.new_message = input("Type Message:")
        self.to_contact = input("Who do you want to send the message to?")
        print (f'"{self.new_message}" was sent to {self.to_contact}')


