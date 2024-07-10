from lib.space import Space
class SpaceRepository:
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        spaces = []
        for row in rows:
            space = Space(
                row["id"],
                row["name"],
                row["street"],
                row["city"],
                row["property_type"],
                row["maximum_capacity"],
                row["number_of_bedrooms"],
                row["number_of_bathrooms"],
                row["price_per_night"],
                row["user_id"])
            spaces.append(space)
        return spaces
    
    def find(self, id):
        rows = self._connection.execute(
            "SELECT * FROM spaces WHERE id = %s", [id]
        )
        row = rows[0]
        for row in rows:
            return Space(
                row["id"],
                row["name"],
                row["street"],
                row["city"],
                row["property_type"],
                row["maximum_capacity"],
                row["number_of_bedrooms"],
                row["number_of_bathrooms"],
                row["price_per_night"],
                row["user_id"])
    
    def create(self, space):
        self._connection.execute(
            "INSERT INTO spaces (name, street, city, property_type, maximum_capacity, number_of_bedrooms, number_of_bathrooms, price_per_night, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", [
                space.name,
                space.street,
                space.city,
                space.property_type,
                space.maximum_capacity,
                space.number_of_bedrooms,
                space.number_of_bathrooms,
                space.price_per_night,
                space.user_id
            ]
        )
        
    def delete(self, id):
        self._connection.execute("DELETE FROM spaces WHERE id = %s", [id])
        return 