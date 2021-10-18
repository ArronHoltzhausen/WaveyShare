#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.INFO)
try:
    logging.info("epd2in13_V2 Demo")
    epd = epd2in13_V2.EPD()
    logging.info("init and Clear")
    #epd.init(epd.FULL_UPDATE)
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    # # partial update
    logging.info("4.show time...")
    time_image = Image.new('1', (epd.height, epd.width), 255)
    time_draw = ImageDraw.Draw(time_image)

    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    epd.displayPartBaseImage(epd.getbuffer(time_image))

    #image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    #draw = ImageDraw.Draw(image)
    #draw.rectangle([(0,0),(50,50)],outline = 0)
    #draw.rectangle([(55,0),(100,50)],fill = 0)
    #draw.line([(0,0),(50,50)], fill = 0,width = 1)
    #draw.line([(0,50),(50,0)], fill = 0,width = 1)
    #draw.chord((10, 60, 50, 100), 0, 360, fill = 0)
    #draw.ellipse((55, 60, 95, 100), outline = 0)
    #time_draw.pieslice((55, 60, 95, 100), 90, 180, outline = 0)
    #draw.pieslice((55, 60, 95, 100), 270, 360, fill = 0)
    #draw.polygon([(110,0),(110,50),(150,25)],outline = 0)
    #draw.polygon([(190,0),(190,50),(150,25)],fill = 0)
    #draw.text((120, 60), 'e-Paper demo', font = font15, fill = 0)
    #draw.text((110, 90), u'微雪电子', font = font24, fill = 0)

    epd.init(epd.PART_UPDATE)
    num = 0
    while (True):
        time_draw.rectangle((175, 0, 250, 50), fill = 255)
        time_draw.text((175, 0), time.strftime('%H:%M:%S'), font = font18, fill = 0)
        time_draw.line([(-10,18),(250,18)], fill = 0,width = 2)
        time_draw.text((120, 20), "poes", font = font24, fill = 0)
        time_draw.text((120, 40), "yes", font = font24, fill = 0)
        time_draw.text((120, 60), "ass", font = font24, fill = 0)
        time_draw.text((120, 80), "owo", font = font24, fill = 0)
        #time_draw.bitmap() <<<<======
        epd.displayPartial(epd.getbuffer(time_image))
        num = num + 1
        if(num == 20):
            break
    epd.Clear(0xFF)
    logging.info("Clear...")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    logging.info("Goto Sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    epd2in13_V2.epdconfig.module_exit()
    exit()
