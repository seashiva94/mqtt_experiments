# MQTT Setup

MQTT is a commonly used lightweight data agnostic protocol for IoT devices. It can be easily use for comunication between the devices.
MQTT uses a client-server based publish/subscribe model, where clients publish messages to a topic on the broker (server)
or subscribe to topics on the broker to recieve messages related to that topic.

## Advantages of using MQTT

* MQTT provides various levels of Quality of service that can be used as per the requirements.
* It allows for arbitrary number of devices to be conteolled easily
* It avoids time spent in sending web requests and responses using the traditional HTTP protocol
* It can be used to easily monitor the network by looking at al messages
* Data can be secured by using TLS/SSL security
* It allows integration with other services like apache storm, and ELK stack easily
* Many enterprise servers exist like Hive MQ that allow applicatoin to be scaled up
* It allows various devices using different platform to communicate seemlessly
* Various services can be used for visualisation (eg Kibana) or making dashboards for apps (eg mqtt dashboard)

## Our Setup

![dendrite setup](https://github.com/seashiva94/mqtt_experiments/blob/master/mqtt%20preesentation/dendritesetup.pdf)

* The MQTT subscribers running on the raspberry pis subscribe to the broker and listen for commands
* The publisher connects to the broker and sends messages to the raspberr pis
* The publisher sends the message in response to some event that it observes.
* The dendrites are connected to the individual battery packs via relays controlled by the raspberry pis using the dendrite class
* The dendrites can be controlled by turning the relay on or off as per the message recieved.

## Requirements

* Dendrites 
* raspberry pi setup with rasspbian OS and grovepi hat
* setup grovepi on the raspberry pis (grovepi setup instructions by dexter industries)
* grove relays
* install cloudmesh.pi on the raspberry pis to easiily interface with a variety of grove sensors (clougmesh.pi github page)
* setup paho-mqtt client for python on raspberry pis ( run pip install paho-mqtt )
* a local machine running MQTT broker (or use iot.eclipse.org server for testing) and paho-mqtt client to run pblisher
* connect all devices to the same wireless local network
