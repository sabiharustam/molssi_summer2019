#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>
#include "temperature.hpp"

PYBIND11_MODULE(sss_cpp, m)
{
    m.doc() = "This is example c++ module called from python";
    m.def("f_to_celsius", f_to_celsius, "Convert fahrenheit to celsius");
    m.def("c_to_k", c_to_k, "Convert celsius to kelvin");
    m.def("f_to_kelvin", f_to_kelvin, "Convert fahrenheit to kelvin");
    m.def("f_to_c_vector", f_to_c_vector, "Convert fahrenheit matrix to celsius vector");
    m.def("f_to_c_matrix", f_to_c_matrix, "Convert fahrenheit matrix to celsius matrix");
}