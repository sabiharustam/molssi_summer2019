# include <iostream>
# include "temperature.hpp"


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
    for(int i = 0; i < max; i++)
    // first is initialization, second is test, third is what to execute.
    // what this function does is it will print i in every step till
    // i reaches the max.
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