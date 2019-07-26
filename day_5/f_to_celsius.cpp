# include <iostream>

double f_to_celsius(double f_temp)
{
    return (f_temp - 32.0)/1.8;
}

int main(void)
{
	double f = 100.0;
	double c = f_to_celsius(f);
	std::cout << "F = " << f << "\nC = " << c << std::endl;

	return 0;
}