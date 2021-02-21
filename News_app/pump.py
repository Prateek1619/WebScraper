
# This module is just a preparation of creating service
from requests import get
from time import sleep
from News_app.routes import Get_live_news_feed

flag = False 
class Update_news():
  
  def pump(self):
    print("pumping")
    # once to start, then loop
    self.updateDB()
    while not(sleep(600)):
       self.updateDB()

  def updateDB(self):
    print("Pushing news to store")
    retval = Get_live_news_feed()
    print(retval)

def startLoop():
  global flag
  print("starting")
  flag = True
  pump = Update_news()
  pump.pump()

startLoop()