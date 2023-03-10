from database import Base
from sqlalchemy import String ,Column,Integer,ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship


class Todo(Base):
    
    __tablename__ = "todo"
    
    STATUS = (
        ("CREATED" , "created"),
        ("IN-PROGRESS" , "in-progress"),
        ("COMPLETED" ,"completed"),
    )
    
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    title = Column(String(255))
    description = Column(String(255))
    status = Column(ChoiceType(choices=STATUS),default="CREATED")
    user_id = Column(Integer,ForeignKey('user.id'))
    
    todo = relationship('User', back_populates = 'user')
    
    def __repr__(self):
        return f"<Todo {self.id}>"
    
    
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer,primary_key=True,index= True,autoincrement=True)
    username = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))

    user = relationship('Todo', back_populates = 'todo')

    def __repr__(self):
        return f"<Order {self.username}>"
    