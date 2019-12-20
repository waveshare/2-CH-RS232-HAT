#!/usr/bin/python
# -*- coding:utf-8 -*-
import serial
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_2_CH_RS232_HAT import config

ser = config.config(dev = "/dev/ttySC0")
data = ''
ser.Uart_SendString('Waveshare 2-CH RS232 HAT\r\n')

try:
    while(1):
        data_t = ser.Uart_ReceiveByte()
        
        print("%c"%data_t),
        ser.Uart_SendByte(data_t)

except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    exit()


     
     
     
     