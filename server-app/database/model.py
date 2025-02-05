from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Course(Base):
    _tablename_ = 'course'

    id = Column(Integer, primary_key=True, index=True)
    coursename = Column(String, nullable=False, index=True)
    semester_fee = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)


# campus
    # instructor_id = Column(Integer, ForeignKey("instructors.id"), nullable=False) # Foreign key to instructors table
    is_active = Column(Boolean, default=True) # Course is active by default

    # Relationship to instructor (One-to-many relationship: One instructor can have many courses)
    instructor = relationship("Instructor", back_populates="courses")

    #Relationship to students (Many-to-many relationship via the association table)
    students = relationship("Student", secondary="enrollments", back_populates="courses")

    def _repr_(self):
        return f"<Course(name='{self.name}', description='{self.description}')>"



class Instructor(Base):  
    _tablename_ = 'instructors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)


    def _repr_(self):
        return f"<Instructor(name='{self.name}')>"



class Student(Base):
    _tablename_ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)

    courses = relationship("Course", secondary="enrollments", back_populates="students") 

    def _repr_(self):
        return f"<Student(name='{self.name}')>"


# Association table for the many-to-many relationship between students and courses
from sqlalchemy import Table, MetaData
metadata_obj = MetaData()
enrollments = Table('enrollments', metadata_obj,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)