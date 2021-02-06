def interest_rate_calculation(term,principal):
    interest = 0.5
    interest += principal * 0.000003
    interest += term / 12 * 0.4
    return interest
def main():
    principal = float(input('principal: '))
    term = float(input('term: '))
    print('Your Interest Rate is', round(interest_rate_calculation(term,principal),2),'%')
main()
