# include <iostream>

double f_to_celsius(double f_temp);   // this is function declaration.



double f_to_celsius(double f_temp)
{
    return (f_temp - 32.0)/1.8;
}

double celsius_to_f(double c_temp)
{
    return (c_temp * 9/5) + 32;
}

int main(void)
{

	double c = 37.7778;
	double f = celsius_to_f(c);
	std::cout << "F = " << f << "\nC = " << c << std::endl;

	return 0;
}