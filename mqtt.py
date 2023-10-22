import paho.mqtt.client as mqtt
import json
import subprocess
import os

ipv4 = os.popen('ip addr show enp0s8 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()
#ipv6 = os.popen('ip addr show enp0s8 | grep "\<inet6\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()

print(ipv4)

broker_address="10.10.10.4" 
MQTT_TOPIC = ipv4

def on_connect(client, userdata, flags, rc):

    client.subscribe(MQTT_TOPIC)
    print("Conectado y suscrito ")

def on_message(client, userdata, message):

    #Se recibe el mensaje del payload
    m_decode=str(message.payload.decode("utf-8", "ignore"))

    #Convertimos el Json a Object
    m_in=json.loads(m_decode)

    #1 Debemos parar el proceso actual, que esta ejecutandose
    subprocess.call('pkill dotnet', shell=True)

    #2 Abrimos el archivo y sustituimos lo que hay en el JSON
    #   por lo que se nos ha enviado en el payload

    with open('/home/rodri/ghosts/config/timeline.json','w') as json_file:
        json.dump(m_in, json_file,indent=4)
        print("Fichero recibido")

    #3 Volvemos a arrancar el servicio GHOSTS
    subprocess.call('dotnet ~/ghosts/ghosts.client.linux.dll', shell=True)
    print("Mensaje recibido=",m_decode)
    print("Topic=",message.topic)
    print("Nivel de calidad [0|1|2]=",message.qos)
    print("Flag de retencion = ",message.retain)

#create new instance
print("creating new instance")
client = mqtt.Client("C3")

# Register publish callback function
client.on_connect = on_connect
client.on_message = on_message
print("connecting to broker")
client.connect(broker_address,2000)



client.loop_forever() 