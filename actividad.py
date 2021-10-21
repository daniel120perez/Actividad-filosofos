import threading
import time

class Filosofo(threading.Thread):
  def __init__(self, num, tenedor):
      threading.Thread.__init__(self)
      self.tenedor = tenedor
      self.num = num
      self.temp = (self.num + 1) % 5

  def come(self):
      print ("El filosofo "+str(self.num)+" come")
      time.sleep(2)

  def piensa(self):
      print ("El filosofo "+str(self.num)+" en espera")
      time.sleep(2)

  def obtieneTenIzq(self):
      print ("El filosofo "+str(self.num)+" Agarra tenedor izquierdo")
      print ("obtiene el tenedor "+str(self.num))
      time.sleep(2)
      self.tenedor[self.num].acquire()

  def obtieneTenDer(self):
      print ("El filosofo "+str(self.num)+" Agarra tenedor derecho")
      time.sleep(2)
      self.tenedor[self.temp].acquire()

  def liberaTenDer(self):
      print ("El filosofo "+str(self.num)+" deja el  tenedor derecho")
      time.sleep(2)
      self.tenedor[self.temp].release()

  def liberaTenIzq(self):
      print ("El filosofo "+str(self.num)+" deja el  tenedor izquierdo")
      time.sleep(2)
      self.tenedor[self.num].release()


  def run(self):
      while(True):
          self.piensa()
          self.obtieneTenIzq()
          self.obtieneTenDer()
          self.come()
          self.liberaTenDer()
          self.liberaTenIzq()
                                                                                                                                            
tenedor = [1,1,1,1,1]

for i in range(0, 5):
  tenedor[i] = threading.BoundedSemaphore(1)

for i in range(0, 5):
  t = Filosofo(i, tenedor)
  t.start()
  time.sleep(2)