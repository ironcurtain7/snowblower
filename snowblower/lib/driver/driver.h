#pragma once
#include <Arduino.h>

class driver
{
public:
    void set_motors(int powerb, int powera);
    void motors_attach();
};