from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Request(db.Model):
    __tablename__ = "requests"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, nullable=False)
    request_name = db.Column(
        db.String, nullable=False
    )  # Added field for name of request
    filename = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    # Relationship to results
    results = db.relationship(
        "Result", back_populates="request", cascade="all, delete-orphan"
    )


class Result(db.Model):
    __tablename__ = "results"
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey("requests.id"), nullable=False)
    result = db.Column(db.Float, nullable=False)

    # Relationship back to request
    request = db.relationship("Request", back_populates="results")
