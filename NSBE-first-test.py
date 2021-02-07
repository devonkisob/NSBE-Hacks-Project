'''
Project Name: NSBE Investors
Authors: Owen Stephenson, Kyle Clahar
Date: 06.02.2021
'''

def wrong_input():
    '''
    () -> none
    This function tells the user that they've inputed an invalid value.
    '''
    return str('* Sorry, that wont work. State your answer again.')

def get_suggested_principal():
    '''
    () -> float
    Inputs the user's yearly income, only accepts numeric value for the income. Based on this income a suggested investment amount is generate.
    '''
    print('* Please state your yearly income (CAD$)')
    while True:
        yincome = input()
        if (yincome.isnumeric()) == True:
            yincome = float(yincome)
            print('* Thank you')
            break
        elif (yincome.isnumeric()) != True:
            print(wrong_input())
            continue
    suggested_principal = float(0)
    if yincome < 30000:
        suggested_principal = yincome * 0.05
    elif yincome >= 30000 and yincome < 50000:
        suggested_principal = yincome * 0.1
    elif yincome >= 50000 and yincome < 70000:
        suggested_principal = yincome * 0.15
    elif yincome >= 70000 and yincome < 100000:
        suggested_principal = yincome * 0.17
    elif yincome >= 100000:
        suggested_principal = yincome * 0.2
    return suggested_principal

def principal_investment_choice(suggested_principal):
    '''
    (float) -> float
    This function suggests the generated investment amount but also allows the user to enter a custom amount to invest. It only accepts certain boolean inputs from the user, either Y/N or A/B. 
    It returns the principal investment, weither it be a custom amount or the suggested amount.
    '''
    while True:
        print("* Do you know how much you want your principal investment to be?")
        print("* State [Y] for yes or [N] for no.")
        know_P = input()
        if know_P == ('Y'):
            print('* How much would you like to invest? (CAD$)')
            while True:
                principal = input()
                if (principal.isnumeric()) == True:
                    principal = float(principal)
                    if principal > 1000000:
                        print('* Too high, maximum principal investment is $1 million')
                        continue                    
                    print("* Thank you")
                    break
                elif (principal.isnumeric()) != True:
                    print(wrong_input())
                    continue
            break
            
        elif know_P == ('N'):
            while True:
                print("* Your suggested principal investment is",int(suggested_principal),'$')
                print("* Would you like to use your suggested principal investment, or choose your own investment value?")
                print("* State [A] for suggested principal investment, or [B] for your own investment value.")                
                confirm_suggested_principal = input()
                if confirm_suggested_principal == ('A'):
                    principal = suggested_principal
                    print("* Thank you")
                    break
                elif confirm_suggested_principal == ('B'):
                    know_P = ('Y')
                    print("* Thank you")
                    break
                else:
                    print(wrong_input())
                    continue
            if confirm_suggested_principal == ('A'):
                break
            elif confirm_suggested_principal == ('B'):
                continue
        else:
            print(wrong_input())
            continue
    return principal

def time_choice():
    print('* How long would you like to invest your money? (in years)')
    while True:
        time = input()       
        if (time.isnumeric()) == True:
            time = float(time)
            if time > 30:
                print('That is too long, maximum investment period is 30 years')
                continue
            print('* Thank you')           
            break
        elif (time.isnumeric()) != True:
            print(wrong_input())
            continue
        
    return time

def interest_rate_calculation(time,principal):
    '''
    (float,str) -> float
    This function uses the time and principal of the investment to calculate the interest rate. The time and principal are directly proportional to the interest rate increases as the time and 
    principle increase.
    '''
    interest = 0.5
    interest += int(principal) * 0.000003
    interest += time * 0.2
    return interest

def caluculate_final_amount(time,principal,interest):
    '''
    (float,float,float) -> float
    This function uses the time, principle and interest rate according to the compound interest formula to calculate the final amount of the investment
    '''
    final_amount = float(0)
    interest += 1
    time = time
    interest = pow(interest,time)
    final_amount = principal * interest
    return final_amount

def main():
    print("*"*40)
    print("* Compound Interest Calculator")
    suggested_principal = get_suggested_principal()
    principal = principal_investment_choice(suggested_principal)
    time = time_choice()
    interest = float(interest_rate_calculation(time,principal)/100)
    print('* Your Interest Rate is', round(interest_rate_calculation(time,principal),2),'%')
    final_amount = caluculate_final_amount(time,principal,interest)
    print('* Once your current investment reaches maturity your final amount will be $', round(final_amount,2))
    print('* You will have profitted $', round(final_amount - principal,2))
    
main()
