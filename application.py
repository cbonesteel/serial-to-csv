import serial, csv

arduino_port = "/dev/cu.usbmodem141401" # Change this to your port
baud = 9600 # Do not change
filename = "output.csv"

arduino = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)
with open(filename, 'w', newline='') as csvfile:
    print("Created file")

    sample = 200 # Change to larger or maybe find way to autofinish

    writer = csv.writer(csvfile, delimiter=' ', dialect='excel')

    print("Printing Column Headers")
    writer.writerow(["Seconds"])

    line = 1 # Do not change

    while line <= sample:
        print("Line " + str(line) + ": writing...")
        getData=str(arduino.readline()) # Read from serial
        
        data=getData[2:][:-5] # Get data and write to terminal
        print(data)

        writer.writerow([data]) # write data to csv
        line = line+1

    print("Data collection complete!")
    csvfile.close()