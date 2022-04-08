card_date=int(input('enter your card here (year):'))
if card_date<=2021:
    print('card is expire please renew it through branch thnlks for visiting')
else:
    print('''
    please choose following option:-
    1) saving acount = s
    2) changre password = c
    3) trasition  = t
    ''')
a = input()
if a=='s':
    amount=int(input('Enter amount: '))
    password=int(input('Enter your password, '))
    if amount >= 5000:
        print('sorry amount not avilable ,start again to proceed.... ')
    else:
        print('successfully resived',amount)    
elif a=='t':
    amount=int(input('Enter amount to trasaction: '))
    trasaction_adress=input('Enter hrer trasaction Acount Number ')
    branch=input('branch: ')
    code=input('Ifc code :')
    password=int(input('Enter your password, '))
    print('trasaction successfuly completed',amount,'Rs at Account',trasaction_adress)
elif a=='c':
    mobile=int(input('Enter your monbile number: '))
    otp=int(input('Enter your otp here  :'))
    new=int(input('Enter New Password: '))
    con=int(input('Confirm your Password: '))
    print('your password changed Successfully: ')
else:
    print('start again to proceed....')




    
           
 