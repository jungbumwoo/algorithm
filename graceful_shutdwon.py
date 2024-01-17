import signal
import time
import os
import psutil

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, *args):
    pid = os.getpid()
    print(f"pid: {pid} start running..")
    print("doing some graceful killing...")
    print("release lock...")
    print("doing some graceful killing...2")

    process = psutil.Process()
    print(process.memory_info().rss) 

    print("doing some graceful killing...3")
    self.kill_now = True

if __name__ == '__main__':
  pid = os.getpid()
  print(f"pid: {pid} start running..")
  killer = GracefulKiller()
  i = 0
  while not killer.kill_now:
    time.sleep(3)

    print(f"doing something {i} in a loop ...")
    i += 1
   
  print("End of the program. I was killed gracefully :)")
