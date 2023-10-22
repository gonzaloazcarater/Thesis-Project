# parte osquestador
#se necesita un topic para envair el menaje sobre MQTT
#publicar un fichero en un topic con un identiifcador con esa IP
#import paho.mqtt.client as mqtt #import the client1
import paho.mqtt.client as mqtt
import json
import watchdog
import random
import os
import parserv4
MQTT_HOST = "localhost"

MQTT_TOPIC = "prueba/1"

def escoger_archivo():
    rutas=parserv4.frutassin
    #random.shuffle(rutas)
    for dir in rutas:

        ficheros=os.listdir(dir)
        random.shuffle(ficheros)
        
        for f in ficheros:
            mensaje=json.dumps('dir + f')

def get_topic():
    print()
#parte 1 publicador : orquestador envia mensaje
# Define on_publish event function
def on_publish(client, userdata, mid):
    print ("Message Published")

#broker_address="broker.hivemq.com" 
#revisar que el puerto  1883 esta escuchando a la ip de la maquina final.(listerner1883)
broker_address="localhost" 


#crear un cliente
print("creating new instance")
client = mqtt.Client("P1")

# Register publish callback function
client.on_publish = on_publish
print("connecting to broker")
client.connect(broker_address)
#start the loop
client.loop_start()
# Loop forever 
#print("Subscribing to topic","/prueba1")
#client.subscribe("ipmaquina")
