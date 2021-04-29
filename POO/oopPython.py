class Hotel:
    def __init__(self, max_num_guest,parking_zone):
        self.max_num_guest = max_num_guest
        self.parking_zone = parking_zone
        self.guest = 0

    def plus_guest(self, number_of_guest):
        self.guest += number_of_guest
    
    def checkout(self,number_of_guest):
        self.guest -= number_of_guest
    
    def total_guest(self):
        return self.guest


class Cuarto:
    pass


#Instanciamos la clase: 
platziHotel = Hotel(500,1000)
