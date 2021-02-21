from flask import render_template, redirect, flash, url_for, request, Blueprint
from bs4 import BeautifulSoup
import requests
import textwrap
from News_app.models import News
from News_app.db import log
#from News_app.get_items import *
from News_app.links import *
import sys
#from werkzeug.urls import url_parse
#from News_app.run import db, app

News_t = Blueprint('News_t', __name__, template_folder='templates')

@News_t.route('/', methods=['GET','POST'])
def Get_live_news_feed():
    try:
        rss_text=requests.get(news_url).text
        soup_page=BeautifulSoup(rss_text,"xml")

        for (title, url, shorttxt) in get_items(soup_page):
            title = '\n'.join(textwrap.wrap(title))
            url = '\n'.join(textwrap.wrap(url))
            shorttxt = '\n'.join(textwrap.wrap(textwrap.shorten(shorttxt, 128)))
        
            dict = organise_data(title, url, shorttxt)
            log.feed(dict)  # writing into db

        else:
            print("Successfully inserted all elements")
            return result()
              
    except Exception as e:
        error = 'Error on line {} and file {}'.format(e.__traceback__.tb_lineno, e.__traceback__.tb_frame), type(e).__name__, str(e)
        return render_template('error.html', exception = "{}".format(error))

def result():
    """ Description
        In this function we extract the content from News table from DB.
        and pass the object to html file
    """
    try:
        feed = News.get_latest_ten()
        for i in feed:
            print(i)
        return render_template("index.html", title='Results', feed = feed)
    except Exception as e:
        print("failed before rendering the HTML")
        error = 'Error on line {} and file {}'.format(e.__traceback__.tb_lineno, e.__traceback__.tb_frame), type(e).__name__, str(e)
        return render_template('error.html', exception = "{}".format(error))

def organise_data(title, url, shorttxt):
    dict = {'title': title, 'url': url, 'shorttxt':shorttxt}
    return dict

def get_items(soup):
    try:
        for news in soup.findAll("item")[0:11]:
            s = BeautifulSoup(news.description.text, 'lxml')
            a = s.select('a')[-1]
            a.extract()

            html = requests.get(news.link.text)
            soup_content = BeautifulSoup(html.text,"lxml")

            # perform basic sanitization:
            for t in soup_content.select('script, noscript, style, iframe, nav, footer, header'):
                t.extract()

            yield news.title.text.strip(), html.url , str(soup_content.select_one('body').text)
    except Exception as e:
        error = 'Error on line {} and file {}'.format(e.__traceback__.tb_lineno, e.__traceback__.tb_frame), type(e).__name__, str(e)
        return render_template('error.html', exception = "{}".format(error))