from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rentomatic.domain import room
from rentomatic.repository.postgres_objects import Base, Room

class PostgresRepo:
    def __init__(self, connection_data):
        connection_string = "postgresql+psycopg2://{}:{}@{}/{}".format(
            connection_data['user'],
            connection_data['password'],
            connection_data['host'],
            connection_data['dbname']
        )
        
        self.enginge = create_engine(connection_string)
        Base.metadata.bind = self.engine
    
    def list(self, filters=None):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        
        query = session.query(Room)
        
        if filters is None:
            return query.all()
        if 'code_eq' in filters:
            query = query.filter(Room.code == filters['code_eq'])
        if 'price_eq' in filters:
            query = query.filter(Room.price == filters['price_eq'])
        if 'price_lt' in filters:
            query = query.filter(Room.price < filters['price_lt'])
        if 'price_gt' in filters:
            query = query.filter(Room.price > filters['price_gt'])
        
        return [
            room.Room(
                code=q.code,
                size=q.size,
                price=q.price,
                latitude=q.latitude,
                longitude=q.longitude
            )
        ]