from app import app, db
from models import Application

class MyApplication():

    def CreateApplication(self, appData):
        name = appData['name']
        existing = Application.query.filter_by(name=name).first()
        if existing is None: 
            myapp = Application(name = name)
            db.session.add(myapp)
            db.session.commit()
            return True
        else:
            return False
        