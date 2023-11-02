bill = input("Welcome to the tip calculator! What was the total bill? ")
tip_amt = float(input("What percent tip would you like to give? "))
num_ppl = input("How many people to split the bill? ")
answer = float(float(bill)/float(num_ppl) * ((float(tip_amt)/100.00)+1.00))
y = format(answer, '.2f')

print("Each person should pay: " + " " + "$" +str(y))