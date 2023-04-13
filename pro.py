import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
import gpiozero as gpio
from time import sleep
import numpy as np
import pyaudio
import numpy as np
import matplotlib.pyplot as plot
from gpiozero import LED, Button
import matplotlib.pyplot as plt
import fitz
import sys
import atexit
import matplotlib.pyplot as pltb
import threading
import tkinter as tk
from tkinter import ttk
from reportlab.pdfgen import canvas
import fitz
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg





#leds de volumen 1
led_v1_1=gpio.LED(2)
led_v1_2=gpio.LED(14)
led_v1_3=gpio.LED(15)
#leds de volumen 2
led_v2_1=gpio.LED(3)
led_v2_2=gpio.LED(11)
led_v2_3=gpio.LED(0)

#leds de volumen 3
led_v3_1=gpio.LED(4)
led_v3_2=gpio.LED(13)
led_v3_3=gpio.LED(19)

#leds de volumen 4
led_v4_1=gpio.LED(8)
led_v4_2=gpio.LED(7)
led_v4_3=gpio.LED(1)

#leds de volumen 5
led_v5_1=gpio.LED(12)
led_v5_3=gpio.LED(16)


button_up = Button(10)
button_down = Button(9)
button_config = Button(6)
button_save = Button(5)
button_vup = Button(18)
button_vdown = Button(23)

button_sonido1 = Button(17)
button_sonido2 = Button(27)
button_sonido3 = Button(22)
button_sonido4 = Button(24)
button_sonido5 = Button(25)

button_yes= Button(20)
button_no = Button(21)

button_grafica = Button(26)

permiso1=1
permiso2=1
permiso3=1
permiso4=1
permiso5=1
permiso6=1
permiso7=1
permiso8=1
permiso9=1
permiso10=1
permiso11=1
permiso12=1
permiso13=1
permiso14=1
permiso15=1






led_index = 1
volumen1=1
volumen2=1
volumen3=1
volumen4=1
volumen5=1
c_configuration = 0



f = 400.0               #frecuencia de la señal (numero flotante)


    

    

def increment_led():
    global led_index
    if led_index < 5:
        led_index += 1
    else:
        led_index = 1
    sleep(0.3)
def decrement_led():
    global led_index
    if led_index > 1:
        led_index -= 1
    else:
        led_index = 5
    sleep(0.3)
def configuration ():
    #led volumen 1
    led_v1_1.off()
    led_v1_2.off()
    led_v1_3.off()
    #led volumen 2
    led_v2_1.off()
    led_v2_2.off()
    led_v2_3.off()
    #led volumen 4
    led_v4_1.off()
    led_v4_2.off()
    led_v4_3.off()
    #led volumen 5
    led_v5_1.off()
    led_v5_3.off()
    
    global c_configuration
    c_configuration = 1
def saves ():
    global c_configuration
    c_configuration = 0
def increment_v():
    if c_configuration==1:
        if led_index==1:
            global volumen1
            if volumen1 < 4:
                volumen1 += 1
            else:
                volumen1 = 1
        if led_index==2:
            global volumen2
            if volumen2 < 4:
                volumen2 += 1
            else:
                volumen2 = 1
        if led_index==3:
            global volumen3
            if volumen3 < 4:
                volumen3 += 1
            else:
                volumen3 = 1
        if led_index==4:
            global volumen4
            if volumen4 < 4:
                volumen4 += 1
            else:
                volumen4 = 1
        if led_index==5:
            global volumen5
            if volumen5 < 4:
                volumen5 += 1
            else:
                volumen5 = 1
    sleep(0.3)
def decrement_v():
    if c_configuration==1:
        if led_index==1:
            global volumen1
            if volumen1 > 0:
                volumen1 -= 1
            else:
                volumen1 = 3
        if led_index==2:
            global volumen2
            if volumen2 > 0:
                volumen2 -= 1
            else:
                volumen2 = 3
        if led_index==3:
            global volumen3
            if volumen3 > 0:
                volumen3 -= 1
            else:
                volumen3 = 3
        if led_index==4:
            global volumen4
            if volumen4 > 0:
                volumen4 -= 1
            else:
                volumen4 = 3
        if led_index==5:
            global volumen5
            if volumen5 > 0:
                volumen5 -= 1
            else:
                volumen5 = 3
    sleep(0.3)
def sonido1():
    if volumen1==1:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.1           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 10000.0               #frecuencia de la señal (numero flotante)
        global frec1
        frec1=f2
      
        
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()
    if volumen1==2:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.45           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 10000.0               #frecuencia de la señal (numero flotante)
        global frec2
        frec2=f2
      
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()
    if volumen1==3:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 1.0           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 10000.0               #frecuencia de la señal (numero flotante)
        global frec3
        frec3 =f2
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()

def sonido2():
    if volumen2==1:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.3           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 8000.0               #frecuencia de la señal (numero flotante)
        global frec4
        frec4 =f2
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()
    if volumen2==2:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.6           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 8000.0               #frecuencia de la señal (numero flotante)
        global frec5
        frec5 =f2
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()
    if volumen2==3:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.7           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 8000.0               #frecuencia de la señal (numero flotante)
        global frec6
        frec6 =f2
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()

def sonido3():
    if volumen3==1:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.2           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 11000.0               #frecuencia de la señal (numero flotante)
        global frec7
        frec7 =f2
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()
    if volumen3==2:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.40           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 11000.0               #frecuencia de la señal (numero flotante)
        global frec8
        frec8 =f2
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()
    if volumen3==3:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.89           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 11000.0               #frecuencia de la señal (numero flotante)
        global frec9
        frec9 =f2
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()
def sonido4():
    if volumen4==1:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.18           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 12000.0               #frecuencia de la señal (numero flotante)
        global frec10
        frec10 =f2
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()
    if volumen4==2:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.52           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 12000.0               #frecuencia de la señal (numero flotante)
        global frec11
        frec11 =f2
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()
    if volumen4==3:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.92           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 12000.0               #frecuencia de la señal (numero flotante)
        global frec12
        frec12 =f2
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()
    
def sonido5():
    if volumen5==1:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.15           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 14000.0               #frecuencia de la señal (numero flotante)
        global frec13
        frec13 =f2
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()
    if volumen5==2:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.55           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 14000.0               #frecuencia de la señal (numero flotante)
        global frec14
        frec14 =f2
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()
    if volumen5==3:
        p = pyaudio.PyAudio()   #crear objeto PyAudio
        volumen = 0.95           #volumen entre 0 y 1, (numero flotante)
        fs = 44100              #frecuencia de muestreo
        duracion = 2.0          #duracion de la señal en segundos (numero flotante)
        f2 = 14000.0               #frecuencia de la señal (numero flotante)
        global frec15
        frec15 =f2
        #generar señal discreta en base a los parametros para un señal sinuidal periodica
        #discreta.
        x = np.sin(2*np.pi*np.arange(duracion*fs)*f2/fs)
        x = np.float32(x)       #convertimos los valores a flotantes de 32 bits, se requiere
                   #esta conversion de los datos para su reproduccion con pyaudio.

        #la funcion open que se utiliza a continuacion crea un stream (flujo) de datos vacio para
        #reproducir la señal creadad. Para crear dicho stream se requiere
        #especificar los parametros adecuados, como minimo:  el formato de los datos, la
        #cantidad de canales, la frecuencia de muestreo y un parametro booleano para
        #especificar si es un stream de salida o de entrada.

        stream = p.open(format = pyaudio.paFloat32,
            channels = 1,
            rate = fs,
            output = True
            )

        #escribe los datos de la señal x en el stream y modifica su amplitud al multiplicar
        #por la variable vol.  La variable vol se puede obviar si no se requiere variar el
        #volumen.
        stream.write(volumen*x)
        #detiene el stream
        stream.stop_stream()
        #cierra el stream
        stream.close()
        #finaliza sesion de PyAudio
        p.terminate()
def yes():
    global permiso1
    global permiso2
    global permiso3
    global permiso4
    global permiso5
    global permiso6
    global permiso7
    global permiso8
    global permiso9
    global permiso10
    global permiso11
    global permiso12
    global permiso13
    global permiso14
    global permiso15
    
    
    if volumen1==1 and permiso1==1:
        print("se escucho")
        permiso1=0
        global muestra1
        muestra1=1
    if volumen1==2 and permiso2==1:
        print("se escucho")
        global muestra2
        muestra2=1
        permiso2=0
    if volumen1==3 and permiso3==1:
        print("se escucho")
        global muestra3
        muestra3=1
        permiso3=0
    if volumen2==1 and permiso4==1:
        print("se escucho")
        global muestra4
        muestra4=1
        permiso4=0
    if volumen2==2 and permiso5==1:
        print("se escucho")
        global muestra5
        muestra5=1
        permiso5=0
    if volumen2==3 and permiso6==1:
        print("se escucho")
        global muestra6
        muestra6=1
        permiso6=0
    if volumen3==1 and permiso7==1:
        print("se escucho")
        global muestra7
        muestra7=1
        permiso7=0
    if volumen3==2 and permiso8==1:
        print("se escucho")
        global muestra8
        muestra8=1
        permiso8=0
    if volumen3==3 and permiso9==1:
        print("se escucho")
        global muestra9
        muestra9=1
        permiso9=0
    if volumen4==1 and permiso10==1:
        print("se escucho")
        global muestra10
        muestra10=1
        permiso10=0
    if volumen4==2 and permiso11==1:
        print("se escucho")
        global muestra11
        muestra11=1
        permiso11=0
    if volumen4==3 and permiso12==1:
        print("se escucho")
        global muestra12
        muestra12=1
        permiso12=0
    if volumen5==1 and permiso13==1:
        print("se escucho")
        global muestra13
        muestra13=1
        permiso13=0
    if volumen5==2 and permiso14==1:
        print("se escucho")
        global muestra14
        muestra14=1
        permiso14=0
    if volumen5==3 and permiso15==1:
        print("se escucho")
        global muestra15
        muestra15=1
        permiso15=0
   
        
    

def no():
    global permiso1
    global permiso2
    global permiso3
    global permiso4
    global permiso5
    global permiso6
    global permiso7
    global permiso8
    global permiso9
    global permiso10
    global permiso11
    global permiso12
    global permiso13
    global permiso14
    global permiso15
    if volumen1==1 and permiso1==1:
        print("no escucho")
        global muestra1
        muestra1=0
        permiso1=0
    if volumen1==2 and permiso2==1:
        print("no escucho")
        global muestra2
        muestra2=0
        permiso3=0
    if volumen1==3 and permiso3==1:
        print("no escucho")
        global muestra3
        muestra3=0
        permiso3=0
    if volumen2==1 and permiso4==1:
        print("no escucho")
        global muestra4
        muestra4=0
        permiso4=0
    if volumen2==2 and permiso5==1:
        print("no escucho")
        global muestra5
        muestra5=0
        permiso5=0
    if volumen2==3 and permiso6==1:
        print("no escucho")
        global muestra6
        muestra6=0
        permiso6=0
    if volumen3==1 and permiso7==1:
        print("no escucho")
        global muestra7
        muestra7=0
        permiso7=0
    if volumen3==2 and permiso8==1:
        print("no escucho")
        global muestra8
        muestra8=0
        permiso8=0
    if volumen3==3 and permiso9==1:
        print("no escucho")
        global muestra9
        muestra9=0
        permiso9=0
    if volumen4==1 and permiso10==1:
        print("no escucho")
        global muestra10
        muestra10=0
        permiso10=0
    if volumen4==2 and permiso11==1:
        print("no escucho")
        global muestra11
        muestra11=0
        permiso11=0
    if volumen4==3 and permiso12==1:
        print("no escucho")
        global muestra12
        muestra12=0
        permiso12=0
    if volumen5==1 and permiso13==1:
        print("no escucho")
        global muestra13
        muestra13=0
        permiso13=0
    if volumen5==2 and permiso14==1:
        print("no escucho")
        global muestra14
        muestra14=0
        permiso14=0
    if volumen5==3 and permiso15==1:
        print("no escucho")
        global muestra15
        muestra15=0
        permiso15=0
        
def grafica ():
    

    def guardar_pdf():
        # Creamos una instancia del documento PDF
        doc = fitz.open()

        # Creamos una página vacía en el documento
        pagina = doc.new_page()

        # Creamos una imagen de la gráfica actual
        figura = plt.gcf()
        figura.savefig("temp.png")

        # Insertamos la imagen en la página
        imagen = fitz.Pixmap("temp.png")
        pagina.insert_image(fitz.Rect(0, 0, imagen.width, imagen.height), pixmap=imagen)

        # Guardamos el documento como un archivo PDF
        doc.save(nombre + ".pdf")

        # Cerramos el documento y eliminamos la imagen temporal
        doc.close()
        imagen.close()
        plt.clf()
        print("Gráfica guardada como PDF")

    # Definimos los valores de la gráfica
    valores = [frec1/1000, frec2/1000, frec3/1000, frec4/1000, frec5/1000, frec6/1000,frec7/1000,frec8/1000,frec9/1000,frec10/1000,frec11/1000,frec12/1000,frec13/1000,frec14/1000,frec15/1000]
    confirmaciones=[muestra1,muestra2,muestra3,muestra4,muestra5,muestra6,muestra7,muestra8,muestra9,muestra10,muestra11,muestra12,muestra13,muestra14,muestra15]

    # Creamos una lista de índices para las barras
    indices = [-2,90,190,10,75,65,34,49,55,78,90,123,165,177,180]

    # Creamos una lista de colores para las barras
    colores = ['blue' if valor == 1 else 'red' for valor in confirmaciones]

    # Creamos la gráfica de barras
    plt.bar(indices, valores, color=colores)

    # Etiquetamos los ejes
    plt.xlabel("Volumen")
    plt.ylabel("Frecuencia")

    # Agregamos el título
    plt.title("Resultados de: "+nombre)

    # Creamos la ventana principal de tkinter
    ventana = tk.Tk()
    ventana.geometry("500x500")

    # Creamos el botón para guardar en PDF
    boton_guardar1 = tk.Button(ventana, text="Guardar", command=guardar_pdf)
    boton_guardar1.place(x=200, y=450)

    # Creamos el widget para mostrar la gráfica
    canvas = tk.Canvas(ventana, width=400, height=400)
    canvas.place(x=50, y=10)

    # Dibujamos la gráfica en el widget
    figura = plt.gcf()
    figura.set_size_inches(4, 4)
    figura_canvas = FigureCanvasTkAgg(figura, master=canvas)
    figura_canvas.get_tk_widget().pack()

    # Mostramos la ventana de tkinter
    ventana.mainloop()
    
    
    
    
    

button_up.when_pressed = increment_led
button_down.when_pressed = decrement_led
button_vup.when_pressed = increment_v
button_vdown.when_pressed = decrement_v
button_save.when_pressed = saves
button_config.when_pressed = configuration

button_sonido1.when_pressed = sonido1
button_sonido2.when_pressed = sonido2
button_sonido3.when_pressed = sonido3
button_sonido4.when_pressed = sonido4
button_sonido5.when_pressed = sonido5

button_yes.when_pressed = yes
button_no.when_pressed = no

button_grafica.when_pressed = grafica
# Crear la ventana principal
ventana = tk.Tk()

# Ajustar tamaño de la ventana
ventana.geometry("400x300")

# Crear función para cada botón
def crear_paciente():
    def salir_c():
        ventana2.destroy()
    def guardar_paciente():
        nombres = nombres_pacientes.get()
        apellidos = apellidos_pacientes.get()
        edad = edad_pacientes.get()
        telefono = telefono_pacientes.get()
        correo = correo_pacientes.get()
        # Conectarse a la base de datos
        conexion = sqlite3.connect('audio.db')
        cursor = conexion.cursor()
        # Crear la tabla si no existe
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS TBpacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombres TEXT,
            apellidos TEXT,
            edad TEXT,
            Telefono TEXT,
            correo TEXT
        )
        ''')
        # Insertar el nuevo producto
        cursor.execute('INSERT INTO TBpacientes (nombres, apellidos,edad,Telefono,correo) VALUES (?, ? , ?, ?, ?)', (nombres, apellidos, edad, telefono, correo))
        conexion.commit()
        conexion.close()
        # Limpiar los campos de entrada
        nombres_pacientes.delete(0, END)
        apellidos_pacientes.delete(0, END)
        edad_pacientes.delete(0, END)
        telefono_pacientes.delete(0, END)
        correo_pacientes.delete(0, END)
    
    ventana2 = Tk()
    ventana2.geometry("400x400")
    ventana2.title('Agregar y mostrar productos')
    # Crear los campos de entrada y los botones
    lbl_nombre = tk.Label(ventana2, text="Nombres")
    lbl_nombre.pack(pady=5)
    nombres_pacientes = Entry(ventana2, width=30)
    nombres_pacientes.pack()
    lbl_nombre = tk.Label(ventana2, text="Apellidos")
    lbl_nombre.pack(pady=5)
    apellidos_pacientes = Entry(ventana2, width=30)
    apellidos_pacientes.pack()
    lbl_nombre = tk.Label(ventana2, text="Edad")
    lbl_nombre.pack(pady=5)
    edad_pacientes = Entry(ventana2, width=30)
    edad_pacientes.pack()
    lbl_nombre = tk.Label(ventana2, text="Telefono")
    lbl_nombre.pack(pady=5)
    telefono_pacientes = Entry(ventana2, width=30)
    telefono_pacientes.pack()
    lbl_nombre = tk.Label(ventana2, text="Correo")
    lbl_nombre.pack(pady=5)
    correo_pacientes = Entry(ventana2, width=30)
    correo_pacientes.pack()
    
    boton_guardar = tk.Button(ventana2, text="Guardar", bg="green", fg="black", command=guardar_paciente, width=20)
    boton_guardar.pack()
    boton_salir_crear = tk.Button(ventana2, text="Salir", bg="red", fg="black", command=salir_c, width=20)
    boton_salir_crear.pack()



def ver_pacientes():
    # Conectarse a la base de datos
    conexion = sqlite3.connect('audio.db')
    cursor = conexion.cursor()
    # Obtener los productos de la tabla
    cursor.execute('SELECT * FROM TBpacientes')
    productos = cursor.fetchall()
    conexion.close()
    # Crear la ventana de la tabla
    ventana_tabla = Toplevel()
    ventana_tabla.title('Pacientes registrados')
    tabla = ttk.Treeview(ventana_tabla)
    tabla.pack()
    tabla['columns'] = ('nombres', 'apellidos','edad', 'telefono', 'correo')
    tabla.heading('nombres', text='Nombres')
    tabla.heading('apellidos', text='Apellidos')
    tabla.heading('edad', text='Edad')
    tabla.heading('telefono', text='Telefono')
    tabla.heading('correo', text='Correo')
    # Agregar los productos a la tabla
    for producto in productos:
        tabla.insert('', 'end', text=producto[0], values=(producto[1], producto[2],producto[3],producto[4],producto[5]))

def seleccionar_paciente():
    # Conectarse a la base de datos
    conexion = sqlite3.connect('audio.db')
    cursor = conexion.cursor()
    # Obtener los productos de la tabla
    cursor.execute('SELECT * FROM TBpacientes')
    productos = cursor.fetchall()
    conexion.close()
    # Crear la ventana de selección de productos
    ventana_seleccion = Toplevel()
    ventana_seleccion.geometry("500x500")
    ventana_seleccion.title('Seleccionar paciente')
    etiqueta = Label(ventana_seleccion, text='Seleccione un paciente:')
    etiqueta.pack()
    lista_productos = Listbox(ventana_seleccion, height=20, width=50)
    lista_productos.pack()
    # Agregar los productos a la lista
    for producto in productos:
        lista_productos.insert(END, producto[1]+" "+producto[2])
    # Función para seleccionar un producto de la lista
    def seleccionar():
        seleccionado = lista_productos.get(lista_productos.curselection())
        global nombre
        nombre=seleccionado
        # Hacer algo con el producto seleccionado (por ejemplo, imprimirlo en la consola)
        print('Paciente seleccionado para iniciar examen:', nombre)
        
        ventana_seleccion.destroy()
        ventana.destroy()
    boton_seleccionar = tk.Button(ventana_seleccion, text="Seleccionar", bg="green", fg="black", command=seleccionar, width=20)

    
    boton_seleccionar.pack()
    
def salir():
    ventana.destroy()

# Crear botones
btn_crear = tk.Button(ventana, text="Crear nuevo paciente", bg="green", fg="black", command=crear_paciente, width=20)
btn_ver = tk.Button(ventana, text="Ver pacientes", bg="orange", fg="black", command=ver_pacientes, width=20)
btn_seleccionar = tk.Button(ventana, text="Seleccionar paciente", bg="yellow", fg="black", command=seleccionar_paciente, width=20)
btn_salir = tk.Button(ventana, text="Salir", bg="red", fg="black", command=salir, width=20)

# Posicionar los botones en la ventana
btn_crear.pack(pady=10)
btn_ver.pack(pady=10)
btn_seleccionar.pack(pady=10)
btn_salir.pack(pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
while True:
    if c_configuration == 1:
        if led_index==1:
            if volumen1==1:
                led_v1_1.on()
                led_v1_2.off()
                led_v1_3.off()
                sleep(0.2)
                led_v1_1.off()
                led_v1_2.off()
                led_v1_3.off()
            if volumen1==2:
                led_v1_1.on()
                led_v1_2.on()
                led_v1_3.off()
                sleep(0.2)
                led_v1_1.off()
                led_v1_2.off()
                led_v1_3.off()
            if volumen1==3:
                led_v1_1.on()
                led_v1_2.on()
                led_v1_3.on()
                sleep(0.2)
                led_v1_1.off()
                led_v1_2.off()
                led_v1_3.off()
        elif led_index==2:
            if volumen2==1:
                led_v2_1.on()
                led_v2_2.off()
                led_v2_3.off()
                sleep(0.2)
                led_v2_1.off()
                led_v2_2.off()
                led_v2_3.off()
            if volumen2==2:
                led_v2_1.on()
                led_v2_2.on()
                led_v2_3.off()
                sleep(0.2)
                led_v2_1.off()
                led_v2_2.off()
                led_v2_3.off()
            if volumen2==3:
                led_v2_1.on()
                led_v2_2.on()
                led_v2_3.on()
                sleep(0.2)
                led_v2_1.off()
                led_v2_2.off()
                led_v2_3.off()
        elif led_index==3:
            if volumen3==1:
                led_v3_1.on()
                led_v3_2.off()
                led_v3_3.off()
                sleep(0.2)
                led_v3_1.off()
                led_v3_2.off()
                led_v3_3.off()
            if volumen3==2:
                led_v3_1.on()
                led_v3_2.on()
                led_v3_3.off()
                sleep(0.2)
                led_v3_1.off()
                led_v3_2.off()
                led_v3_3.off()
            if volumen3==3:
                led_v3_1.on()
                led_v3_2.on()
                led_v3_3.on()
                sleep(0.2)
                led_v3_1.off()
                led_v3_2.off()
                led_v3_3.off()
        elif led_index==4:
            if volumen4==1:
                led_v4_1.on()
                led_v4_2.off()
                led_v4_3.off()
                sleep(0.2)
                led_v4_1.off()
                led_v4_2.off()
                led_v4_3.off()
            if volumen4==2:
                led_v4_1.on()
                led_v4_2.on()
                led_v4_3.off()
                sleep(0.2)
                led_v4_1.off()
                led_v4_2.off()
                led_v4_3.off()
            if volumen4==3:
                led_v4_1.on()
                led_v4_2.on()
                led_v4_3.on()
                sleep(0.2)
                led_v4_1.off()
                led_v4_2.off()
                led_v4_3.off()
        elif led_index==5:
            if volumen5==1:
                led_v5_1.on()
                led_v5_3.off()
                sleep(0.2)
                led_v5_1.off()
                led_v5_3.off()
            if volumen5==2:
                led_v5_1.on()
                led_v5_3.off()
                sleep(0.2)
                led_v5_1.off()
                led_v5_3.off()
            if volumen5==3:
                led_v5_1.on()
                led_v5_3.on()
                sleep(0.2)
                led_v5_1.off()
                led_v5_3.off()
    elif c_configuration==0:
        if volumen1==1:
            led_v1_1.on()
            led_v1_2.off()
            led_v1_3.off()
        if volumen1==2:
            led_v1_1.on()
            led_v1_2.on()
            led_v1_3.off()
        if volumen1==3:
            led_v1_1.on()
            led_v1_2.on()
            led_v1_3.on()
        if volumen2==1:
            led_v2_1.on()
            led_v2_2.off()
            led_v2_3.off()
        if volumen2==2:
            led_v2_1.on()
            led_v2_2.on()
            led_v2_3.off()
        if volumen2==3:
            led_v2_1.on()
            led_v2_2.on()
            led_v2_3.on()
        if volumen3==1:
            led_v3_1.on()
            led_v3_2.off()
            led_v3_3.off()
        if volumen3==2:
            led_v3_1.on()
            led_v3_2.on()
            led_v3_3.off()
        if volumen3==3:
            led_v3_1.on()
            led_v3_2.on()
            led_v3_3.on()
        if volumen4==1:
            led_v4_1.on()
            led_v4_2.off()
            led_v4_3.off()
        if volumen4==2:
            led_v4_1.on()
            led_v4_2.on()
            led_v4_3.off()
        if volumen4==3:
            led_v4_1.on()
            led_v4_2.on()
            led_v4_3.on()
        if volumen5==1:
            led_v5_1.on()
            led_v5_3.off()
        if volumen5==2:
            led_v5_1.on()
            led_v5_3.off()
        if volumen5==3:
            led_v5_1.on()
            led_v5_3.on()
    sleep(0.1)