from time import sleep
def printt(string, delay):
  for i in str(string):
    print(i, end="", flush = True)
    sleep(delay)
  print('')
printt("TypeWriter Effect!", 0.5)
