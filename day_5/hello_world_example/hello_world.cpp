# include <iostream>
// including iostream to use cout.  Header.



int main(void)
{
	// This is one line comment. Start with double slash.
	/* This can go over 
	multiple line
	without any breaking. end with
	*/
	std::cout << "Hello, world!" << std::endl;

	int a = 10;
	a = 1.9;
	std::cout << "a is" << a << std::endl;
	// This is from c to c++. Maybe you can add an error message.

	// in c++ you can declare variable to be constants.
	const double d = 10.0;
	//d = 1.0; get rid of this since this gives error cause you are trying to over write constants.

	return 0;
}

