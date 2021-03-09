# coding=utf-8
from datetime import datetime

timenow = datetime.now()

format = timenow.strftime("%a, %b %d   %I:%M %p")
print(format)
