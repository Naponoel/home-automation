/* 
 * - - - - - [libraries] - - - - - - 
 *  URL-i za library-e:
 *  https://github.com/knolleary/pubsubclient
 *  http://arduino.esp8266.com/stable/package_esp8266com_index.json
 * - - - - - [MQTT] - - - - - - - - 
 * Imena soba:
 *  --> Vidi .dwg
 * Format MQTT topic-a:
 * /<soba>/naredbe
 * /<soba>/feedback
*/

#include <PubSubClient.h>
#include <ESP8266WiFi.h>

// WiFi i VPS
const char* remote_vps_ip = "172.105.76.166";
const char* lan_access_point_ssid = "Wifac";
const char* lan_access_point_password = "heksa4389px20";

// GPIO i MQTT
const int lightPin = 2;
char* lightTopic = "/soba/light1";


WiFiClient wifiClient;

void callback(char* topic, byte* payload, unsigned int length);

PubSubClient client(remote_vps, 1883, callback, wifiClient);

void setup() {
  //initialize the light as an output and set to LOW (off)
  pinMode(lightPin, OUTPUT);
  digitalWrite(lightPin, LOW);

  //start the serial line for debugging
  Serial.begin(115200);
  delay(100);


  //start wifi subsystem
  WiFi.begin(ssid, password);
  //attempt to connect to the WIFI network and then connect to the MQTT server
  reconnect();

  //wait a bit before starting the main loop
      delay(2000);
}



void loop(){

  //reconnect if connection is lost
  if (!client.connected() && WiFi.status() == 3) {reconnect();}

  //maintain MQTT connection
  client.loop();

  //MUST delay to allow ESP8266 WIFI functions to run
  delay(10); 
}


void callback(char* topic, byte* payload, unsigned int length) {

  //convert topic to string to make it easier to work with
  String topicStr = topic; 

  //Print out some debugging info
  Serial.println("Callback update.");
  Serial.print("Topic: ");
  Serial.println(topicStr);

  //turn the light on if the payload is '1' and publish to the MQTT server a confirmation message
  if(payload[0] == '1'){
    digitalWrite(lightPin, HIGH);
    client.publish("/test/confirm", "Light On");

  }

  //turn the light off if the payload is '0' and publish to the MQTT server a confirmation message
  else if (payload[0] == '0'){
    digitalWrite(lightPin, LOW);
    client.publish("/test/confirm", "Light Off");
  }

}




void reconnect() {

  //attempt to connect to the wifi if connection is lost
  if(WiFi.status() != WL_CONNECTED){
    //debug printing
    Serial.print("Connecting to ");
    Serial.println(ssid);

    //loop while we wait for connection
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }

    //print out some more debug once connected
    Serial.println("");
    Serial.println("WiFi connected");  
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
  }

  //make sure we are connected to WIFI before attemping to reconnect to MQTT
  if(WiFi.status() == WL_CONNECTED){
  // Loop until we're reconnected to the MQTT server
    while (!client.connected()) {
      Serial.print("Attempting MQTT connection...");

      // Generate client name based on MAC address and last 8 bits of microsecond counter
      String clientName;
      clientName += "esp8266-";
      uint8_t mac[6];
      WiFi.macAddress(mac);
      clientName += macToStr(mac);

      //if connected, subscribe to the topic(s) we want to be notified about
      if (client.connect((char*) clientName.c_str())) {
        Serial.print("\tMTQQ Connected");
        client.subscribe(lightTopic);
      }

      //otherwise print failed for debugging
      else{Serial.println("\tFailed."); abort();}
    }
  }
}

//generate unique name from MAC addr
String macToStr(const uint8_t* mac){

  String result;

  for (int i = 0; i < 6; ++i) {
    result += String(mac[i], 16);

    if (i < 5){
      result += ':';
    }
  }

  return result;
}
