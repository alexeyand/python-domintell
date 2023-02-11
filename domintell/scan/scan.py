import time
import logging
import sys
import domintell
#import credentials
import os, sys

def _on_message(message):
    print('received message')
    print(message)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# UDP, Serial (or USB over serial) connection to Domintell controller

host = {
    'ADDRESS': '10.200.1.213:6029',
    'SECRET': 'LOGIN'
}
#host = '10.200.1.214, 6029'
	
logging.info(host['ADDRESS'])

controller = domintell.Controller(host) 
controller.subscribe(_on_message)

logging.info('LOGIN')
controller.login(host['SECRET'])

time.sleep(10)
logging.info('Starting scan')
controller.scan(None)

logging.info('Going to sleep')
time.sleep(100)
logging.info('Exiting ...')
controller.stop()
