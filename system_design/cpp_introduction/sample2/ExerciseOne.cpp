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
    // Create a Point object using the default constructor.
    int unsigned x, y;

    x = 1;
    y = 2;

    cout << "x: " << x << ", y: " << y << endl;

    // for loop and print 1 to 10
    for (int i = 1; i <= 10; i++)
    {
        cout << i << endl;
    }

    // ++ first and start from 0
    for (int i = 0; i < 10; ++i)
    {
        cout << i << endl;
    }

    cout << "================" << endl;
    // have a blank line
    cout << endl;

    // ++ first and start from 0
    for (int i = 0; i < 10;)
    {
        ++i;
        cout << i << endl;
    }

    // switch case
    int num;

    cout << "Enter a number: ";
    cin >> num;

    // switch case
    switch (num)
    {
        case 1:
            cout << "One" << endl;
            break;
        case 2:
            cout << "Two" << endl;
            break;
        default:
            cout << "Default" << endl;
            break;
    }

    // work with input and output files
    ifstream input_data;
    ofstream output_data;

    input_data.open("input.txt");

    // if none and create a new file
    if (!input_data.is_open())
    {
        cout << "File not found, creating a new file" << endl;
        input_data.open("input.txt", ios::out);
        input_data.close();
        input_data.open("input.txt", ios::in);
    }

    // get the current working directory
    char *cwd = getcwd(NULL, 0);
    cout << "Current working directory: " << cwd << endl;

    output_data.open("output.txt");

    if (input_data.is_open())
    
    input_data.close();
    output_data.close();

    // left shift and right shift
    int a = 1;
    int b = 2;

    cout << "a: " << a << ", b: " << b << endl;
    int c = a << b;
    int d = a >> b;
    cout << "a(after left shift): " << c << ", a(after right shift): " << d << endl;
    
    // Home directory is ~
    char *home = getenv("HOME");
    cout << "Home directory: " << home << endl;


    return 0;
}
