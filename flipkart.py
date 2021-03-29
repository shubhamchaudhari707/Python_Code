import sys
class customer:
    appname='Flipkart'
    def __init__(self,name):
        self.name=name

print('welcomr to ',customer.appname)
name=input('Enter your name ')
c=customer(name)
while (True):
    print('m-mobiles\nf-freeze\nl-led\ne-exit\n**************************')
    option=input('choice your option \n')
    if option=='m' or option=='M':
        print('a-motortola:12000\nb-nokia:15000\nc-samsung:17000')
        option1=input('enter choose \n')
        if option1 =='a':
            print('payment option is now :')
            amt=int(input('enter the amount motorola : '))
            if amt >=12000:
                print('* Sucessfuly payment option * ')
                print('*****  congrates you buy this product  *****')
            elif amt<1201:
                print('please 12000 paid only ')
            #else:
               # print(' * Thanks for tip *')
                #print('*****  congrates you buy this product  *****')
            sys.exit()
        elif option1 =='b':
            print('payment option is now :')
            amt = int(input('enter the amount nokia : '))
            if amt >=15000:
                print('* Sucessfuly payment option * ')
                print('*****  congrates you buy this product  *****')
            elif amt<1501:
                print('please 15000 paid only ')
            #else:
               # print(' * Thanks for tip *')
               # print('*****  congrates you buy this product  *****')
            sys.exit()
        elif option1 =='c':
            print('payment option is now ')
            amt = int(input('enter the amount samsung : '))


            if amt >=17000:
                print('* Sucessfuly payment option * ')
                print('*****  congrates you buy this product  *****')
            elif amt<1701:
                print('please 17000 paid only ')
            #else:
              #  print(' * Thanks for tip *')

            sys.exit()
        else:
            print('please valid option !!!!!!\n----------------------')

    elif option == 'f' or option == 'F':
        print('a-samsung:12000\nb-haier:15000\nc-Lg:17000')
        option1 = input('enter choose \n')
        if option1 == 'a':
            print('payment option is now :')
            amt = int(input('enter the amount samsung : '))
            if amt >= 12000:
                print('* Sucessfuly payment option * ')
                print('*****  congrates you buy this product  *****')
            elif amt < 1201:
                print('please 12000 paid only ')
           # else:
            #    print(' * Thanks for tip *')
             #   print('*****  congrates you buy this product  *****')
            sys.exit()
        elif option1 == 'b':
            print('payment option is now :')
            amt = int(input('enter the amount haier : '))
            if amt >= 15000:
                print('* Sucessfuly payment option * ')
                print('*****  congrates you buy this product  *****')
            elif amt < 1501:
                print('please 15000 paid only ')
            #else:
             #   print(' * Thanks for tip *')
              #  print('*****  congrates you buy this product  *****')
            sys.exit()
        elif option1 == 'c':
            print('payment option is now ')
            amt = int(input('enter the amount Lg : '))

            if amt >= 17000:
                print('* Sucessfuly payment option * ')
                print('*****  congrates you buy this product  *****')
            elif amt < 1701:
                print('please 17000 paid only ')
            #else:
             #   print(' * Thanks for tip *')

            sys.exit()
        else:
            print('please valid option !!!!!!\n------------------')

    elif option == 'l' or option == 'L':
        print('a-videocon:12000\nb-sharp:15000\nc-sony:17000')
        option1 = input('enter choose \n')
        if option1 == 'a':
            print('payment option is now :')
            amt = int(input('enter the amount videocon : '))
            if amt >= 12000:
                print('* Sucessfuly payment option * ')
                print('*****  congrates you buy this product  *****')
            elif amt < 1201:
                print('please 12000 paid only ')
           # else:
            #    print(' * Thanks for tip *')
             #   print('*****  congrates you buy this product  *****')
            sys.exit()
        elif option1 == 'b':
            print('payment option is now :')
            amt = int(input('enter the amount sharp : '))
            if amt >= 15000:
                print('* Sucessfuly payment option * ')
                print('*****  congrates you buy this product  *****')
            elif amt < 1501:
                print('please 15000 paid only ')
            #else:
             #   print(' * Thanks for tip *')
              #  print('*****  congrates you buy this product  *****')
            sys.exit()
        elif option1 == 'c':
            print('payment option is now ')
            amt = int(input('enter the amount sony : '))

            if amt >= 17000:
                print('* Sucessfuly payment option * ')
                print('*****  congrates you buy this product  *****')
            elif amt < 1701:
                print('please 17000 paid only ')
          #  else:
           #     print(' * Thanks for tip *')

            sys.exit()
        else:
            print('please valid option !!!!!!\n------------------')


    elif option=='e' or option=='E':

        print('Yhanks for flipkart shoping ')
        print('*'*50)
        sys.exit()
    else:
        print('please valid option !!!!!!')
        print('*'*50)







































