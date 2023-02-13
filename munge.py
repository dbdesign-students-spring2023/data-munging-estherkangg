# Place code below to do the munging part of this assignment.
def munge():
    f = open('data/nasa_data.txt', 'r') # open the file in read mode
    n = open('data/clean_data.csv', 'w') #open new csv file to write to

    lines = f.readlines()
    count = 0

    for line in lines: #for every line in the data file
        line = line.strip() 
        if line == '': #skip lines that start with empty character
            continue
        if line.startswith('Year'):
            if count == 0: #keep first header line
                count = 1
                first = line.split() 
                first.pop() #delete last column
                n.write(','.join(first))
                n.write("\n")
            else: #skip the rest of the headers
                continue
        if line[0].isdigit(): 
            parts = line.split() 
            parts.pop() #delete last column

            for i in range(1, len(parts)):
                if "*" in parts[i]: 
                    continue
                anomaly = float(parts[i])
                anomaly_f = anomaly/100*1.8 #convert celsius to fahrenheit 
                parts[i] =format(anomaly_f, '.1f')
            n.write(','.join(parts))
            n.write("\n")

    f.close()
    n.close()

munge()