#!/usr/bin/env python
import click
import os
import subprocess

def brimodename(bri) :
    if bri == 0 :
        return "Off"
    if bri == 1 :
        return "Low"
    if bri == 2 :
        return "Medium"
    if bri == 3 :
        return "Max"

def brival() :
    return int(subprocess.Popen("cat /sys/class/leds/asus::kbd_backlight/brightness", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())

def rgbspeedname(speed) :
    name = ""
    if speed == 0 :
        name = "Slow"
    if speed == 1 :
        name = "Medium"
    if speed == 2 :
        name = "Fast"
    return name

def rgbspeed() :
    return nodeval("kbbl_speed")

def rgbmodename():
    mode = nodeval("kbbl_mode")
    modename = ""
    if mode == 00 :
        modename = "Static"
    elif mode == 1 :
        modename = "Breathing"
    elif mode == 2 :
        modename = "Color Cycle"
    elif mode == 3 :
        modename = "Strobing"
    else : modename = "Not found"
    return modename

def nodeval(node) :
    kek = subprocess.Popen("cat /sys/devices/platform/faustus/kbbl/"+node, shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    return int(kek)

def setnode(node,val) :
    os.system('bash -c "echo '+val+' >> /sys/devices/platform/faustus/kbbl/'+node+'"')

@click.command()
@click.option("--red",prompt="Red value")
@click.option("--green",prompt="Green value")
@click.option("--blue",prompt="Blue value")
@click.option("--mode",prompt="Modes")
#@click.option("-")
def main(red,green,blue,mode):
    setnode("kbbl_red",str(red))
    setnode("kbbl_green",str(green))
    setnode("kbbl_blue",str(blue))
    setnode("kbbl_mode",str(mode))
    setnode("kbbl_set","1")

main()