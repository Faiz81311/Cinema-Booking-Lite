import csv


def mov(a):
    if a == '1':
        f = 'Joker'
    elif a == '2':
        f = 'Dolittle'
    elif a == '3':
        f = 'The Grudge'
    elif a == '4':
        f = 'The Invisible Man'
    else:
        print("Invalid Input")
    return(f)



def hall(a):
    if a == '1':
        f = 'Hall A'
    elif a == '2':
        f = 'Hall B'
    elif a == '3':
        f = 'Hall C'
    else:
        print("Invalid Input")
    return f



def time(a):
    if a == '1':
        f = '11:00 A.M'
    elif a == '2':
        f = '1:30 P.M'
    elif a == '3':
        f = '4:30 P.M'
    elif a == '4':
        f = '8:00 P.M'
    else:
        print("Invalid Input")
    return f



def seat(a):
    if a == '1':
        f = '2-B'
    elif a == '2':
        f = '3-B'
    elif a == '3':
        f = '8-A'
    elif a == '4':
        f == '3-E'    
    elif a == '5':
        f = '6-H'
    elif a == '6':
        f = '8-F'
    elif a == '7':
        f = '12-D'
    elif a == '8':
        f == '4-F'
    else:
        print("Invalid Input")
    return f






g=open("cinema.csv","w")
r=["Movie","Day And Date","Venue","Time","Seat","ClassType","Snacks"]
l=[]



print("This Is Online Booking for <enter places name> Cinemas")
print("Today We Will Be Showing : Joker Dolittle The Grudge The Invisible Man ")


m = input("Your Choice : ")
print("[1] For Joker")
print("[2] For Dolittle")
print("[3] For The Grudge")
print("[4] For The Invisible Man")
h = mov(m)
l.append(h)


m = input("Enter The Day And Date You Will Come To The Cinema : ") 
l.append(m)


print("Which Venue Would You Like To Take ")
m = input("Your Choice : ")
print("[1] For Hall A")
print("[2] For Hall B")
print("[3] For Hall C")
h = hall(m)
l.append(h)


print("What Time Would You Like To See It By")
m = input("Your Choice : ")
print("[1] For 11:00 A.M Show")
print("[2] For 1:30 P.M Show")
print("[3] For 4:30 P.M Show")
print("[4] For 8:00 P.M Show")
h = time(m)
l.append(h)


print("The Available Seats Are ")
m = input("Your Choice : ")
print("[1] For 2-B")
print("[2] For 3-B")
print("[3] For 8-A")
print("[4] For 3-E")
print("[5] For 6-H")
print("[6] For 8-F")
print("[7] For 12-D")
print("[8] For 4-F")
h = seat(m)
l.append(h)

print("")
m = input("Your Choice : ")
print("[1] for bronze for Rs")



h = classtype(m)
l.append(h)

print("")
m = input("Your Choice : ")
h = Snacks(m)
l.append(h)


k = csv.writer(g)
k.writerow(r)
k.writerow(l)

g.close