# include <iostream>

const double zero_k = 273.15;

double f_to_celsius(double f_temp);   // this is function declaration.



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

double f_to_kelvin(double f_temp)
{
    double c_temp = f_to_celsius(f_temp);
    return celsius_to_kelvin(c_temp);
}

// Function returns false if f_temp is unpysical.
bool check_temperature(double f_temp)
{
    double k = f_to_kelvin(f_temp);
    if (k <= 0.0 || k > 1.0e6)
        return false;

    else
        return true;
}

void count(int max)
{
    for(int i = 0; i < max; i++)   // first is initialization, second is test, third is what
        std::cout << "i is" << i << std::endl;
    // i++ is equal to i+=1 or ++i is the same.
}

int main(void)
{
    count(100);
	double c = 37.7778;
	double f = celsius_to_f(c);
	double k = f_to_kelvin(f);
	std::cout << "F = " << f << "\nC = " << c << "\nK = " << k << std::endl;

	return 0;
}