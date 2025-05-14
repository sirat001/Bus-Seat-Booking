# Created On 30-April-2023

import random
all_tickets = []

A = ['A1', 'A2', 'A3', 'A4']
B = ['B1', 'B2', 'B3', 'B4']
C = ['C1', 'C2', 'C3', 'C4']
D = ['D1', 'D2', 'D3', 'D4']
seats = [A, B, C, D]

booked_A = [False, False, False, False]
booked_B = [False, False, False, False]
booked_C = [False, False, False, False]
booked_D = [False, False, False, False]
booked_seat = [booked_A, booked_B, booked_C, booked_D]


def status_of_all_seats():
    print('\n\n')
    for i in range(4):
        for j in range(4):
            if booked_seat[i][j] == False:
                print(f'{seats[i][j]} Available', end = "\t\t")
            else:
                print(f'{seats[i][j]} Not Available', end = "\t")
        print()
    print('\n\n')


def available_seats():
    print('\n----------------\nAvailable Seats\n----------------')
    for i in range(4):
        for j in range(4):
            if booked_seat[i][j] == False:
                print(f'{seats[i][j]}', end = " , ")
    print('\n\n')


def status_of_a_seat(x):
    for i in range(4):
        for j in range(4):
            if seats[i][j] == x:
                if booked_seat[i][j] == False:
                    print(f'\n\n{seats[i][j]} is Available\n\n')
                    break
                else:
                    print(f'\n\n{seats[i][j]} is Not Available\n\n')
                    break
    print()




def get_ticket(seat):
    name = input("Enter Passenger name : " )
    tkt_no = name[0] + str((random.randint(0000000, 999999)))
    print(f'\n\n\tDhakChit MiniBus\n----------------------------\nTicket No - {tkt_no}\nPassenger Name - {name}\nSeat No - {seat}\n------------------------------\n\n\n')
    ticket = [tkt_no, name, seat]
    all_tickets.append(ticket)


def book_a_seat():
    status_of_all_seats()
    x = input("Enter seat number : ")
    for i in range(4):
        for j in range(4):
            if seats[i][j] == x:
                if booked_seat[i][j] == False:
                    booked_seat[i][j] = True
                    get_ticket(seats[i][j])
                    break
                else:
                    print(f'\n\n{seats[i][j]} is Already booked.Please Choose another one.\n\n')
                    break
    print()



def cancel_booking(x):
    for i in range(4):
        for j in range(4):
            if seats[i][j] == x:
                if booked_seat[i][j] == True:
                    booked_seat[i][j] = False
                    print("\n\n------------------------------------\nBooking canceled successfully.\n---------------------------------\n\n")
                    for i in range(len(all_tickets)):
                        if all_tickets[i][2] == x:
                            all_tickets.pop(i)
                        break
                elif booked_seat[i][j] == False:
                    print(f"{x} is not booked.\n\n\n")
                    break
    print()
    
    

def show():
    if len(all_tickets) == 0:
        print('\nNo tickets.')
    else:
        print('All tickets\n\n')
        for i in range(len(all_tickets)):
            print(f'{i+1}. ', end = "")
            for j in range(3):
                print(all_tickets[i][j], end = ", ")
            print('\n')
    print()


while True:
    print('\n\nWelcome to Dhakchit Minibus\n---------------------------\n1.Show the status of all 16 seats on the bus.\n2.Show only the available (not booked) seats on the bus.\n3.Print the status of one seat when the seat number is input\n4.Book a seat\n5.Cancel booking of a seat\nPress q for quit.')
    ch = input("Enter your choice : ")
    if ch == 'q' or ch == 'Q':
        break
    elif ch == '1':
        status_of_all_seats()
    elif ch == '2':
        available_seats()
    elif ch == '3':
        x = input('Enter seat number : ')
        status_of_a_seat(x)
    elif ch == '4':
        
        book_a_seat()
    elif ch == '5':
        x = input('Enter seat number : ')
        cancel_booking(x)
    ### For Admin only to print all tickets
    ## Not showing to all
    elif ch == 'Print all' or ch == 'print all':
        show()
