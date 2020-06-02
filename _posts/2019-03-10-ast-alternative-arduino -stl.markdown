---
title: ":bug: alternative STL Arduino port"
layout: post
date: 2019-03-10 17:49
tag: Arduino
image: https://roseleblood.github.io/openess/Logo-OpenESS.png
headerImage: false
projects: true
hidden: true # don't count this post in blog pagination
description: "fast and other STL Arduino Port"
category: project
author: roseleblood
externalLink: false
---

---
### .:: aSTLino - alternative STL Arduino port ::.
Eine etwas andere Standard Template Libary die viele Futures aus C# in C++ implantiert. Zum Beispiel event / delegates system

----

## Examples

_blink.ino_

```cpp
#include <aSTLino.h>
#include <arduino/rgb_strip.hpp>
#include <arduino/stream.hpp>


arduino::digitalOut<13> led;

void setup() {
  led.begin();

  Serial.begin(9600);
  Serial << led.to_string() << endl;
}

void loop() {
  led.write(false);
  delay(250);
  led.write(true);
  delay(250);
}
```
_blink_without_delay.ino_

```cpp
#include <aSTLino.h>
#include <arduino/elapsedTimer.hpp>
#include <arduino/rgb_strip.hpp>
#include <arduino/stream.hpp>

class BlinkWithoutDelay {
  public:
    BlinkWithoutDelay()  {
      m_timer = arduino::elapsedTimer(std::string("test"), 1000);
    }
    void begin() {
      m_timer.OnElapsed += new std::delegate<BlinkWithoutDelay, arduino::timerEventArgs>(this,    &BlinkWithoutDelay::onTimer_elapsed);
      m_timer.begin();
      m_led.begin();
    }
    void update() {
      m_timer.update();
    }
    void onTimer_elapsed(const std::object *object, arduino::timerEventArgs args) {
      m_ledStatus = !m_ledStatus;
      m_led.write(m_ledStatus);
    }
  private:
    arduino::elapsedTimer m_timer;
    arduino::digitalOut<13> m_led;
    bool m_ledStatus;
};

BlinkWithoutDelay test;

void setup() {
  test.begin();
}
void loop () {
  test.update();
}

```
_led_strip.ino_

```cpp
#include <aSTLino.h>
#include <arduino/rgb_strip.hpp>
#include <arduino/stream.hpp>
#include <math/vector3.hpp>
#include <arduino/eeprom.hpp>

//#define EEPROM_CLEAR 0

arduino::rgb_strip<5,6,3, false> ledstrip; // pin, pin, pin, invert?
arduino::digitalOut<13> led;

void setup() {
  Serial.begin(9600);
  #ifdef EEPROM_CLEAR
    arduino::eeprom::clear();
    arduino::eeprom::write(std::math::color<float>(0,0,255,128), 1);
    while(true) {}
  #endif

  led.begin();
  ledstrip.begin();

  std::math::color<float> f;
  arduino::eeprom::read(f, 1);

  ledstrip.color(f);

}
void loop() {
   led.write(false);
   while (Serial.available() ) {
     led.write(true);

     int r = Serial.parseInt(); r = (r >255) ? 255 : (r < 0) ? 0 : r;
     int g = Serial.parseInt(); g = (g >255) ? 255 : (g < 0) ? 0 : g;
     int b = Serial.parseInt(); b = (b >255) ? 255 : (b < 0) ? 0 : b;
     int a = Serial.parseInt(); a = (a >255) ? 255 : (a < 0) ? 0 : a;

     ledstrip.fade_color(std::math::color<float>(r, g, b, a), 0.1f, 150);

     arduino::eeprom::write(ledstrip.color(), 1);
     Serial << ledstrip.to_string() << endl;
   }
}
```

_event.ino_
```cpp
#include <aSTLino.h>

#include <string.hpp>
#include <math/matrix4x4.hpp>
#include <event.hpp>

class serverEventArgs : public std::eventArgs {
public:
   serverEventArgs(std::string msg)  { m_msg = msg; }
   std::string getMessage() { return m_msg; }
private:
    std::string m_msg;
};
class Server : public std::object
{
public:
    std::event<serverEventArgs> MessageSent;

    void SendMessage(serverEventArgs p_msg)
    {
        MessageSent(this, p_msg);
    }
};
class EventTest {
  public:
    void run() {
        Server server;

        server.MessageSent += new std::delegate<EventTest, serverEventArgs>
                (this, &EventTest::Server_OnMessageSent);
        server.MessageSent += new std::delegate<EventTest, serverEventArgs>
                (this, &EventTest::Server_OnMessageSent);
        server.MessageSent += new std::delegate<EventTest, serverEventArgs>
                (this, &EventTest::Server_OnMessageSent);

        server.SendMessage(serverEventArgs(std::string("Hallo C++ EventSystem")));
    }
  protected:
    void Server_OnMessageSent(const std::object* sender, serverEventArgs msg) {
         Serial.print("Reach message from Server: ");
         Serial.println(msg.getMessage().c_str());
    }
};
////------------------------------
EventTest eventTest;

void setup() {
  Serial.begin(9600);
}

void loop() {
  std::string var = std::string("Hello world");
  Serial.print(var.c_str()); Serial.print(" from aSTL v. "); Serial.println(std::asstlVersion().c_str() );

  eventTest.run();

  while(true) {}
}
```

## Link
aSTLino Projekt page: https://github.com/RoseLeBlood/aSTLino/

## License
The MIT License (MIT)

Copyright (c) 2016 RoseLeBlood

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
