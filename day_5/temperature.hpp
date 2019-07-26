
#pragma once

double f_to_celsius(double f_temp);
double celsius_to_f(double c_temp);
double celsius_to_kelvin(double c_temp);
double f_to_kelvin(double f_temp);

bool check_temperature(double f_temp)
{
    double k = f_to_kelvin(f_temp);
    if (k <= 0.0 || k > 1.0e6)
        return false;

    else
        return true;
}
