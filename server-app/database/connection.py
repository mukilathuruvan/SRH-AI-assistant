from flask_sqlalchemy import SQLAlchemy
import os

DB_URL = os.getenv('DATABASE_URL', 'mysql://root:root@localhost/srh_ai_assistance')


class DatabaseManager:
    def _init_(self,app):
        self.db =SQLAlchemy()
        app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL   
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        

    def create_tables(self):
        with app.app_context():
            db.create_all()

    def add_course(self, course):
        try:
            with app.app_context():
                db.session.add(course)
                db.session.commit()
                db.session.refresh(course)
                return course
        except Exception as e:
            print(f"Error adding course: {e}")
            return None
    
    def get_courses(self):
        try:
            with app.app_context():
                courses = Course.query.all()
                return courses
        except Exception as e:
            print(f"Error fetching courses: {e}")
            return []
        
    def update_course(self, course):
        try:
            with app.app_context():
                db.session.commit()
                db.session.refresh(course)
                return course
        except Exception as e:
            print(f"Error updating course: {e}")
            return None
        
    def delete_course(self, course):
        try:
            with app.app_context():
                db.session.delete(course)
                db.session.commit()
                return True
        except Exception as e:
            print(f"Error deleting course: {e}")
            return False
        







# Example of adding a course:
# session = SessionLocal()
# new_course = Course(name="Python Programming", description="Intro to Python", instructor_id=1) # Assuming instructor with ID 1 exists
# session.add(new_course)
# session.commit()
# session.refresh(new_course)
# session.close()