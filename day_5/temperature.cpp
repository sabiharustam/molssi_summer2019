
const double zero_k = 273.15;

double f_to_celsius(double f_temp)
{
    return (f_temp - 32.0)/1.8;
}

double celsius_to_f(double c_temp)
{
    return (c_temp * 9/5) + 32;
}

double celsius_to_kelvin(double c_temp)
{
    return c_temp + zero_k;
}

{
    double c_temp = f_to_celsius(f_temp);
    return celsius_to_kelvin(c_temp);
}