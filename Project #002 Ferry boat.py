weight = 5000; plT=0; plC=0;min=0
vehicleW = input('Write the weight of the vehicle: ')
min=vehicleW
while vehicleW < weight:
    weight -= vehicleW
    vehicleT = raw_input('Write vehicle type T for Trucks and C for Cars: ')
    while vehicleT != 'T' and vehicleT != 'C':
        vehicleT = raw_input('Write vehicle type T or C: ')
    if vehicleT == 'T':
        print "You'll pay 100$"
        plT+=1
    else:
        print "You'll pay 70$"
        plC+=1
    if vehicleW < min:
        min = vehicleW
    vehicleW = input('Write the weight of the vehicle: ')

print "IMPORT OF VEHICLES IS OVER."

if plT > plC:
    print "There have entered more Trucks."
else:
    print "There have entered more Cars."

print min,"is the lightest vehicle that has entered."

print plT * 100 + plC * 70,"is the income of the ferry."
     
