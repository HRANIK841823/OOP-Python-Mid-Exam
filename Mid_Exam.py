from datetime import date

class Star_Cinema:
    __hall_list=[] # Attributes to store Hall List
    __hall_no=[]    #Attronites to store Hall List
    
    @classmethod
    def entry_hall(cls, hall, hall_no):
        cls.__hall_list.append(hall)
        cls.__hall_no.append(hall_no)
        
    # View Hall Name 
    def view(self,h_no):
        """Method to view hall details"""
        for hall_no,name in zip(Star_Cinema.__hall_no,Star_Cinema.__hall_list):
            if hall_no==h_no:
                print("***************************")
                print(f"  {hall_no} -> {name}  ")
                print("***************************")
        print()
    
    # View Hall list
    def Add_list(self):
        """Method to display list of halls"""
        for hall_no, name in zip(Star_Cinema.__hall_no, Star_Cinema.__hall_list):
            print(f'Hall No : {hall_no} -> {name}', end=" ")  
            print()

class Hall(Star_Cinema):
    def __init__(self,name,rows,cols,hall_no) -> None:
        self.__seats={}     # Dictionary to store seat status
        self.__show_list=[] # List to store show list
        self.__hall_name=name
        self.__rows=rows
        self.__cols=cols
        self._hall_no=hall_no
        Star_Cinema.entry_hall(self.__hall_name, self._hall_no)

    def entry_show(self, id, movie_name, time):
        """Method to add a new Show"""
        show = (id, movie_name, time)
        self.__show_list.append(show)
        key_value = []
        for seat_row in range(self.__rows):
            key_value.append([])
            for seat_col in range(self.__cols):
                set_seat = 0
                key_value[seat_row].append(set_seat)
        self.__seats[id] = key_value
    def book_seats(self, id, seats_list):
        """Method to book seat for a Show"""
        for book_seat in seats_list:
            row, col = book_seat
            if 0 <= row < self.__rows and 0 <= col < self.__cols:
                if self.__seats[id][row][col] == 0:
                    self.__seats[id][row][col] = 1
                    print("\nSeats booked successfully.\n")
                else:
                    print(f"This ({row},{col}) Seat already booked!!")
            else:
                print("Sorry!! Invalid Seats.\n")
                
    def view_show_list(self):
        """Method to view all show list"""
        for show in self.__show_list:
            print("Movie Id No -> ",show[0],"Movie Name -> ", f"*{show[1]}*","Date -> ",f"{date.today()}","Show Time -> ",f"{show[2]}")
            
    def view_available_seats(self, id):
        """Method to view available seats for a show"""
        show_found = False
        for show in self.__show_list:
            if show[0] == id:
                print(f"Available Seats for Movie name: {show[1]} ({show[0]})")
                show_found = True
                break
        if not show_found:
            print("Invalid Movie ID. Please enter a correct Movie ID!!!")
            return
        for i in range(1, self.__rows + 1):
            for j in range(1, self.__cols + 1):
                print(f"Avaiable Seats for This Row,Col ({i}, {j})")
        print("\n")
        print(f"\nUpdate Seats for {self.__show_list[0][2]}\n")
        for key, val in self.__seats.items():
            for value in val:
                print(f"    {value}")

# Initializing cinema halls and shows
hall1 = Hall("Sakib Khan Cineplex", 10, 10, 1)
hall2 = Hall("Dipjol Cineplex", 7, 7, 2)
hall3 = Hall("Jayed Khan Cineplex", 5,5, 3)
hall1.entry_show(101, "12th Fail", "10:00 AM")
hall1.entry_show(102, "3 Idiots", "12:00 PM")
hall1.entry_show(103, "Dilwale", "3:30 PM")
hall2.entry_show(201, "3 Idiots", "11:0 AM")
hall2.entry_show(202, "Ammajan", "3:00 PM")
hall2.entry_show(203, "12th Fail", "8:00 PM")
hall3.entry_show(301, "DJ", "10:30 AM")
hall3.entry_show(302, "12th Fail", "3.00 PM")
hall3.entry_show(303, "Pathan", "4:00 PM")

# Main Function For User
while True:
    print("Option : 1 -> For View All show Today")
    print("Option : 2 -> For check All availabe Seats")
    print("Option : 3 -> For Ticket Booking")
    print("Option : 4 -> For Exit")
    opt = int(input("\nChoose Your Option: "))
    print("\n")
    if opt == 1:
        hall1.Add_list()
        print("\n")
        op = int(input("Please Choose Cinema Hall No: "))
        print("\n")
        if op <= 3:
            if op == 1:
                hall1.view(op)
                print("\n")
                hall1.view_show_list()
                print("\n")
            elif op == 2:
                hall2.view(op)
                print("\n")
                hall2.view_show_list()
                print("\n")
            elif op == 3:
                hall3.view(op)
                print("\n")
                hall3.view_show_list()
                print("\n")
        else:
            print("\nThere is No more Cinema Hall!!\n")
    elif opt == 2:
        hall1.Add_list()
        hall_no = int(input("\nChoose Your Hall No: "))
        if hall_no <= 3:
            if hall_no == 1:
                hall1.view(hall_no)
                print("\nFor this Hall Available Movie!!\n")
                hall1.view_show_list()
                print("\n")
                user_id = int(input("Please Input Movie Id no: "))
                print("\n")
                hall1.view_available_seats(user_id)
                print("\n")
            elif hall_no == 2:
                hall2.view(hall_no)
                print("\nFor this Hall Available Movie!!\n")
                hall2.view_show_list()
                print("\n")
                user_id = int(input("Please Input Movie Id no: "))
                print("\n")
                hall2.view_available_seats(user_id)
                print("\n")
            elif hall_no == 3:
                hall3.view(hall_no)
                print("\nFor this Hall Available Movie!!\n")
                hall3.view_show_list()
                print("\n")
                user_id = int(input("Please Input Movie Id no: "))
                print("\n")
                hall3.view_available_seats(user_id)
                print("\n")
        else:
            print("\nThere is No more Cinema Hall!!\n")
    elif opt == 3:
        hall1.Add_list()
        h_no = int(input("\nChoose Your Hall No: "))
        if h_no <= 3:
            if h_no == 1:
                hall1.view(h_no)
                print("\nFor this Hall Available Movie!!\n")
                hall1.view_show_list()
                print("\n")
                user = int(input("Please Input Movie Id no: "))
                ticket_no = int(input("Number of Ticket: "))
                seat_list = []
                for tick in range(ticket_no):
                    row = int(input("Enter seat Row: "))
                    col = int(input("Enter Seat Column: "))
                    seat = (row, col)
                    seat_list.append(seat)
                hall1.book_seats(user, seat_list)
            elif h_no == 2:
                hall2.view(h_no)
                print("\nFor this Hall Available Movie!!\n")
                hall2.view_show_list()
                print("\n")
                user = int(input("Please Input Movie Id no: "))
                ticket_no = int(input("Number of Ticket: "))
                seat_list = []
                for tick in range(ticket_no):
                    row = int(input("Enter seat Row: "))
                    col = int(input("Enter Seat Column: "))
                    seat = (row, col)
                    seat_list.append(seat)
                hall2.book_seats(user, seat_list)
            elif h_no == 3:
                hall3.view(h_no)
                print("\nFor this Hall Available Movie!!\n")
                hall3.view_show_list()
                print("\n")
                user = int(input("Please Input Movie Id no: "))
                ticket_no = int(input("Number of Ticket: "))
                seat_list = []
                for tick in range(ticket_no):
                    row = int(input("Enter seat Row: "))
                    col = int(input("Enter Seat Column: "))
                    seat = (row, col)
                    seat_list.append(seat)
                hall3.book_seats(user, seat_list)
    elif opt == 4:
        print("Thanks for visiting Our Project!!")
        break
