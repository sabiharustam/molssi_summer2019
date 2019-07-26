# include <iostream>

double f_to_celsius(double f_temp);   // this is function declaration.

int main(void)
{
	double f = 100.0;
	double c = f_to_celsius(f);
	std::cout << "F = " << f << "\nC = " << c << std::endl;

	return 0;
}

double f_to_celsius(double f_temp)
{
    return (f_temp - 32.0)/1.8;
}