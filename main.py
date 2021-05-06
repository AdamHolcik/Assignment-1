#problem 1
first = input('What is your fist name? ') #takes input of the users first name
last = input('What is your last name? ') #takes input of the users last name
print('Your name backwards is',last,first) #gives output of the users last name then first name
#problem 2
num = int(input("please enter a number: "))#takes users input of number
if num == 0: #is true if the inputed number is equal to 0
  print(num, "is 0") #if the if statement is true it prints saying the inputed number is 0
elif num % 2 == 0: #is true of the inputed number is perfectly divisble by 2, meaning it is an even number
  print(num,"is even") #if the if statement is true it prints saying the inputer number is even
else: #finally, if the code reaches here the inputed number is not 0 and it is not divisible by 2 meaning it is an odd number
  print(num, 'is odd') #prints saying the inputed number is odd
#problem 3
day = int(input('please enter a number between 1 and 365: ')) #gets input of a number between 1 and 365 which will then be converted to an exact date
if day <= 31: #Jauary
  print('Today is January', day) #Prints the month as well as the date
elif day <=  59: #Febuary
  print('Today is Febuary', day-31) #Prints the month as well as the date
elif day <= 90: #March
  print('Today is March', day-59) #Prints the month as well as the date
elif day <= 120: #April
  print('Today is April', day-90) #Prints the month as well as the date
elif day <= 151: #May
  print('Today is May', day-120) #Prints the month as well as the date
elif day <= 181: #June
  print('Today is June', day-151) #Prints the month as well as the date
elif day <= 212: #July
  print('Today is July', day-181) #Prints the month as well as the date
elif day <= 243: #August
  print('Today is August', day-212) #Prints the month as well as the date
elif day <= 273: #September
  print('Today is September', day-243) #Prints the month as well as the date
elif day <= 304: #October
  print('Today is October', day-273) #Prints the month as well as the date
elif day <= 334: #November
  print('Today is November', day-304) #Prints the month as well as the date
else: #December
  print('Today is December', day-334) #Prints the month as well as the date
  #Date is found by subracting from the input how many days till the start of that month, the remainder is the exact date in that month
#problem 4
num = 5 #sets variable num to 5
x = 0 # sets variable x to 0, variable x is responsible for making sure that the numbers are displayed properly
for x in range(num,0,-1): #for loop with variable x, first time it is 5, and lowers each consectuive run, untill it reaches 0
    for i in range(x,0,-1): #for loop that prints the desired awnswer, first time x is five,so it runs 5 times, next time it runs 4 times and so on.
      print(i, end='') #prints the actuall numbers, when it runs 5 times it prints all 5 numbers; 54321, when it runs 4 times it prints 4 numbers; 4321, and so on.
    print('') #makes sure that each new line is actually on a new line
#NOTE: I finished this one and number 5 and went to number 6, but after that when I was double checking everything I realised that this one was removeing the highest number each time, and not the lowest (54321, then 4321 instead of 54321 then 5432), I have not been bale to figure out how to swap it around.
#problem 5
num = int(input('please enter a number: ')) #sets variable num to the users input
x = 0 # sets variable x to 0, variable x is responsible for making sure that the numbers are displayed properly
for x in range(num,0,-1): #for loop with variable x, first time it is 5, and lowers each consectuive run, untill it reaches 0
    for i in range(x,0,-1): #for loop that prints the desired awnswer, first time x is five,so it runs 5 times, next time it runs 4 times and so on.
      print(i, end='') #prints the actuall numbers, when it runs 5 times it prints all 5 numbers; 54321, when it runs 4 times it prints 4 numbers; 4321, and so on.
    print('') #makes sure that each new line is actually on a new line
    # The only difference between this code and number 4 is the main controlling variable num is now set to the users input instead of 5, allowing the user to input any number they want, although if the number is too high the code will not function(such as 100), it is recomended to only input numbers less than 10
#problem 6
day = int(input('please enter a number between 1 and 365: ')) #gets input of a number between 1 and 365 which will then be converted to an exact date
if day <= 31: #Jauary
  week = int(day/7) # this code is the same for all months, with just the day having the correct amount of days subtracted from it to get the correct week; it takes the days of the month, and divides it by 7(days in a week), it converts it to an integer because we don't usually say week 2.6, because of this it is allways rounded down, so week 1 would be dispayed as week 0, in the print it is offset by adding 1 to week.
  print('Today is January', day, 'it is week', week+1, 'of the month') #Prints the month as well as the date
elif day <=  59: #Febuary
  week = int((day-31)/7)
  print('Today is Febuary', day-31, 'it is week', week+1, 'of the month') #Prints the month as well as the date
elif day <= 90: #March
  week = int((day-59)/7)
  print('Today is March', day-59, 'it is week', week+1, 'of the month') #Prints the month as well as the date
elif day <= 120: #April
  week = int((day-90)/7)
  print('Today is April', day-90, 'it is week', week+1, 'of the month') #Prints the month as well as the date
elif day <= 151: #May
  week = int((day-120)/7)
  print('Today is May', day-120, 'it is week', week+1, 'of the month') #Prints the month as well as the date
elif day <= 181: #June
  week = int((day-151)/7)
  print('Today is June', day-151, 'it is week', week+1, 'of the month') #Prints the month as well as the date
elif day <= 212: #July
  week = int((day-181)/7)
  print('Today is July', day-181, 'it is week', week+1, 'of the month') #Prints the month as well as the date
elif day <= 243: #August
  week = int((day-212)/7)
  print('Today is August', day-212, 'it is week', week+1, 'of the month') #Prints the month as well as the date
elif day <= 273: #September
  week = int((day-243)/7)
  print('Today is September', day-243, 'it is week', week+1, 'of the month') #Prints the month as well as the date
elif day <= 304: #October
  week = int((day-273)/7)
  print('Today is October', day-273, 'it is week', week+1, 'of the month') #Prints the month as well as the date
elif day <= 334: #November
  week = int((day-304)/7)
  print('Today is November', day-304, 'it is week', week+1, 'of the month') #Prints the month as well as the date
else: #December
  week = int((day-334)/7)
  print('Today is December', day-334, 'it is week', week+1, 'of the month') #Prints the month as well as the date
  #Date is found by subracting from the input how many days till the start of that month, the remainder is the exact date in that month