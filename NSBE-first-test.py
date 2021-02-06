'''
Project Name: NSBE Project
Authors: Owen Stephenson, Kyle Clahar
Date: 06.02.2021
'''

def get_suggested_principal():
    print('Please state your yearly income (CAD$)')
    yincome = float(input())
    suggested_principal = float(0)
    if yincome <= 50000:
        suggested_principal = yincome * 0.1
    elif yincome > 50000:
        suggested_principal = yincome * 0.15
    return suggested_principal

def interest_rate_calculation(term,principal):
    interest = 0.5
    interest += principal * 0.000003
    interest += term / 12 * 0.4
    return interest

def caluculate_final_amount(term,principal,interest):
    final_amount = float(0)
    interest += 1
    term = term/12
    interest = pow(interest,term)
    final_amount = principal * interest
    return final_amount
    
def main():
    print("*"*20)
    print("Compound Interest Calculator")
    print("Your suggested principal investment is",int(get_suggested_principal()),'$')
    print('How much would you like to invest? (CAD$)')
    principal = float(input())
    print('How long would you like to invest your money? (in months)')
    term = float(input())
    interest = float(interest_rate_calculation(term,principal)/100)
    print('Your Interest Rate is', round(interest_rate_calculation(term,principal),2),'%')
    final_amount = caluculate_final_amount(term,principal,interest)
    print('Once your investment reach maturity your final amount will be', round(final_amount,2),'$')
main()
