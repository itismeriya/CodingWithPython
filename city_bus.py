import math

#get Fare function to calculate the function
def getFare(source,destination):

    route=[ ["TH","GA","IC","HA","TE","LU","NI","CA"] , [800,600,750,900,1400,1200,1100,1500] ]

    #Initial fare
    fare=0.0

    if not ( source in route[0] and destination in route[0] ):
        print("INVALID INPUT")
        exit()

    if route[0].index(source) < route[0].index(destination):
        for i in range ( route[0].index(source) , route[0].index(destination) ):
        fare+=route[1][i]

    elif route[0].index(source) > route[0].index(destination):
        for i in range ( route[0].index(source)+1 , len(route[0]) ):
        fare+=route[1][i]  
    
        for i in range ( 0 , route[0].index(destination)+1 ):
        fare+=route[1][i] 

    return float( math.ceil(fare*0.005) )

#taking user input
source = input("Enter source : ")
destination = input("Enter destination : ")
fare = getFare( source , destination )

if fare == 0:
    print("INVALID INPUT")
else:
    print(fare)

