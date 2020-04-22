from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Database.Database import Base  # Remove Database. when instantiating database with shell, add for runtime


friendConnections = Table('friends', Base.metadata,
    Column('user1', Integer, ForeignKey('users.id'), nullable=False), #  primary_key=True ?
    Column('user2', Integer, ForeignKey('users.id'), nullable=False) #  primary_key=True ?
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    key = Column(Integer, nullable=False, unique=True)
    days = relationship('Day', backref='user', lazy=True)
    friends = relationship('User', secondary=friendConnections,
                    primaryjoin=id==friendConnections.c.user1,
                    secondaryjoin=id==friendConnections.c.user2,
                    backref='friendConnections',
                    lazy=True
    )

class Day(Base):
    __tablename__ = 'days'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    userID = Column(Integer, ForeignKey('users.id'), nullable=False)
    courses = relationship('Course', backref='day', lazy=True)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    start = Column(String, nullable=False)
    end = Column(String, nullable=False)
    text = Column(String, nullable=False)
    weekDay = Column(Integer, ForeignKey('days.id'), nullable=False)

#class FriendConnection(Base):
#    __tablename__ = 'friends'
#    id = Column(Integer, primary_key=True)
#    user1ID = Column(Integer, ForeignKey('users.id'), nullable=False)
#    user2ID = Column(Integer, ForeignKey('users.id'), nullable=False)


# One to many relationship reference : https://www.youtube.com/watch?v=juPQ04_twtA  Pretty Printed Yt channel
