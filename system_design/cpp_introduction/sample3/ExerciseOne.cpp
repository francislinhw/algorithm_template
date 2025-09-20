// Finally create a test program (separate source file with a main() function) for the Point class. It should do the following things:
// • Include the point header file.
// • Ask the user for the x- and y-coordinates using the std::cin object (needs the “iostream” header file).
// • Then create a Point object using the default constructor.
// • Set the coordinates entered by the user using the setter functions.
// • Print the description of the point returned by the ToString() function.
// • Print the point coordinates using the get functions.

#include <iostream>
#include <unistd.h>
#include <fstream> // work with input and output files
#include <string> // work with strings
#include <sstream> // work with strings # The difference between string and sstream is that string is a class and sstream is a class template
#include <vector> // work with vectors
#include <map> // work with maps
#include <set> // work with sets
#include <queue> // work with queues
#include <stack> // work with stacks
#include <algorithm> // work with algorithms
// #include <fstream.h>

using namespace std;

int main()
{
    // Pointer
    int *p = new int(10);

    // princt the address of the pointer
    cout << "Address of the pointer: " << p << endl;

    // print the value of the pointer
    cout << "Value of the pointer: " << *p << endl;

    // print the address of the value of the pointer
    cout << "Address of the value of the pointer: " << &*p << endl;

    // Reference to value
    int &r = *p; // * means dereference the pointer so the reference is the value of the pointer
    cout << "Address of the reference: " << &r << endl;
    cout << "Value of the reference: " << r << endl;
    cout << "Address of the value of the reference: " << &r << endl;


    // Reference to a reference
    int &r2 = r;
    cout << "Address of the reference to the reference: " << &r2 << endl;
    cout << "Value of the reference to the reference: " << r2 << endl;
    cout << "Address of the value of the reference to the reference: " << &r2 << endl;

    // Reference to a pointer
    int *&r3 = p; 
    cout << "Address of the reference to the pointer: " << &r3 << endl;
    cout << "Value of the reference to the pointer: " << r3 << endl;
    cout << "Address of the value of the reference to the pointer: " << &r3 << endl;

    // Reference to a reference to a pointer
    return 0;
}
