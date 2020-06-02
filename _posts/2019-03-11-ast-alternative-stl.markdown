---
title: ":bug: alternative STL"
layout: post
date: 2019-03-11 18:15
tag: cpp
image: https://roseleblood.github.io/openess/Logo-OpenESS.png
headerImage: false
projects: true
hidden: true # don't count this post in blog pagination
description: "fast and alternative STL implantations for varios platform"
category: project
author: roseleblood
externalLink: false
---

---
# .:: aSTL - alternative STL ::.


##  Description
Eine etwas andere Standard Template Libary die viele Futures aus C# in C++ implantiert. Zum Beispiel event / delegates system.

## Weitere Futures:
    - string format function (std::frmstring(const char* fmt, ...); )
    - another stdout and stdin output see: examples/HelloWorld/main.cpp - class std::Console
    - hash functions see include/hash/hash.cpp
    - einfach zu portieren (see include/config.hpp und src/PLATFORM.cpp)

## Geplante Implantierungen:
    - network class for socket, tcp, udp
    - img load and save
    - network streams
    - thread and threadsafe

----

## Examples

_Example 1: Hello World_
```cpp

#include <nclude/string.hpp>
#include <include/iostream.hpp>
#include <include/stl.hpp>
#include <include/application.hpp>

#include <conio.h>

using namespace std;

class test : public Program
{
public:
    override int Main() {
        string var = string("Hello world");
        string outstring = std::frmstring( "%s from asSTL v. %s", var.c_str(), asstlVersion().c_str()  );
        Console::writeline(outstring);
        return 0;
     }
};
SET_PROGRAM(test);

```
_math -xample_

```cpp

#include <include/math/matrix4x4.hpp>
#include <include/iostream.hpp>
#include <include/application.hpp>
#include <conio.h>


using namespace std;

class test : public Program
{
public:
    override int Main() {
        vec2();
        vec3();
        vec4();

        std::math::mat4f mat = std::math::matrix4x4_identity<float>();

        std::Console::writeline( std::frmstring("mat4:\n%s" ,mat.to_string().c_str()) );

        return 0;
     }
private:
     void vec2() {
        std::math::vec2f a = std::math::vec2f(3,2);
        std::math::vec2f b = std::math::vec2f(1,2);
        std::math::vec2f c = a + b;

        std::Console::writeline(std::frmstring("vec2: %s + %s = %s" ,std::vec2_string(a).c_str(),
                std::vec2_string(b).c_str(), std::vec2_string(c).c_str()) );

        c = a * b;
        std::Console::writeline(std::frmstring("vec2: %s * %s = %s" , a.to_string().c_str(),
                 b.to_string().c_str(), c.to_string().c_str()) );

        c = a - b;
        std::Console::writeline(std::frmstring("vec2: %s - %s = %s" , a.to_string().c_str(),
                 b.to_string().c_str(), c.to_string().c_str()) );

         c = a / b;
        std::Console::writeline(std::frmstring("vec2: %s / %s = %s" , a.to_string().c_str(),
                 b.to_string().c_str(), c.to_string().c_str()) );
    }
    void vec3()  {
        std::math::vec3f a = std::math::vec3f(3,2,1);
        std::math::vec3f b = std::math::vec3f(1,2,3);
        std::math::vec3f c = a + b;

        std::Console::writeline(std::frmstring("vec3: %s + %s = %s" ,std::vec3_string(a).c_str(),
                std::vec3_string(b).c_str(), std::vec3_string(c).c_str()) );

        c = a * b;
        std::Console::writeline(std::frmstring("vec3: %s * %s = %s" , a.to_string().c_str(),
                 b.to_string().c_str(), c.to_string().c_str()) );

        c = a - b;
        std::Console::writeline(std::frmstring("vec3: %s - %s = %s" , a.to_string().c_str(),
                 b.to_string().c_str(), c.to_string().c_str()) );

         c = a / b;
        std::Console::writeline(std::frmstring("vec3: %s / %s = %s" , a.to_string().c_str(),
                 b.to_string().c_str(), c.to_string().c_str()) );
    }
    void vec4() {
        std::math::vec4f a = std::math::vec4f(3,2,1,0.5f);
        std::math::vec4f b = std::math::vec4f(1,2,3,4);
        std::math::vec4f c = a + b;

        std::Console::writeline(std::frmstring("vec4: %s + %s = %s" ,std::vec4_string(a).c_str(),
                std::vec4_string(b).c_str(), std::vec4_string(c).c_str()) );

        c = a * b;
        std::Console::writeline(std::frmstring("vec4: %s * %s = %s" , a.to_string().c_str(),
                 b.to_string().c_str(), c.to_string().c_str()) );

        c = a - b;
        std::Console::writeline(std::frmstring("vec4: %s - %s = %s" , a.to_string().c_str(),
                 b.to_string().c_str(), c.to_string().c_str()) );

         c = a / b;
        std::Console::writeline(std::frmstring("vec4: %s / %s = %s" , a.to_string().c_str(),
                 b.to_string().c_str(), c.to_string().c_str()) );
    }

};
SET_PROGRAM(test);

```

_Example 3: events_
```cpp

#include "../../include/string.hpp"
#include "../../include/string_utils.hpp"
#include "../../include/event.hpp"
#include "../../include/iostream.hpp"
#include "../../include/application.hpp"

#include <conio.h>

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
        std::Console::writeline("Server send message: ");
        MessageSent(this, p_msg);
    }
};


class test : public std::Program {
public:
    int Main() {
        Server server;

        server.MessageSent += new std::delegate<test, serverEventArgs>
                (this, &test::Server_OnMessageSent);
        server.MessageSent += new std::delegate<test, serverEventArgs>
                (this, &test::Server_OnMessageSent);
        server.MessageSent += new std::delegate<test, serverEventArgs>
                (this, &test::Server_OnMessageSent);

        server.SendMessage(serverEventArgs(std::string("Hallo C++ EventSystem")));

        std::Console::writeline("Bitte druecken Sie eine Taste ...");
        _getch();

        return 0;
    }
private:
    void Server_OnMessageSent(const std::object* sender, serverEventArgs msg) {
        static int iindex; iindex++;

        std::Console::writeline(std::frmstring("Client%d reach messages: %s",
                iindex, msg.getMessage().c_str()));
    }

};

SET_PROGRAM(test);


```



## Link
aSTL Projekt page: https://github.com/RoseLeBlood/aSTL/

## License
The MIT License (MIT)

Copyright (c) 2016 RoseLeBlood

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
