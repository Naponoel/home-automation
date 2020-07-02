#include <PubSubClient.h>

/* 
 *  URL-i za library-e:
 *  https://github.com/knolleary/pubsubclient
 *  http://arduino.esp8266.com/stable/package_esp8266com_index.json
*/

#include <PubSubClient.h>
#include <ESP8266WiFi.h>

#define mqtt_broker "192.168.1.101"
String ssid = "TP-Link_2BC6";
String password = "83911903";
const char* client_ID = "zfk5g";
char* lightTopic = "/test/light1";
const int lightPin = 2;

int status = WL_IDLE_STATUS;

WiFiClient WiFi_cli;

void callback(char* topic, byte* payload, unsigned int length);
PubSubClient MQTT_cli(mqtt_broker, 1883, callback, WiFi_cli);

// Setup se vrti samo jednom pri RST ESP-a
void setup() {
  delay(5000);
  
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  connect_or_reconnect();
  }

void connect_or_reconnect() {
  // WiFi Connection
  if (WiFi.status() != WL_CONNECTED) {
    Serial.print("Trying WiFi connection with: '" + (String)ssid + "' access point");

    while ( WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(" . ");
      }
      
    Serial.print("\nWiFi connection\t\tOK\n");
    }

  // MQTT Connection
  if(WiFi.status() == WL_CONNECTED){
    while (!MQTT_cli.connected()) {
      Serial.print("\nTrying MQTT connection with: '" + (String)mqtt_broker + "'");
      if (MQTT_cli.connect(client_ID)) {
        Serial.print("\nMQTT connection\t\tOK\n");
        //client.subscribe(lightTopic);
        }
      }
    }
  }
  
void callback(char* topic, byte* payload, unsigned int length) {
  String topicStr = topic; 
  //Print out some debugging info
  Serial.println("Callback update.");
  Serial.print("Topic: ");
  Serial.println(topicStr);

  //turn the light on if the payload is '1' and publish to the MQTT server a confirmation message
  if(payload[0] == '1'){
    digitalWrite(lightPin, HIGH);
    MQTT_cli.publish("/test/confirm", "Light On");

    }

  //turn the light off if the payload is '0' and publish to the MQTT server a confirmation message
  else if (payload[0] == '0'){
    digitalWrite(lightPin, LOW);
    MQTT_cli.publish("/test/confirm", "Light Off");
    }
  }
  
// Loop je while True petlja kontroler-a
void loop() {
  if (!MQTT_cli.connected() && WiFi.status() == 3) {
    connect_or_reconnect();
    }
  MQTT_cli.loop();
  delay(10); 
}
