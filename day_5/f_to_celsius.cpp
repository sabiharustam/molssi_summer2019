# include <iostream>
# include <vector>
# include <string>
# include "temperature.hpp"

void print_vector(const std::vector<double> & vec)
{
    //for(size_t i = 0; i < vec.size(); i++)
    //    std::cout << "Element " << i << " is" << vec[i] << std::endl;
    // range-based for loop
    for(auto it : vec)
        std::cout << it << std::endl;
    vec[0] = 0.000;
}
int main(void)
{
    std::vector<double> my_vector;

    my_vector.push_back(3.1415);

    std::cout << "0th element is " << my_vector[0] << std::endl;
    std::cout << "0th element is " << my_vector.at(0) << std::endl;

    std::cout << "1st element is " << my_vector[1] << std::endl;
    //std::cout << "1st element is " << my_vector.at(1) << std::endl;

    std::string s = "This is a string";
    std::cout << "s is " << s << std::endl;

    std::vector<double> multiples;
    for(int i = 0; i < 6; i++)
    {
        double k = 3.1415 * i;
        multiples.push_back(k);
    }

    /*for(int i = 0; i < 5; i++)
    {
        std::cout << multiples[i] << std::endl;
    }
    std::cout << "My vector has " << multiples.size() << " elements" <<
    std::endl;*/
    print_vector(multiples);
	return 0;
}

