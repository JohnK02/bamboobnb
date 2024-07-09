from lib.spaces_repository import SpaceRepository
from lib.space import Space
"""
When #all is called all of the instances of space returned
"""
def test_all(db_connection):
    db_connection.seed("seeds/test_bamboo_bnb_directory.sql")
    repo = SpaceRepository(db_connection)
    result = repo.all()
    assert result == [
        Space(
            1,
    'space1',
    'street1',
    'city1',
    'type1',
    1,
    1,
    1,
    100.00,
    1
),
Space(
    2,
    'space2',
    'street2',
    'city2',
    'type2',
    2,
    2,
    2,
    200.00,
    2
),
Space(
    3,
    'space3',
    'street3',
    'city3',
    'type3',
    3,
    3,
    3,
    300.00,
    3
)
    ]

"""
when #find is called with an id, the specified space instance is returned
"""
# def test_find(db_connection):
#     db_connection.seed("seeds/test_bamboo_bnb_directory.sql")
#     repo = SpaceRepository(db_connection)
#     result = repo.find(1)
#     assert result == Space(
#             1,
#     'space1',
#     'street1',
#     'city1',
#     'type1',
#     1,
#     1,
#     1,
#     100.00,
#     1
# )