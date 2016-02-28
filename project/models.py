from view import db

class Task(db.Model):
    __tablename__ = "tasks"

    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    due_date = db.Colum(db.Date,nullable=True)
    priority = db.Column(db.Integer,nullable=True)
    status = db.Column(db.Integer)

    def __init__(self,name,due_date,priority,status):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __repr__(self):
        return '<name {0}>'.format(self.name)
