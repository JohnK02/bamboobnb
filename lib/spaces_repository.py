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
    
    # def find(self, id):
    #     pass
