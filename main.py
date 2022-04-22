#This program should be run with font style as "Courier New"
import pickle
from datetime import datetime

#Main Page
def main_page():
    print("\n(Please run the program with font style as 'Courier New')\n")
    print((" " * 25),"---------------------------------------------------")
    print((" " * 25),"                  PARADISE HOTELS                  ")
    print((" " * 25),"---------------------------------------------------")
    print((" " * 25),"1. Manage Rooms")
    print((" " * 25),"2. Manage Customers")
    print((" " * 25),"0. Exit")
    print((" " * 25),"Enter your choice: ", end='')
    choice = input()
    if choice == "1":
        room_menu()
    elif choice == "2":
        customer_menu()
    elif choice == "0":
        print((" "*25),"Thank You")
    else:
        print("Wrong Choice")
        menu()

#File Handling
def add(data,filename):
        file = open(filename, "ab")
        pickle.dump(data, file)
        file.close()

def read(filename):
        data = []
        try:
            file = open(filename, "rb")
        except FileNotFoundError:
            return data
        while True:
            try:
                i = pickle.load(file)
                data.append(i)
            except EOFError:
                break
        file.close()
        return data

def edit(data,filename):
        file = open(filename, "wb")
        for i in data:
            pickle.dump(i, file)
        file.close()

#Printing Functions

def print_rooms(sno_room,room_no, floor,beds,avlb):
        print(sno_room,end=" "*7)
        q=len(str(room_no))
        print(room_no,end=" "*(19-q))
        w=len(str(floor))
        print(floor,end=" "*(13-w))
        e=len(str(beds))
        print(beds,end=" "*(12-e))
        r=len(str(avlb))
        print(avlb)

def print_top_room():
    print("-"*102)
    print("S No.",end="   ")
    print("Room Number","Floor","Beds","Available",sep=" "*8)
    print("-"*102)
    
def print_top_customers():
    print("-"*102)
    print("S No.",end="   ")
    print("Name","Address","Phone","Room No.","Entry Date",sep=" "*7,end=" "*8)
    print("Checkout Date")
    print("-"*102)

def print_customers(sno_customer, name, address, phone, room_no, entry_date, checkout_date):
        print(sno_customer,end=" "*7)
        q=len(str(name))
        print(name,end=" "*(11-q))
        w=len(str(address))
        print(address,end=" "*(14-w))
        e=len(str(phone))
        print(phone,end=" "*(12-e))
        y=len(str(room_no))
        print(room_no,end=" "*(11-y))
        r=len(str(entry_date.strftime("%I:%M %p,%d-%m-%Y")))
        print(entry_date.strftime("%I:%M %p,%d-%m-%Y"),end=" "*(22-r))
        if checkout_date is not None:
            t=len(str(checkout_date.strftime("%I:%M %p,%d-%m-%Y")))
            print(checkout_date.strftime("%I:%M %p,%d-%m-%Y"))
        else:
            print(checkout_date)

#Some Useful Functions

def new_room(sno_room):
    room_no = int(input("Enter the room no: "))
    floor = input("Enter the floor (Ex. ground, first etc.): ")
    beds = int(input("Enter number of beds: "))
    avlb = True
    return [sno_room, room_no, floor, beds, avlb]
              
def new_customer(sno_customer, room_no):
    name = input("Enter the name: ")
    address = input("Enter the address: ")
    phone = int(input("Enter the phone number: "))
    entry_date = datetime.now()
    return [sno_customer, name, address, phone, room_no, entry_date, None]

def change_availability(room_no, available):
    rooms = read("rooms.dat")
    position = -1
    for room in rooms:
        position += 1
        if room_no == room[1]:
            break
    room = rooms[position]
    room[4] = available
    edit(rooms,"rooms.dat")
    print("Room status updated")

def rooms_found_position_by_room_no():
    rooms = read("rooms.dat")
    found = False
    position = -1
    if len(rooms) == 0:
        print("No rooms found")
    else:
        room_no = int(input("Enter the room no: "))
        for room in rooms:
            position += 1
            if room_no == room[1]:
                found = True
                break
        if not found:
            print("There is no room with room number ",room_no)
        else:
            print_top_room()
            print_rooms(rooms[position][0],rooms[position][1],rooms[position][2],rooms[position][3],rooms[position][4])
    return rooms, found, position

def customers_found_position_by_room():
    customers = read("customers.dat")
    found = False
    position = -1
    if len(customers) == 0:
        print("No customer found")
    else:
        room_no = int(input("Enter the room no: "))
        for customer in customers:
            position += 1
            if room_no == customer[4] and customer[6] is None:
                found = True
                break
        if not found:
            print("Room not occupied")
        else:
            print_top_customers()
            print_customers(customers[position][0],customers[position][1],customers[position][2],customers[position][3],customers[position][4],customers[position][5],customers[position][6])
    return customers, found, position

def customers_found_position_by_phone():
    customers = read("customers.dat")
    found=False
    position=-1
    if len(customers) == 0:
        print("No room occupied")
    else:
        phone = int(input("Enter the phone number: "))
        for customer in customers:
            position+=1
            if phone == customer[3]:
                found=True
                break
        if not found:
            print("No customer has the entered phone number")
        else:
            print_top_customers()
            print_customers(customers[position][0],customers[position][1],customers[position][2],customers[position][3],customers[position][4],customers[position][5],customers[position][6])
    return customers,found,position

def menu():
    print("-"*100)
    cc=input("Wish to continue?(y/n): ")
    if cc.lower()=="y":
        print("1. Manage Rooms")
        print("2. Manage Customers")
        print("0. Exit")
        print("Enter your choice: ", end='')
        choice = input()
        if choice == "1":
            room_menu()
        elif choice == "2":
            customer_menu()
        elif choice == "0":
            print("Thank You")
    elif cc.lower()=="n":
        print("Thank You")
    else:
        print("Wrong Choice")
        menu()

#Room Menu Begins

def add_room():
    rooms = read("rooms.dat")
    if len(rooms) == 0:
        sno_room = 1
    else:
        sno_room = len(rooms)+ 1
    room = new_room(sno_room)
    add(room,"rooms.dat")
    print("Room added")
    menu()

def print_room_by_no():
    rooms = read("rooms.dat")
    if len(rooms) == 0:
        print("No rooms found")
    else:
        room_no = int(input("Enter the room no: "))
        for room in rooms:
            if room_no == room[1]:
                break
        if not found:
            print("There is no room with room number ",room_no)
        else:
            print_top_room()
            print_rooms(rooms[position][0],rooms[position][1],rooms[position][2],rooms[position][3],rooms[position][4])
    menu()

def print_room_by_beds():
    rooms = read("rooms.dat")
    results = []
    if len(rooms) == 0:
        print("No rooms found")
    else:
        beds = int(input("Enter the number of beds in the room: "))
        for room in rooms:
            if beds == room[3]:
                results.append(room)
        if len(results) == 0:
            print("There is no room with ",beds,"number of beds")
        else:
            print(len(results), " rooms have",beds,"beds")
            print_top_room()
            for room in results:
                print_rooms(room[0],room[1],room[2],room[3],room[4])
    menu()

def modify_room_details():
    rooms, found, position = rooms_found_position_by_room_no()
    if found:
        room = rooms[position]
        print("Input new values (leave blank to keep previous value)")
        room_no = input("Enter new room no: ")
        if len(room_no) > 0:
            room[1] = int(room_no)
        floor = input("Enter new floor: ")
        if len(floor) > 0:
            room[2] = floor
        beds = input("Enter number of beds: ")
        if len(beds) > 0:
            room[3] = int(beds)
        edit(rooms,"rooms.dat")
        print("Room's details modified")
    menu()

def delete_room():
    rooms, found, position = rooms_found_position_by_room_no()
    if found:
        room = rooms[position]
        confirm = input("Delete this room ? (Y/N) : ")
        if confirm.lower() == 'y':
            rooms.remove(room)
            edit(rooms,"rooms.dat")
            print("Room deleted")
        else:
            print("Operation Cancelled")
    menu()

def view_all_rooms():
    rooms = read("rooms.dat")
    if len(rooms) == 0:
        print("No rooms found")
    print_top_room()
    for room in rooms:
        print_rooms(room[0],room[1],room[2],room[3],room[4])
    menu()

def room_menu():
    print()
    print("---------------------------------------------------")
    print("                     ROOM MENU                     ")
    print("---------------------------------------------------")
    print()

    print("1. Add new room")
    print("2. Print room details by room no")
    print("3. Find available rooms by number of beds")
    print("4. Modify Room details")
    print("5. Delete room")
    print("6. View all rooms")
    print("0. Go Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_room()
    elif choice =="2":
        print_room_by_no()
    elif choice == "3":
        print_room_by_beds()
    elif choice == "4":
        modify_room_details()
    elif choice == "5":
        delete_room()
    elif choice == "6":
        view_all_rooms()
    elif choice == "0":
        main_page()
    else:
        print("Invalid choice")
        menu()

#Customer Menu Begins

def add_customer():
    rooms, found, position = rooms_found_position_by_room_no()
    if found:
        room_no = rooms[position][1]
        customers = read("customers.dat")
        if len(customers) == 0:
            sno_customer= 1
        else:
            sno_customer = len(customers) + 1
        customer = new_customer(sno_customer, room_no)
        confirm = input("Confirm (Y/N): ")
        if confirm.lower() == 'y':
            add(customer,"customers.dat")
            change_availability(room_no, False)
            print("Customer checked in")
        else:
            print("Operation Canceled")
    menu()

def print_customers_by_name():
    customers = read("customers.dat")
    results = []
    if len(customers) == 0:
        print("No room occupied")
    else:
        name = input("Enter the name: ").lower()
        

        for customer in customers:
                if customer[1].lower()==name:
                        results.append(customer)
        if len(results) == 0:
            print("No customer with name",name)
        else:
            print(len(results), " customers have name",name)
            print_top_customers()
            for customer in results:
                print_customers(customer[0],customer[1],customer[2],customer[3],customer[4],customer[5],customer[6])
    menu()

def print_customers_by_phone():
    customers = read("customers.dat")
    found=False
    if len(customers) == 0:
        print("No room occupied")
    else:
        phone = int(input("Enter the phone number: "))
        for customer in customers:
            if phone == customer[3]:
                found=True
                break
        if not found:
            print("No customer has the entered phone number")
        else:
            print_top_customers()
            print_customers(customers[position][0],customers[position][1],customers[position][2],customers[position][3],customers[position][4],customers[position][5],customers[position][6])
    menu()

def print_customers_by_room_no():
    customers = read("customers.dat")
    found=False
    if len(customers) == 0:
        print("No room occupied")
    else:
        room_no = int(input("Enter the room no: "))
        for customer in customers:
            if room_no == customer[4] and customer[6] is None:
                found=True
                break
        if not found:
            print("room",room_no,"is not occupied")
        else:
            print_top_customers()
            print_customers(customers[position][0],customers[position][1],customers[position][2],customers[position][3],customers[position][4],customers[position][5],customers[position][6])
    menu()

def print_customers_by_check_in():
    customers = read("customers.dat")
    if len(customers) == 0:
        print("No room occupied")
    else:
        date = int(input("Enter check in date(Date of the month):"))
        month = int(input("Month: "))
        year = int(input("Year: "))
        check_in = datetime(year, month, date)
        results = []
        for customer in customers:
            if customer[5].date() == check_in.date():
                results.append(customer)
        if len(results) == 0:
            print("No customer checked in on",check_in.strftime("%d-%m-%Y"))
        else:
            print(len(results), " customers checked in on",check_in.strftime("%d-%m-%Y"))
            print_top_customers()
            for customer in results:
                print_customers(customer[0],customer[1],customer[2],customer[3],customer[4],customer[5],customer[6])
    menu()

def print_current_list_of_customers():
    customers = read("customers.dat")
    if len(customers) == 0:
        print("No room occupied")
    else:
        results = []
        for customer in customers:
            if customer[6] is None:
                results.append(customer)
        if len(results) == 0:
            print("No room currently occupied")
        else:
            print(len(results), " customers currently staying")
            print_top_customers()
            for customer in results:
                print_customers(customer[0],customer[1],customer[2],customer[3],customer[4],customer[5],customer[6])
    menu()

def modify_customer_details():
    customers, found, position = customers_found_position_by_phone()
    if found:
        customer = customers[position]
        print("Input new values (leave blank to keep previous value)")
        name = input("Enter new name: ")
        if len(name) > 0:
            customer[1] = name
        address = input("Enter new address: ")
        if len(address) > 0:
            customer[2] = address
        phone = input("Enter new phone number: ")
        if len(phone) > 0:
            customer[3] = int(phone)
        confirm = input("Confirm Edit? (Y/N): ")
        if confirm.lower() == 'y':
            edit(customers,"customers.dat")
            print("Customer details modified successfully")
        else:
            print("Operation Cancelled")
    menu()

def check_out():
    customers, found, position = customers_found_position_by_room()
    if found:
        customer = customers[position]
        customer[6] = datetime.now()
        confirm = input("Confirm checkout? (Y/N): ")
        if confirm.lower() == 'y':
            edit(customers,"customers.dat")
            change_availability(customer[4], True)
        else:
            print("Operation Cancelled")
    menu()

def delete_customer():
    customers, found, position = customers_found_position_by_phone()
    if found:
        confirm = input("Confirm delete?? (Y/N): ")
        if confirm.lower() == 'y':
            customers.pop(position)
            edit(customers,"customers.dat")
            print("Customer record deleted")
        else:
            print("Operation Cancelled")
    menu()

def view_all_customers():
    customers = read("customers.dat")
    if len(customers) == 0:
        print("No room occupied")
    print_top_customers()
    for customer in customers:
        print_customers(customer[0],customer[1],customer[2],customer[3],customer[4],customer[5],customer[6])
    menu()
            
def customer_menu():
    print()
    print("---------------------------------------------------")
    print("                  Customer Menu                    ")
    print("---------------------------------------------------")
    print()
    print("1. New Customer")
    print("2. Show Customer Details by name")
    print("3. Show customer details by phone number")
    print("4. Show customer details by room no")
    print("5. Show customer details by check in date")
    print("6. Show current list of customers")
    print("7. Modify customer Details")
    print("8. Customer checkout")
    print("9. Delete Customer record")
    print("10. View all customers")
    print("0. Go Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_customer()
    elif choice == "2":
        print_customers_by_name()
    elif choice == "3":
        print_customers_by_phone()
    elif choice == "4":
        print_customers_by_room_no()
    elif choice == "5":
        print_customers_by_check_in()
    elif choice == "6":
        print_current_list_of_customers()
    elif choice == "7":
        modify_customer_details()
    elif choice == "8":
        check_out()
    elif choice == "9":
        delete_customer()
    elif choice == "10":
        view_all_customers()
    elif choice == "0":
        main_page()
    else:
        print("Invalid choice")
        menu()

#__name__==__main__
main_page()




    
        
