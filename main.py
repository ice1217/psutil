# Importing the library
import psutil
import uvicorn
import gunicorn
from datetime import datetime
import pytz

import ssl
from psutil._common import bytes2human
from fastapi import FastAPI

app = FastAPI()

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
# Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
# Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

@app.get("/")
def read_root():
  timezone_WIB = pytz.timezone('Asia/Jakarta')
  current_time = datetime.now(timezone_WIB)
  # Calling psutil.cpu_precent() for 4 seconds
  cpu_percent = str(psutil.cpu_percent(1))
  cpu_percent_str = str(psutil.cpu_percent(1)) + '%'
  cpu_count = psutil.cpu_count()
  print('CPU Count: ', cpu_count)
  print('The CPU usage is: ', cpu_percent_str)

  # Getting % usage of virtual_memory ( 3rd field)
  mem = psutil.virtual_memory()
  mem_total = mem[0]
  mem_available = mem[1]
  mem_percent = mem[2]
  mem_used = mem[3]
  mem_free = mem[4]

  mem_total_str = bytes2human(mem[0])
  mem_available_str = bytes2human(mem[1])
  mem_percent_str = str(mem[2]) + '%'
  mem_used_str = bytes2human(mem[3])
  mem_free_str = bytes2human(mem[4])

  print('memory total:', mem_total_str)
  print('memory available:', mem_available_str)
  print('memory percent:', mem_percent_str)
  print('memory used:', mem_used_str)
  print('memory free:', mem_free_str)

  return {
    'datetime': current_time,
    'cpu_count': cpu_count,
    'cpu_percent': cpu_percent,
    'mem_total': mem_total,
    'mem_available': mem_available,
    'mem_percent': mem_percent,
    'mem_used': mem_used,
    'mem_free': mem_free,
    'mem_total_str': mem_total_str,
    'mem_available_str': mem_available_str,
    'mem_percent_str': mem_percent_str,
    'mem_used_str': mem_used_str,
    'mem_free_str': mem_free_str
  }
