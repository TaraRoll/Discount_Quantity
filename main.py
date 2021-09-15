'''A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.'''

q = int(input("Enter quantity:"))
if(q>10):
  print("YOU CAN GET THE DISCOUNT!!!! YOU'RE COST IS: $",(q*100)*(10/100))
else:
  print("SORRY YOUR COST IS BELOW 1000, SO NO DiSCOUNT :(")



