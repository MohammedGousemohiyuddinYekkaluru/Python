# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

cost_price = float(input("Enter cost price : "))
selling_price = float(input("Enter selling price : "))

def is_profit_or_loss(cp, sp):
    if sp > cp:
        return "Profit"
    else:
        return "Loss"

print(is_profit_or_loss(cost_price, selling_price))

# Another way

def check_business_result(cp, sp):
    if sp > cp:
        profit = sp - cp
        return f"Profit! you made {profit}"
    elif cp > sp:
        loss = cp - sp
        return f"Loss! you loss {loss}"
    else:
        return "Break Even! No Profit, No Loss"
    
print(check_business_result(cost_price, selling_price))