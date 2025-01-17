from app.models import Request, Result, db


def init_db():
    db.create_all()  # This will create tables based on models if they don't exist


def save_request(user, filename):
    try:
        new_request = Request(user=user, filename=filename)
        db.session.add(new_request)
        db.session.commit()
        return new_request.id
    except Exception as e:
        db.session.rollback()
        raise e


def save_result(request_id, result):
    try:
        new_result = Result(request_id=request_id, result=result)
        db.session.add(new_result)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
