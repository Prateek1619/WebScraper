from News_app.run import *
from News_app.models import News


class log():

    def feed(data):
        try:
            news = News(title = data['title'], url=data['url'], shorttxt=data['shorttxt'])
            news.add()
            print("Inserted data in the DB")
        except Exception as e:
            error = 'Error on line {} and file {}'.format(e.__traceback__.tb_lineno, e.__traceback__.tb_frame), type(e).__name__, str(e)
            return render_template('error.html', exception = "{}".format(error))


#  title = db.Column(db.String(256))
#     url = db.Column(db.String(128), type="URL")
#     shorttxt = db.Column(db.String(128))
#     content = db.Column(db.String(1024))