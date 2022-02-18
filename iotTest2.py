import time
import serial
import csv
import webbrowser


ser = serial.Serial(
	port='/dev/ttyS0',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1000,
)
fname = "/etc/nginx/tempdata.csv"
#html_content = f"<html> <head> </head>  <body> </body>  </html>" 
#line='Vipi Bro'
while True:
	if ser.in_waiting > 0:
		line=ser.readline().decode()
		with open(fname,'w') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerow(line)
		readOut = "Temperature: "+line
		html_content = f"<html> <head> </head> <h1> {readOut} </h1> <body> </body> </html>"	
		with open("index.html","w") as html_file:
			html_file.write(html_content)
		print(line)
		time.sleep(1)



