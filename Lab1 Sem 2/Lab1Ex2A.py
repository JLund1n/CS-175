def warmup2():
    file = open('rainfall.txt','r') #opens the text file

    #Create a list of the rainfall range categories
    fifty = []
    sixty = []
    seventy = []
    eighty = []
    ninety = []

    #Deetermine the rain height
    for raw_data in file:
        data = raw_data.split()#Takes the raw data and splits it
        data[1] = float(data[1])#Converts the string val of the data to a float
        #Well loop through the ranges and append the float to one of the rainfall categories
        if data[1]> 50 and data[1] <=60:
            fifty.append(data)
        elif data[1]> 60 and data[1] <=70:
            sixty.append(data)
        elif data[1]> 70 and data[1]<=80:
            seventy.append(data)
        elif data[1]> 80 and data[1]<=90:
            eighty.append(data)
        else:
            ninety.append(data)
    file.close()

    #By using the lambda function you can sort the above list based on the rainfalll data value
    fifty.sort(key=lambda x:x[1])
    sixty.sort(key=lambda x:x[1])
    seventy.sort(key=lambda x:x[1])
    eighty.sort(key=lambda x:x[1])
    ninety.sort(key=lambda x:x[1])

    #create the output file to store the data in
    file_output = open('rainfallfmt.txt','w')

    #Write the data to the file
    #As per the instructions:
    #field width: 25 centered and uppercase
    #field width: 5 right-aligned 1 decimal place
    file_output.write("[50-60mm]\n")
    for line in fifty:
        file_output.write('{0:>25} {1:>5.1f}\n'.format(line[0].upper(),line[1]))

    file_output.write("[60-70mm]\n")
    for line in sixty:
        file_output.write('{0:>25} {1:>5.1f}\n'.format(line[0].upper(),line[1]))

    file_output.write("[70-80mm]\n")
    for line in seventy:
        file_output.write('{0:>25} {1:>5.1f}\n'.format(line[0].upper(),line[1]))

    file_output.write("[80-90mm]\n")
    for line in eighty:
        file_output.write('{0:>25} {1:>5.1f}\n'.format(line[0].upper(),line[1]))

    file_output.write("[90-100mm]\n")
    for line in ninety:
        file_output.write('{0:>25} {1:>5.1f}\n'.format(line[0].upper(),line[1]))
    file_output.close()

warmup2()