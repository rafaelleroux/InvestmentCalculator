#function to calculate shares for self-investment
def self_calc_buy(stock_price, dividend_yield):
    return stock_price / dividend_yield

#function to calculate investment total to self buy
def invest_amt_calc(shares, stock_price):
    return shares * stock_price

#function to calculate shares for a certain amount in returns
def shares_for_returns(return_amount, dividend_yield):
    return return_amount / dividend_yield

#function to determine the investment total of shares for returns
def invest_total_calc(return_shares, stock_price):
    return return_shares * stock_price

'''
variables for stock name, stock price, dividend yield, shares, return_amount,
return shares
'''

try:
    stock_name = input("Enter Stock Name: ")
    stock_price = float(input("Enter Stock Price: "))
    dividend_yield = float(input("Enter Dividend per Share: "))
    shares = self_calc_buy(stock_price, dividend_yield)
    invest_amt = invest_amt_calc(shares, stock_price)


    print(stock_name)
    print(stock_price)
    print(dividend_yield)
    print("# of shares to self buy: " + str(shares))
    print("Invest amount: $" + str(invest_amt))
    return_amount = float(input("How much would you like to make per off of dividends?: "))
    return_shares = shares_for_returns(return_amount, dividend_yield)
    return_invest_amt = invest_total_calc(return_shares, stock_price)
    frequency = input("Does this pay monthly or quarterly?(M/Q): ")
    if frequency == "M" or frequency == "m":
        print("To make " + str(return_amount) + " a month, you'll need " + str(return_shares) + " shares.")
        print("You'll need to invest $" + str(return_invest_amt) + " to own that many shares!")
    elif frequency == "Q" or frequency == "q":
        print("To make " + str(return_amount) + " a month, you'll need " + str(return_shares * 3) + " shares.")
        print("You'll need to invest $" + str(return_invest_amt * 3) + " to own that many shares!")
    else:
        print("Choose a correct letter please")

except ValueError:
    print("Invalid Input: Needs Numbers")

except ZeroDivisionError:
    print("Invalid Number: Can't divide by Zero")

