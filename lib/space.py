class Space:
    def __init__(self, id, name, street, city, property_type, maximum_capacity, number_of_bedrooms, number_of_bathrooms, price_per_night):
        self.id = id
        self.name = name
        self.street = street
        self.city = city
        self.property_type = property_type
        self.maximum_capacity = maximum_capacity
        self.number_of_bedrooms = number_of_bedrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.id}, {self.name}, {self.street}, {self.city}, {self.property_type}, {self.maximum_capacity}, {self.number_of_bedrooms}, {self.number_of_bathrooms}, {self.price_per_night}"
    

