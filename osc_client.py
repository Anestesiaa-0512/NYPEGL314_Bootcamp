# Huats 2023 oscstarterkit
from pythonosc import udp_client

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")

def OSC_Message():
	receive_ip = "127.0.0.1"
	receive_port = 8123
	address = "/print"
	messages = "Hello from OSC"
	send_message(receive_ip,receive_port,address,messages)

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "127.0.0.1"		# wlan ip ||| IP of server
PORT = 8123                        # Port number of server

addr = "/print" 
msg = "salutations from me" #controls the paremeter

#send_message(PI_A_ADDR, PORT, addr, msg)

#OSC_Message() #Uncomment and run file to test