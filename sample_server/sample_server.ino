#include <ESP8266WiFi.h>          //ESP8266 Core WiFi Library (you most likely already have this in your sketch)

#include <DNSServer.h>            //Local DNS Server used for redirecting all requests to the configuration portal
#include <ESP8266WebServer.h>     //Local WebServer used to serve the configuration portal
#include <WiFiManager.h>          //https://github.com/tzapu/WiFiManager WiFi Configuration Magic
ESP8266WebServer server(80);
/*
 ESP8266 Blink by Simon Peter
 Blink the blue LED on the ESP-01 module
 This example code is in the public domain
 
 The blue LED on the ESP-01 module is connected to GPIO1 
 (which is also the TXD pin; so we cannot use Serial.print() at the same time)
 
 Note that this sketch uses LED_BUILTIN to find the pin with the internal LED
*/

void handle_root() {
 server.send(200, "text/plain", "Hello from Venkat");
 delay(100);
}

void setup() {
  Serial.begin(9600);
  Serial.println("Hello fuckers");
  WiFiManager wifiManager;
  wifiManager.autoConnect("Abhay");
  // Wait for connection

server.begin();
  Serial.println("Server started");
  
  server.on("/", handle_root);
  Serial.println("Not connected4");
  server.on("/name", []() {
  String state= server.arg("name");
  server.send(200, "text/plain", "Led is now " + state);
  }); 
}

// the loop function runs over and over again forever
void loop() {
  server.handleClient();
}
