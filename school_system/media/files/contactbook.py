def welcome():
    entry=int(input("""Welcome to our website.
    >>>Login commands are:1,2,3 or 4<<<
    >>>What would you like to do?<<<
    1.Log in
    2.Sign up
    3.Find available rooms
    4.Book a room
    5.cancel the bookings
    6.Exit
    Enter your entry here(1,2,3 or 4): """ ))
  
    return entry

def log_in():
    details={}
   
    while True:
        entry=welcome()
 # conditions for option entered 
        if entry==1:
          if bool(details)!=False:
            for l,n in details.items():
                print(l,'-->',n)
            else:
                print("put your  details")  
   

        elif entry==2:
            email=input("Please enter your email address") 
            password=input("password required") 
log_in()
                        