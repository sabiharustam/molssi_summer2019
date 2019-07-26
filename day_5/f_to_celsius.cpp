# include <iostream>
# include <vector>
# include "temperature.hpp"


int main(void)
{
    std::vector<double> my_vector;
    my_vector.push_back(3.1415);
    std::cout << "0th element is " << my_vector[0] << std::endl;
    std::cout << "0th element is " << my_vector.at(0) << std::endl;

    std::cout << "1st element is " << my_vector[1] << std::endl;
    std::cout << "1st element is " << my_vector.at(1) << std::endl;

    std::cout << "My vector has " << my_vector.size() << "elements" <<
    std::endl;
	return 0;
}