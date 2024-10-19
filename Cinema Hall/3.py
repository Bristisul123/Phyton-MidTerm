class Star_Cinema:
    hall_list= []

    def entry_hall(self,hall):
        self.hall = hall

class Hall(Star_Cinema):
    def __init__(self,row,col, hall_no):
        self.seats = {}
        self.show_list = []
        self.row = row
        self.col = col
        self.hall_no = hall_no       

    def entry_show(self,id,movie_name,time):
        show = (id,movie_name,time)
        self.show_list.append(show)

        seat_allocation = []
        for row in range(self.row):
            seat_row = []
            for col in range(self.col):
                seat_row.append(0)

        self.seats[id] = seat_allocation        


hall1 = Hall(5, 5, 101) 
hall1.entry_show("1", "Jigra", "2PM")
hall1.entry_show("2", "Avtar", "9PM")