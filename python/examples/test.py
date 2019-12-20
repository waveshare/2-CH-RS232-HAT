#!/usr/bin/python
# -*- coding:utf-8 -*-
import serial
import os
import sys
import logging
import time

logging.basicConfig(level=logging.INFO)
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_2_CH_RS232_HAT import config

ser1 = config.config(Baudrate=460800, dev = "/dev/ttySC0")
ser2 = config.config(Baudrate=460800, dev = "/dev/ttySC1")
data = ''

try: 
    while(1):
        ser1.Uart_SendString('Waveshare 2-CH RS232 HAT\r\n')
        data_t = ser2.Uart_ReceiveString(26)
        print data_t
        if(data_t == 'Waveshare 2-CH RS232 HAT\r\n'):
            print("CH1 sends CH2 reception successfully")
        ser2.Uart_SendString('Waveshare 2-CH RS232 HAT\r\n')
        data_t = ser1.Uart_ReceiveString(26)
        print data_t
        if(data_t == 'Waveshare 2-CH RS232 HAT\r\n'):
            print("CH2 sends CH1 reception successfully")
        time.sleep(1)
        
        
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    exit()


    
     
     
     