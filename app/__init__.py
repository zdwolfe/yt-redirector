from thread import start_new_thread
import time
import os
import urllib2

snitch_url = os.environ["SNITCH_URL"]
snitch_interval = os.environ["SNITCH_INTERVAL"]
if snitch_interval is None:
    snitch_interval = 60
else:
    snitch_interval = int(snitch_interval)

# Make a GET to 'SNITCH_URL' every
# SNITCH_INTERVAL seconds for uptime monitoring.
# See https://deadmanssnitch.com
def setInterval(asynchronous = True):
    if asynchronous:
        args = (False,)
        start_new_thread(setInterval, args)
    else:
        while True:
            urllib2.urlopen(snitch_url).read()
            time.sleep(snitch_interval) # seconds

        return

if snitch_url is not None:
    setInterval()
else:
    print "Provide SNITCH_URL for uptime monitoring"