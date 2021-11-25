# Importing the library
import psutil
import uvicorn
import gunicorn
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
  # Calling psutil.cpu_precent() for 4 seconds
  cpu_percent = psutil.cpu_percent(1)
  cpu_count = psutil.cpu_count()
  print('CPU Count: ', cpu_count)
  print('The CPU usage is: ', cpu_percent)

  # Getting % usage of virtual_memory ( 3rd field)
  mem = psutil.virtual_memory()
  mem_total = bytes2human(mem[0])
  mem_available = bytes2human(mem[1])
  mem_percent = bytes2human(mem[2])
  mem_used = bytes2human(mem[3])
  mem_free = bytes2human(mem[4])
  print('memory total:', mem_total)
  print('memory available:', mem_available)
  print('memory percent:', mem_percent)
  print('memory used:', mem_used)
  print('memory free:', mem_free)

  return {
    'cpu_count': cpu_count,
    'cpu_percent': cpu_percent,
    'mem_total': mem_total,
    'mem_available': mem_available,
    'mem_percent': mem_percent,
    'mem_used': mem_used,
    'mem_free': mem_free
  }