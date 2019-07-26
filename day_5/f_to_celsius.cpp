# include <iostream>
# include <vector>
# include "temperature.hpp"


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
    std::vector<double> my_vector;
    my_vector.push_back(3.1415);
    std::cout << "0th element is " << my_vector[0] << std::endl;
	return 0;
}