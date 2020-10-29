# n=int(input())
# for i in range(n):
#     date,month,year=input().split()
#     if date=="1":
#         if month=="January":
#             print("31 December",int(year)-1)
        
#         elif month=="February":
#             print("31 January",year)

#         elif month=="March":
#             if year%4==0:
#                 if year%100==0:
                    
#if year%400==0:
#                         print("29 February",year)
#                     else:
#                         print("28 February",year)
#                 else:
#                     print("29 February",year)
#             else:
#                 print("28 February",year)
            

#         elif month=="April":
#             print("31 March",year)
        
#         elif month=="May":
#             print("30 April",year)
        
#         elif month=="June":
#             print("31 May",year)
        
#         elif month=="July":
#             print("30 June",year)
        
#         elif month=="August":
#             print("31 July",year)
        
#         elif month=="September":
#             print("31 August",year)
        
#         elif month=="October":
#             print("30 September",year)
        
#         elif month=="November":
#             print("31 October",year)
        
#         elif month=="December":
#             print("30 November",year)
    
#     else:
#         print(int(date)-1,month,year)


"""

n=int(input())
for i in range(n):
    date,month,year=input().split()
    if date=="1":
        if month=="January":
            print("31 December",int(year)-1)
        
        elif month=="February":
            print("31 January",year)

        elif month=="March":
            if int(year)%4==0:
                if int(year)%100==0:
                    
                    if int(year)%400==0:
                        print("29 February",year)
                    else:
                        print("28 February",year)
                else:
                    print("29 February",year)
            else:
                print("28 February",year)
            

        elif month=="April":
            print("31 March",year)
        
        elif month=="May":
            print("30 April",year)
        
        elif month=="June":
            print("31 May",year)
        
        elif month=="July":
            print("30 June",year)
        
        elif month=="August":
            print("31 July",year)
        
        elif month=="September":
            print("31 August",year)
        
        elif month=="October":
            print("30 September",year)
        
        elif month=="November":
            print("31 October",year)
        
        elif month=="December":
            print("30 November",year)
    
    else:
        print(int(date)-1,month,year)
        
"""
def checker(year): 
    if (year % 4) == 0: 
        if (year % 100) == 0: 
            if (year % 400) == 0: 
                return True
            else: 
                return False
        else: 
             return True
    else: 
        return False
t=int(input())
while t:
    t-=1
    d,m,y=map(str,input().split())
    d=int(d)
    y=int(y)
    month=["January", "February", "March", "April", "May", "June", "July", "August", "September","October","November","December"]
    if d==1 and m=="January":
        print("31 December",y-1)
    elif d==1 and m=="March":
        if checker(y)==True:
            print("29 February",y)
        else:
            print("28 February",y)
    elif d==1 and m=="August":
        print("31 July",y)
    elif d==1:
        if m=="May" or m=="July" or m=="October" or m=="December":
            for i in range(12):
                if month[i]==m:
                    print("30",month[i-1],y)
                    break
        else:
            for i in range(12):
                if month[i]==m:
                    print("31",month[i-1],y)
    else:
        print(d-1,m,y)
                
