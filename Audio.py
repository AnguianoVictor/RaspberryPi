#!/usr/bin/python
from time import sleep as tiempo
import sys as cmd
import os as audio



def main():
    #os.system('aplay /home/pi/Desktop/Alerta_Audio.wav')
    #print('number arguments:', len(cmd.argv), 'arguments')
    print('Argument List:', str(cmd.argv))
    arg = str(cmd.argv[1])
    #f = open("/home/pi/Desktop/flag.txt", "r")
    ##print(f.read())
    #var = f.read()
    #f.close()
    ##print(var)
    print(arg)
    if arg == '1':
        audio.system('aplay /home/pi/Desktop/Alerta_Audio.wav')
    else:
        print("No One")
    
    
if __name__ == '__main__':
    try:
        main()
            #tiempo(2)
    except:
        print("Error")