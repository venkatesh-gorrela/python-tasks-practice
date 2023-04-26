from datetime import datetime

name=input("Enter your name:")
#List of items
lists='''
Rice    Rs 20/kg
sugar   Rs 30/kg
Salt    Rs 20/Kg
Oil     Rs 80/liter
paneer  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/each
Colgate Rs 85/each
'''
#declaration
Price=0
Pricelist=[]
Totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':20,
'sugar':30,
'salt':20,
'oil':80,
'paneer':110,'maggi':50,'boost':90,'colgate':85}
option=int(input("for list of items press 1"))
if option==1:
    print(lists)
    for i in range(len(items)):
        inp1=int(input("if you want to buy press 1 or 2 for exit:"))
        if inp1==2:
            break
        if inp1==1:
            item=input("Enter your item:")
            quantity=int(input("Enter quantity:"))
            if item in items.keys():
                price=quantity*(items[item])
                Pricelist.append((item,quantity,items,price))
                Totalprice+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                gst=(Totalprice*1)/100
                finalamount=gst+Totalprice
            else:
                print("sorry you entered item is not available")
        else:
            print("you entered wrong number")
        inp=input("can i bill the items yes r no:")
        if inp=='yes':
            pass
            if finalamount!=0:

                print(25*"<","GVL--MART",25*">")
                print(23*" ","RAJAHMUNDRY")
                print("Name:->",name,30*" ","Date:->",datetime.now())
                print(75*"_")
                print("sno",8*" ",'items',4*" ",'quantity',5*" ",'price')
                for i in range(len(Pricelist)):
                    print(i,7*' ',4*' ',ilist[i],4*' ',qlist[i],9*" ",plist[i])
                    print(75*"_")
                    print(50*" ",'Totalamount:->','Rs',Totalprice)
                    print("get amount",52*" ",gst)
                    print(50*" ",'finalamount:','Rs',finalamount)
                    print(75*"_")

                    print(50*" ",'Thanks for visiting GVL--MART')
                    


