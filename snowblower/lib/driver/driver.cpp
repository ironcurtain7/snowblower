#include <driver.h>
void driver::motors_attach()
{
    pinMode(27, OUTPUT);
    pinMode(14, OUTPUT);
    pinMode(32, OUTPUT);
    pinMode(33, OUTPUT);
}

void driver::set_motors(int powerb, int powera)
{
    // управление левым мотором
    if (powera == 0)
    {
        analogWrite(27, 0);
        analogWrite(14, 0);
    }
    else if (powera > 0)
    {

        analogWrite(27, 0);
        analogWrite(14, powera);
    }
    else
    {
        analogWrite(14, 0);
        analogWrite(27, abs(powera));
    }
    // управление правым мотором
    if (powerb == 0)
    {
        analogWrite(33, 0);
        analogWrite(32, 0);
    }
    else if (powerb > 0)
    {

        analogWrite(33, 0);
        analogWrite(32, powerb);
    }
    else
    {
        analogWrite(32, 0);
        analogWrite(33, abs(powerb));
    }
}
