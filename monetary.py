def init_money():
    print("Initialization of denominations  \n")
    coins={0.01:'1c',
          0.05:'5c',
          0.1:'10c',
          0.25:'quarter',
          0.5:'50c',
          1.0:'$1'}
    
    bills={1:'1 dollar bill',
                2:'2 dollars bill',
                5:'5 dollars bill',
                10:'10 dollars bill',
                20:'20 dollars bill',
                50:'50 dollars bill',
                100:'100 dollars bill'
    }
    return coins, bills
        
def search_max_under_amount(amount, money):
    optimized_choice=max([x for x in money.keys() if x<=amount])
    return optimized_choice

def decompose(amount, coins, bills):
    amount=round(amount, 2)
    if amount==0:
        return
    elif 0.01<=amount<=1:
        max_coin=search_max_under_amount(amount,coins)
        part, remainder= divmod(amount, max_coin)
        print(str(part) + " coin(s) of "+ coins[max_coin])
    else:
        max_bill=search_max_under_amount(amount,bills)
        part, remainder= divmod(amount, max_bill)
        print(str(part) + " bill(s) of "+ bills[max_bill])
    decompose(remainder, coins, bills)

def make_change(charged, received, coins, bills):
    if received<charged:
        print("Missing money.Error \n")
        return
    elif charged == received:
        print("Received the exact amount needed. No change \n")
    else:        
        change=received-charged
        print("Your change should be "+ str(change)+ " dollars")
        decompose(change, coins, bills)


def compute_change(charged, received):
    '''
    print("Initializing the currency system \n")
    print("Enter the denominations for BILLS separated by a semicolon. For example 1 or 100.\n")
    bills=str(input())
    bill_list=bills.split(';')
    print(bill_list)
    print("Enter the denominations for COINS separated by a semicolon. For example 1c or $1.\n")   
    coins=str(input())
    coin_list=coins.split(';')
    print(coin_list)
'''
    coins, bills= init_money()
    make_change(charged, received, coins, bills)
