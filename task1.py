from task_classes1 import *

def create_add():
    n=int(input('enter number of Address to be added:'))
    adr_lst=[]
    for num in range(n):
        add=Address()
        city=str(input("enter name of city:"))
        pin=int(input("enter pin code of city:"))
        add.set_city(city)
        add.set_pin(pin)
        adr_lst.append(add)
    return adr_lst


def create_stu(l):
    new_adr=[]
    stu_list=[]
    for i in l:
        new_adr.append(i.get_pin())
    while True:
        try:
            n=int(input('enter no of Students to be added:'))
            break
        except ValueError as e:
            print(e)
    for i in range(n):
        stu=Student()
        while True:
            try:
                rn1=rn()
                break
            except RollNoInvalid as r:
                print(r)
            except ValueError as e:
                print(e)
        while True:
            try:
                name=nm()
                break
            except NameInvalid as e:
                print(e)
        while True:
            try:
                marks=mks()
                break
            except MarksInvalid as r:
                print(r)
            except ValueError as r:
                print(r)
        print(list(enumerate(new_adr,1)))
        while True:
            a=int(input("enter address key to select:"))
            if a in range(1,len(l)+1):
                add=l[a-1]
                stu.set_add(add)
                break
            else:
                print("Wrong Choice")
        stu.set_rn(rn1)
        stu.set_name(name)
        stu.set_marks(marks)
        stu_list.append(stu)
    return stu_list

def update_add(l):
    new_adr=[]
    add=None
    for i in l:
        new_adr.append(i.get_pin())
    print(list(enumerate(new_adr,1)))
    while True:
        a=int(input("enter address key to select:"))
        if a in range(1,len(l)+1):
            add=l[a-1]
            break
    return add
         
        
        
    




stu_list=[]
adr_list=[]



print("---Menu---\n"\
      "1.Student\n"\
      "2.Address\n"\
      "3.Exit")
while True:
     while True:
          try:
               ch=int(input('enter your choice of Main Menu:'))
               break
          except ValueError as r :
               print(r)
     if ch==1:
         ad=None
         while True:
             
             try:
                 ad=ad_list(adr_list)
                 break
             except AddressInvalid as r:
                 print(r)
                 break
                 
         if ad:
                 
             while True:
                 print("----Menu Student---\n"\
                  "1.Create Student \n"\
                  "2.Update Student\n"\
                  "3.Delete Student\n"\
                  "4.Show Students\n"\
                  "5.Show Student by Marks\n"\
                  "6.exit")
                 while True:
                     try:
                         ch1=int(input('enter your Choice of Student Menu: '))
                         break
                     except ValueError as r:
                         print(r)
                 if ch1==1:
                     
                     stu=create_stu(adr_list)
                     stu_list.extend(stu)
                     print(stu_list)
                     print(stu_list[0].get_add())
                
                 
                     
                    
                 elif ch1 == 2:
                     rn=int(input("enter Roll no of Student to be Updated:"))
                     for i in stu_list:
                         if rn== i.get_rn():
                             i.set_rn(int(input("enter new Roll no:")))
                             i.set_name(input("enter new name: "))
                             i.set_marks(int(input("enter marks:")))
                             add=update_add(adr_list)
                             i.set_add(add)
                             print("data updaed")

                 elif ch1==3:
                     rn=int(input("enter Roll no of student to be deleted:"))
                     for i in stu_list:
                         if rn== i.get_rn():
                             stu_list.remove(i)
                             print("deta deleted")
                         else:
                             print('No roll number check once')
                             
                             
                     else:
                         print('no ROLL NO check once')
                             
                     
                 elif ch1==4:
                     for i in stu_list:
                         print(i.get_rn())
                         print(i.get_name())
                         print(i.get_marks())
                         print(i.get_add())

                 elif ch1==5:
                     new_list1=sorted(stu_list,key=lambda x:x.get_marks(),reverse=True)
                     new_list2=sorted(stu_list,key=lambda x:x.get_marks())
                     print("dessending")
                     for i in new_list1:
                         print(i.get_marks(),i.get_name(),i.get_rn())
                     print("assending")
                     for i in new_list2:
                         print(i.get_marks(),i.get_name(),i.get_rn())

                    
                 elif ch1==6:
                     break
##         else:
##             print("no address to add in student add some addresss")
            
     elif ch==2:
         
         while True:
             print("----Menu Address---\n"\
                  "1.Create Address\n"\
                  "2.Update Address\n"\
                  "3.Delete Address\n"\
                  "4.Show Address\n"\
                  "5.exit")
             
             while True:
                 
                try:
                    ch1=int(input('enter your Choice of Address Menu:'))
                    break
                except ValueError as r:
                    print(r)
             if ch1==1:    
                 add=create_add()
                 adr_list.extend(add)
                 print(adr_list)
                 print(adr_list[0])
                 
                
             elif ch1==2:
                 pin=int(input("enter Pin code of address you Want To Update:"))
                 for i in adr_list:
                    
                     if pin== i.get_pin():
                         i.set_pin(int(input("enter new pin code:")))
                         i.set_city(input("enter new City:"))
                         print(adr_list)
                         print("data updated")
                         break
                 else:
                     print("NO such pin")
                             
                    
                 
                    
             elif ch1 == 3:
                 pin= int(input("enter pin to be deleled:"))
                 for i in adr_list:
                     if pin== i.get_pin():
                         adr_list.remove(i)
                         print("data deleted")
                         break
                         
                 else:
                     print("NO such pin")
                         
                 
             elif ch1==4:
                 for i in adr_list:
                     print(i.get_city())
                     print(i.get_pin())
                     
             elif ch1==5:
                 break                          
     elif ch==3:
         
         break
     else:
         print("no data in address add data in address")
         
            
            
                     
        
            
                    
                
                
        







    
    
            
        
    

