from lib.space import Space

""" 
Construct with fields:
name, street, city, property_type, maximum_capacity, number_of_bedrooms, number_of_bathrooms, price_per_night 
"""
def test_create_space():
    space = Space(1, "Space1", "1st Street", "City1", "House", 4, 2, 1, 100)
    assert space.id == 1
    assert space.name == "Space1"
    assert space.street == "1st Street"
    assert space.city == "City1"
    assert space.property_type == "House"
    assert space.maximum_capacity == 4
    assert space.number_of_bedrooms == 2
    assert space.number_of_bathrooms == 1
    assert space.price_per_night == 100

"""
When Constructing two spaces with the same fields ,they are equal
"""
def test_equality():
    space1 = Space(1, "Space1", "1st Street", "City1", "House", 4, 2, 1, 100)
    space2 = Space(1,"Space1", "1st Street", "City1", "House", 4, 2, 1, 100)
    assert space1 == space2

"""
When constructing a space and its formatted to a string and comes out in a friendly format
"""
def test_formatting():
    space = Space(1, "Space1", "1st Street", "City1", "House", 4, 2, 1, 100)
    assert str(space) == "1, Space1, 1st Street, City1, House, 4, 2, 1, 100"