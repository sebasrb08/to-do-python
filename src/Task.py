from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.Database import Base

class Task(Base):
    __tablename__ = "Tarea"
    
    __table_args__ = {'extend_existing': True}


    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(80))
    status:Mapped[str]=mapped_column(String(30))
    
    def __init__(self,title,description,status):
        self.title=title
        self.description = description
        self.status=status
    
    def get_title(self):
        return self.title
    
    def set_title(self,title):
        self.title=title
    
    def get_description(self):
        return self.description
    
    def set_description(self,description):
        self.description=description
        
    def get_status(self):
        return self.status
    
    def set_status(self,status):
        self.status=status  
