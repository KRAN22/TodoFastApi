from database import Base
from sqlalchemy import String ,Column,Integer
from sqlalchemy_utils.types import ChoiceType


class Todo(Base):
    
    __tablename__ = "TodoList"
    
    STATUS = (
        ("CREATED" , "created"),
        ("IN-PROGRESS" , "in-progress"),
        ("COMPLETED" ,"completed"),
    )
    
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    title = Column(String(255))
    description = Column(String(255))
    status = Column(ChoiceType(choices=STATUS),default="CREATED")
    
    def __repr__(self):
        return f"<Todo {self.id}>"