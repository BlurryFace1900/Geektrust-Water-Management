cmd = input("::")

corp = 1
bore = 1.5
guest = 0

while('BILL' not in cmd):
    if('ALLOT_WATER' in cmd):
        appt_type, ratio = cmd.split(" ")[1], cmd.split(" ")[-1]
        print(appt_type,ratio)
    elif('ADD_GUESTS' in cmd):
        guest += int(cmd.split(" ")[-1])
        print(guest)
    cmd = input("::")

fixed_amount =  900 if appt_type == '2' else 1500
units = fixed_amount / sum(list(map(int,ratio.split(":"))))
print(units, type(ratio.split(":")[0]), ratio.split(":")[0])
fixed_cost = units*int(ratio.split(":")[0])*corp + units*int(ratio.split(":")[1])*bore
print(fixed_cost)


variable_amount = guest*300
if(variable_amount < 501):
    variable_cost = variable_amount*2
elif(variable_amount > 500 and variable_amount < 1501):
    variable_cost = 500*2 + (variable_amount - 500)*3
elif(variable_amount > 1500 and variable_amount < 3001):
    variable_cost = 500*2 + 1000*3 + (variable_amount - 1500)*5
else:
    variable_cost = 500*2 + 1000*3 + 1500*5 + (variable_amount - 3000)*8

print(variable_cost)

print("Total = ", round(fixed_cost+variable_cost))
