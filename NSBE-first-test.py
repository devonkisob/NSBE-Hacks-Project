'''
Project Name: NSBE Project
Authors: Owen Stephenson, Kyle Clahar
Date: 06.02.2021
'''

def wrong_input():
    print('Sorry, that wont work. State your answer again.')

def get_suggested_principal():
    print('Please state your yearly income (CAD$)')
    while True:
        yincome = float(input())
        if (yincome.isnumeric()) == True:
            print('Thank you.')
            break
        elif (yincome.isnumeric()) != True:
            print(wrong_imput)
            continue
    suggested_principal = float(0)
    if yincome < 50000:
        suggested_principal = yincome * 0.1
    elif yincome >= 50000:
        suggested_principal = yincome * 0.15
    return suggested_principal

    ### finalizing user's principal investment
def principal_investment_choice(suggested_principal):
    while True:
        print("Do you know how much you want your principal investment to be?")
        print("State [Y] for yes or [N] for no.")
        know_P = input()
        if know_P == ('Y'):
            print('How much would you like to invest? (CAD$)')
            while True:
                principal = float(input())
                if (principal.isnumeric()) == True:
                    print("Thank you.")
                    break
                elif (principal.isnumeric()) != True:
                    print(wrong_input)
                    continue
                break
            
        elif know_P == ('N'):
            print("Your suggested principal investment is ",int(suggested_principal),'$')
            print("Would you like to use your suggested principal investment, or choose your own investment value?")
            print("State [A] for suggested principal investment, or [B] for your  own investment value.")
            while True:
                confirm_suggested_principal = input()
                if confirm_suggested_principal == ('A'):
                    principal = suggested_principal
                    print("Thank you")
                    break
                elif confirm_suggested_principal == ('B'):
                    know_P = ('Y')
                    print("Thank you")
                    break
                else:
                    print(wrong_input)
                    continue
            if confirm_suggested_principal == ('B'):
                continue
        else:
            print(wrong_input)
            continue
    return principal

def interest_rate_calculation(time,principal):
    interest = 0.5
    interest += int(principal) * 0.000003
    interest += time / 12 * 0.4
    return interest

def caluculate_final_amount(time,principal,interest):
    final_amount = float(0)
    interest += 1
    time = time/12
    interest = pow(interest,time)
    final_amount = principal * interest
    return final_amount

def main():
    print("*"*20)
    print("Compound Interest Calculator")
    suggested_principal = get_suggested_principal()
    principal = principal_investment_choice(suggested_principal)
    print('How long would you like to invest your money? (in months)')
    while True:
        time = float(input())
        if (time.isnumeric()) == True:
            print('Thank you.')
            break
        elif (time.isnumeric()) != True:
            print(wrong_input)
            continue
    interest = float(interest_rate_calculation(time,principal)/100)
    print('Your Interest Rate is', round(interest_rate_calculation(time,principal),2),'%')
    final_amount = caluculate_final_amount(time,principal,interest)
    print('Once your current investment reaches maturity your final amount will be', round(final_amount,2),'$')
    
main()
