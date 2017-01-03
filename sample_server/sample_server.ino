#include <ESP8266WiFi.h>          //ESP8266 Core WiFi Library (you most likely already have this in your sketch)

#include <DNSServer.h>            //Local DNS Server used for redirecting all requests to the configuration portal
#include <ESP8266WebServer.h>     //Local WebServer used to serve the configuration portal
#include <WiFiManager.h>          //https://github.com/tzapu/WiFiManager WiFi Configuration Magic

ESP8266WebServer server(80);


void setup() {
  //Console logs at 9600 baud rate
  Serial.begin(9600);
  Serial.println("Hello World");

  //Create a wifi hotspot
  WiFiManager wifiManager;
  wifiManager.autoConnect("ESP8266 wifi");

  //Starting a server
  server.begin();
  Serial.println("Server started");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  
  server.on("/", handle_root); 
}

void handle_root(){  
  pinMode(get_pin(), OUTPUT);
  digitalWrite(get_pin(), get_state());
  server.send(200, "text/plain", server.arg("pin") +" - "+ String(get_pin()) + " is now on "+ String(digitalRead(get_pin())));
}

int get_pin(){
  String pin=server.arg("pin");

  if(pin=="D0"){
   return D0; 
  }else if(pin=="LED_BUILTIN"){
   return LED_BUILTIN; 
  }else if(pin=="D1"){
   return D1; 
  }else if(pin=="D2"){
   return D2; 
  }else if(pin=="D3"){
   return D4; 
  }else if(pin=="D4"){
   return D4; 
  }else if(pin=="D5"){
   return D5; 
  }else if(pin=="D6"){
   return D6; 
  }else if(pin=="D7"){
   return D6; 
  }else if(pin=="D8"){
   return D6; 
  }  
  return D0;   
}

int get_state(){
  String state=server.arg("state");
  if(state=="high"){
   return HIGH; 
  }else if(state=="low"){
   return LOW; 
  }
  return LOW;   
}

// the loop function runs over and over again forever
void loop() {
  server.handleClient();
}
