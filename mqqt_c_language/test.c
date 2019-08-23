#include "MQTTClient.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    printf("Hello world !");
    /* Now we can create a client object  */
    MQTTClient client;
    rc = MQTTClient_create(&client, url, clientid, MQTTCLIENT_PERSISTENCE_NONE, NULL);
    rc = MQTTClient_receive(client, topicName, topicLen, message, timeout);
    
    return 0;
}
