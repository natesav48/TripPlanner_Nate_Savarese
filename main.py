# 09/06/2023 Nate Savarese
# Trip Planner
def intro_data ():
    global Firstname
    global Lastname
    global Destination
    global Traveldays
    global CurrencySymbol
    global Budget
    global conversion
    print ("hello! Welcome to my trip planner program")


    Firstname = input ("please state your first name")
    Lastname = input ("please state your last name")

    print ("Hi"+ Firstname + Lastname + " I hope your having a wonderful day!")

    Destination = input ("Where are you Headed?")
    print ("That sounds like a great idea! I love" + Destination)

    Traveldays = input ("How many days will you be staying in" + Destination+"?")
    Budget = input ("Whats the total budget, in USD, for the trip?")
    CurrencySymbol = input ("what is the currency symbol for your destination?")
    conversion = float(input ("what is the conversion rate between USD to" + CurrencySymbol + "?"))
#intro_data()

def Converters():
    #time conversions done here
    Hourstraveled = int(Traveldays) * 24
    MinsTraveled = int(Hourstraveled) * 60
    SecondsTraveled = int(MinsTraveled) * 60
    print ("Your total travel time is" , Hourstraveled , "Hours" , MinsTraveled , "Minutes" , SecondsTraveled , "Seconds.")


    #budget converion
    IntTraveldays = int(Traveldays)
    fltbudget = float(Budget)
    Dailybudget = (fltbudget) / (IntTraveldays)
    roundeddailybudget = round(Dailybudget,2)
    print ("Your total budget for the trip is" , Budget)
    print ("Your budget per day is" , (roundeddailybudget))

    #Budget in destination country
    destinationcurrency = fltbudget * conversion
    print (destinationcurrency,CurrencySymbol, "This is the conversion rate from USD to",(CurrencySymbol))
#Converters()

def valid_check():
    try:
        intro_data()
        Converters()
    except:
        print ("make sure input is in proper format")
        valid_check()
valid_check()

def Time_Difference():
    TimeDifference = int(input("Please provide the time difference. If your destinations time zone is behind, please provide a negative number"))
    TimeChange = (TimeDifference + 12) % 24
    print ("When it is 12 O'clock at home, it is" , TimeChange , ":00 in your destination")
Time_Difference()

def Country_Area():
    CountryArea = input ("Please enter the size of your destination in square kilometers")
    try:
        CountryArea = float(CountryArea)
    except:
        print("Please make sure it is in proper format")
        Country_Area()
    roundedcountryarea = CountryArea * 0.386102
    print ("The area of travel for your country is" , int(roundedcountryarea) , "square miles")
Country_Area()

