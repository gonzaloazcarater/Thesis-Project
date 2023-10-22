# %%
import json
import os
import random
# nota: Para que funcione todo, he tenido que eliminar "scenario":
# funcion para dada la topologia, que cree todo.
def cargardatos(path):
    with open(path, 'r') as f:
        topologia = json.load(f)
    return topologia

# %%
def getlan(vm):
    path = 'ejemplo_json_orquestador.json'
    datos = cargardatos(path)
    lans=[]
    for  x in datos:
        for y in datos[x]:
                for z in datos[x][y]:
                    if not "server" in datos[x][y][z]["vm_name"]:
                        lan=datos[x][y][z]['accesibles_vms']
                        lans.append(lan)
                        
    return lan 
# idea1: pasar como parametro una vm que haga que en funcion de la vm saque las lans
# idea2: hacerlo como ahora y uan vez se crea el archivo comprobar el campo command 
# idea3: previo crear el archvio definir ahi la set de lans posibles que pueden servir.


# %%
# función para sacar las direcciones ips de los servers
def getipdir():
    path = 'ejemplo_json_orquestador.json'
    #path='ejemplo_topologia_mario.json'
    datos = cargardatos(path)
    vardirs=[]
    for  x in datos:
        for y in datos[x]:
                for z in datos[x][y]: 
                    #if "server" in datos[x][y][z]["vm_name"]:
                        vardir=datos[x][y][z]['ip_dir'] 
                        vardirs.append(vardir)
    
    return vardirs

# %%
# celda para crear el fichero json.
import json
varser= getipdir()# variable para guardar las direciones de los server.
ftimeline=[]# lista para incluir todos los ficheros timeline que creemos.
frutas=[]#lista para meter aqui las rutas absolitas
frutassin=[]
var1= random.randint(1,4)
varclx=['curl','wget','scp','ssh']#acomandos aparte del ping para realizar a una direccion de un server desde un terminal limux
varcws=['curl','scp','ssh']#acomandos aparte del ping para realizar a una direccion de un server.

#rutas
pathws='C:\\Users\\gonza\\Downloads\\TFG\\Archivos'
pathlx='FicherosTFG'


#servicio:conectarse  a una pagina web
websites=['http://www.etsit.upm.es/','https://www.marca.com/','https://www.lab.dit.upm.es/','https://www.youtube.com/']

#servicio: descargarse imagenes
images=['https://www.dit.upm.es/images/dit08.gif','https://cutt.ly/KGpOBJF','https://hlassets.paessler.com/common/files/infographics/mqtt-architecture.png','https://www.muycomputer.com/wp-content/uploads/2014/07/CMD.jpg']


#subir imagines
imgup1=['https://www.muycomputer.com/wp-content/uploads/2014/07/CMD.jpg & imgur-uploader CMD.jpg']
imgup2=['https://www.dit.upm.es/images/dit08.gif & imgur-uploader dit08.gif']
imgup=[imgup1,imgup2]


#servicio: instalar aplicaciones
appws=['pdfforge.PDFCreator','RARLab.WinRAR','raimo.Smallpdf']
applx=['pinball','vim','filezilla']


#servicio: descarga torrentl
torrent=["https://cutt.ly/HHaUjJT","https://blazing.network/torrents/musica/BushTheKingdomDeluxe.torrent"]

var3=random.randint(100,1000)# variable para asignar a delay after y delay before.

def creararchivo(ruta,datos):

    ftimeline=[]# lista para incluir todos los ficheros timeline que creemos.
    frutas=[]#lista para meter aqui las rutas absolitas
    frutassin=[]
    
    #datos: dentro de cada vm , nos permite acceder a cualqueira de sus atributos.

    varlan=random.choice(datos['accesibles_vms']) # guarda una direcciona aleatoria de las accesibles.
    print(datos['accesibles_vms'])
    
    for i in range(5):
        
        #parte del archvio timeline que estara presente en todos y sera igual para todos.

        timeline={
            "Id": "40e666f6-24f9-4cf7-907a-f28a8cf90d32",
            "Status": "Run",
            "TimeLineHandlers": [
                {
                    "HandlerType": "Command",
                    "Initial": "",
                    "UtcTimeOn": "00:00:00",
                    "UtcTimeOff": "24.00:00:00",
                    "Loop": True,
                    "TimeLineEvents": [
                        
                    ]
                }
            ]
        }
        for j in range(random.randint(2,5)):

            # parte del codigo oara añadir un ping.   
            timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                {
                    "TrackableId": None,
                    "Command": "ping -c {} {}".format(random.randint(1,6), varlan),
                    "CommandArgs": [],
                    "DelayAfter": random.randint(100,1000),
                    "DelayBefore": random.randint(100,1000)
                }
            )

            #visitar una pagina web en chrome
            timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                {
                    "TrackableId": None,
                    "Command": "start chrome /incognito  {}".format(random.choice(websites)),
                    "CommandArgs": [],
                    "DelayAfter": random.randint(100,1000),
                    "DelayBefore": random.randint(100,1000)
                }
            )

            #streaming de audio a traves de vlc            
            timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                {
                    "TrackableId": None,
                    #"Command": "vlc -vvv -I dummy {} --sout '#standard{access=http,mux=ogg,dst=localhost:8080}' ".format(os.path.join(pathws,"\Prueba3.mp4")),
                    "CommandArgs": [],
                    "DelayAfter": random.randint(100,1000),
                    "DelayBefore": random.randint(100,1000)
                }
            ) 

            #jugar a un juego online            
            timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                {
                    "TrackableId": None,
                    "Command": "ssh sshtron.zachlatta.com",
                    "CommandArgs": [],
                    "DelayAfter": random.randint(100,1000),
                    "DelayBefore": random.randint(100,1000)
                }
            )           

            if datos['type_of_OS']=='LINUX':

            #parte del codigo para añadir uno de los comandos de varc si el os es LINUX.
                if random.randint(1,4)==1 or random.randint(1,4)==3 :
                    timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                        {
                            "TrackableId": None,
                            "Command": "{} {}".format(random.choice(varclx),random.choice(varser)),
                            "CommandArgs": [],
                            "DelayAfter": random.randint(100,1000),
                            "DelayBefore": random.randint(100,1000)
                        }
                    ) 

                            #servicio de instalar app en linux
                    timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                        {
                            "TrackableId": None,
                            "Command": "sudo apt-get update & sudo apt-get install{}".format(applx),
                            "CommandArgs": [],
                            "DelayAfter": random.randint(100,1000),
                            "DelayBefore": random.randint(100,1000)
                        }
                    )    
                            #servicio de torrent en linux
                    timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                        {
                            "TrackableId": None,
                            "Command": "transmission-cli {}".format(torrent),
                            "CommandArgs": [],
                            "DelayAfter": random.randint(100,1000),
                            "DelayBefore": random.randint(100,1000)
                        }
                    )   

                            #subir imagen en lx
                    timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                        {
                            "TrackableId": None,
                            "Command": "wget {}".format(random.choice(imgup)),
                            "CommandArgs": [],
                            "DelayAfter": random.randint(100,1000),
                            "DelayBefore": random.randint(100,1000)
                        }
                    )   

                            #crear y unirse videollamada
                    timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                        {
                            "TrackableId": None,
                            "Command": "meet -o",
                            "CommandArgs": [],
                            "DelayAfter": random.randint(100,1000),
                            "DelayBefore": random.randint(100,1000)
                        }
                    )
                            #speedtest
                    timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                        {
                            "TrackableId": None,
                            "Command": "speedtest-cli",
                            "CommandArgs": [],
                            "DelayAfter": random.randint(100,1000),
                            "DelayBefore": random.randint(100,1000)
                        }
                    )                    
                            #medicion con iperf
                    timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                        {
                            "TrackableId": None,
                            "Command": "iperf -c{}".format(varlan),
                            "CommandArgs": [],
                            "DelayAfter": random.randint(100,1000),
                            "DelayBefore": random.randint(100,1000)
                        }
                    )                    

            #caso de comandos que son diferente si el tipo de sisteam operativo es windows
            else: 
                if random.randint(1,4)==2 or random.randint(1,4)==4 :
                    timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                        {
                            "TrackableId": None,
                            "Command": "{} {}".format(random.choice(varcws),random.choice(varser)),
                            "CommandArgs": [],
                            "DelayAfter": random.randint(100,1000),
                            "DelayBefore": random.randint(100,1000)
                        }
                    )   
                            #servicio de instalar app en windows
                    timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                        {
                            "TrackableId": None,
                            "Command": "winget upgrade & winget install {}".format(appws),
                            "CommandArgs": [],
                            "DelayAfter": random.randint(100,1000),
                            "DelayBefore": random.randint(100,1000)
                        }
                    )
                            #servicio torrent en windows
                    timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                        {
                            "TrackableId": None,
                            "Command": "aria2c {}".format(torrent),
                            "CommandArgs": [],
                            "DelayAfter": random.randint(100,1000),
                            "DelayBefore": random.randint(100,1000)
                        }
                    )
                            #subir imagen en ws
                    timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                        {
                            "TrackableId": None,
                            "Command": "curl -O {}".format(random.choice(imgup)),
                            "CommandArgs": [],
                            "DelayAfter": random.randint(100,1000),
                            "DelayBefore": random.randint(100,1000)
                        }
                    )
                           #medicion con iperf
                    timeline["TimeLineHandlers"][0]["TimeLineEvents"].append(
                        {
                            "TrackableId": None,
                            "Command": "iperf3 -c{}".format(varlan),
                            "CommandArgs": [],
                            "DelayAfter": random.randint(100,1000),
                            "DelayBefore": random.randint(100,1000)
                        }
                    )                                                                   

            print(os.getcwd())
        
            print('Archivo {} creado'.format(i +1))
        ruta_archivo = os.path.join(ruta, "timeline{}.json".format(i+1))
        if ruta not in frutassin:
            frutassin.append(ruta)
        frutas.append(ruta_archivo)
        print(frutas)
       
        with open(ruta_archivo,"w") as f:
            f.write(json.dumps(timeline,indent=4))
        # creacion de los ficheros timeline
    
    ftimeline.append(timeline) #agrupacion de todos los archviso timeline
    #print(ftimeline)


# %%
def parser():
    # crear carpeta por cada LAN y Vm que encuentre.
    import sys
    import os
    #path = sys.argv[1]# guarda el segundo argumento que le pasemos.
    path = 'ejemplo_json_orquestador.json'
    #path='ejemplo_topologia_mario.json'
    datos = cargardatos(path)

    for i in datos:

        if not os.path.exists(i):#
            #condicion para que no la cree si ya existe
            os.mkdir(i)# creamos la primera carpeta.
        
        for j in datos[i]:

            path = os.path.join(i, j) # con join "unimos" el directorio actual en uno solo.
            
            if not os.path.exists(path):
                os.mkdir(path)
                #creamos la primera subcarpeta
                print(path)
            
            for k in datos[i][j]:

                path = os.path.join(i,j,k)
                if not os.path.exists(path):
                    #comprobar si name es server o no.

                    if not "SERVER" in datos[i][j][k]["type_of_vm"]:
                        
                        os.mkdir(path) 
                        #crea la ultima subcarpeta
                        
                        creararchivo(path,datos[i][j][k])
                        #llamamos a creararchivo pasandole la ruta y  los atriubutos de cada vm.
                        # se escoge aletoriamente uno de esos archvios y se envia sobre mqtt
                       
                        ruta=random.choice(frutas)
                        print(ruta)
                        fichero=random.choice(os.listdir(path))
                        print(fichero)
                    
parser()

# %%
import shutil
shutil.rmtree('scenario')
#shutil.rmtree('001-Terraform_COBRA')


# %%
# parte osquestador
#se necesita un topic para envair el menaje sobre MQTT
#publicar un fichero en un topic con un identiifcador con esa IP
#import paho.mqtt.client as mqtt #import the client1
import paho.mqtt.client as mqtt
MQTT_HOST = "localhost"
MQTT_TOPIC = ""
MQTT_MSG=json.dumps('timeline1.json');



#varser= getserverdir()# variable para guardar las direciones de los server.

#parte 1 publicador : orquestador envia mensaje
# Define on_publish event function
def on_publish(client, userdata, mid):
    print ("Message Published")

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC)
    client.publish(MQTT_TOPIC, MQTT_MSG)
#suscriptor se suscribe al topic
def on_message(client, userdata, message):
    #Se recibe el mensaje del payload
    m_decode=str(message.payload.decode("utf-8", "ignore"))

    #Convertimos el Json a Object
    m_in=json.loads(m_decode)

    #1º Debemos parar el proceso actual, que esta ejecutandose
    subprocess.call('pkill dotnet', shell=True)

    #2º Abrimos el archivo y sustituimos lo que hay en el JSON
    #   por lo que se nos ha enviado en el payload

    with open('~/ghosts/config/timeline.json', 'w') as json_file:
        json.dump(m_in, json_file)
        
    #3º Volvemos a arrancar el servicio GHOSTS
    subprocess.call('dotnet ~/ghosts/ghosts.client.linux.dll', shell=True)
    print("Mensaje recibido=",m_decode)
    print("Topic=",message.topic)
    print("Nivel de calidad [0|1|2]=",message.qos)
    print("Flag de retención =",message.retain)

    #broker_address="broker.hivemq.com" 
    broker_address="localhost" 


    #create new instance
    print("creating new instance")
    client = mqtt.Client("P1")

# Register publish callback function
    client.on_publish = on_publish
    client.on_connect = on_connect
    client.on_message = on_message
    print("connecting to broker")
    client.connect(broker_address)
    #start the loop
    client.loop_start()
    # Loop forever
    client.loop_forever()    
    print("Subscribing to topic","/mqtt/prueba/escenario1")
    client.subscribe("/mqtt/prueba/escenario1")




# %%
for i in range(5):
    print(i)



