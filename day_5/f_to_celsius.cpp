# include <iostream>
# include <vector>
# include <string>
# include <Eigen/Dense>
# include "temperature.hpp"

// commend to run:
// g++ -std=c++11 -Wall *.cpp -I${CONDA_PREFIX}/include/eigen3 -o f_to_celsius


int main(void)
{
    Eigen::MatrixXd mat(2,3);
    Eigen::VectorXd vec(3);

    mat(0,0) = 1.0;
    mat(0,1) = 2.0;
    mat(0,2) = 3.0;
    mat(1,0) = 4.0;
    mat(1,1) = 5.0;
    mat(1,2) = 6.0;

    vec(0) = vec(1) = vec(2) = 1.0;

    std::cout << "v.v = " << vec.dot(vec) << std::endl;
    std::cout << mat << std::endl;

	return 0;
}

