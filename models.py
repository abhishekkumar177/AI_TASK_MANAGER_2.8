from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# -----------------------------
# USER MODEL
# -----------------------------
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(20), default="Member")  # "Admin" or "Member"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role
        }


# -----------------------------
# TASK MODEL
# -----------------------------
class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(50), default="Pending")
    deadline = db.Column(db.Date)
    
    # NEW FIELD: assigned user
    assigned_to_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    assigned_user = db.relationship("User", backref="assigned_tasks", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "deadline": str(self.deadline) if self.deadline else None,
            "assigned_to": self.assigned_user.username if self.assigned_user else None
        }
