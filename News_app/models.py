from flask import render_template
from datetime import datetime
from News_app.run import db


class News(db.Model):
    __tablename__ = 'News'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.String(256))
    url = db.Column(db.String(1024))
    shorttxt = db.Column(db.String(32))
  

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except Exception as e:
            print('Something went wrong')
            error = 'Error on line {} and file {}'.format(e.__traceback__.tb_lineno, e.__traceback__.tb_frame), type(e).__name__, str(e)
            return render_template('error.html', exception = "{}".format(error))

    @classmethod
    def get_latest_ten(cls):
        limit=10
        return cls.query.order_by(cls.id.desc()).limit(limit)

    def add(self):
        try:
            db.session.add(self)    
            db.session.commit()
        except Exception as e:
            print("db insertion failed")
            error = 'Error on line {} and file {}'.format(e.__traceback__.tb_lineno, e.__traceback__.tb_frame), type(e).__name__, str(e)
            return render_template('error.html', exception = "{}".format(error))
        