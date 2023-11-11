import time
import random
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("test.mosquitto.org" , 1883, 60) #conectar servidos


topic = "sensor/presion"
topic2 = "sensor/humedad"
topic3 = "sensor/temperatura"


client.loop_start() # empezar bucle

try:
    while True:
        
        value = random.randint(1, 100) # valor aleatorio entre 1 y 100
        client.publish(topic, value) # publicar el valor aleatorio en el topico
        
        value2 = random.uniform(1, 10)
        value_real = format(value2, ".2f")
        client.publish(topic2, value_real)
        
        value3 = random.uniform(-100, 100)
        client.publish(topic3, value3)
        
        time.sleep(2) # tiempo de espera

#except KeyboardInterrupt:
    #client.loop_stop() # Detener el bucle de ne caso de interrupcion

finally:
    client.disconnect() # cerrar conexion con server mqtt 