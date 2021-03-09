import psutil
import math

memoryused = round(psutil.virtual_memory().used / 1000000000, 2)
totalmemory = round(psutil.virtual_memory().total / 1000000000, 0)

memory = "\uf85a  {0} / {1} GB".format(memoryused, totalmemory)

print(memory)
