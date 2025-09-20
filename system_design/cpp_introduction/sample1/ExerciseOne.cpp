// Finally create a test program (separate source file with a main() function) for the Point class. It should do the following things:
// • Include the point header file.
// • Ask the user for the x- and y-coordinates using the std::cin object (needs the “iostream” header file).
// • Then create a Point object using the default constructor.
// • Set the coordinates entered by the user using the setter functions.
// • Print the description of the point returned by the ToString() function.
// • Print the point coordinates using the get functions.
#include "Point.hpp" // Include the point header file.
#include <iostream>

int main()
{
    // Create a Point object using the default constructor.
    Point p;
    double x, y;

    // Ask the user for the x- and y-coordinates using the std::cin object (needs the “iostream” header file).
    std::cout << "Enter the x-coordinate: ";
    std::cin >> x;
    std::cout << "Enter the y-coordinate: ";
    std::cin >> y;

    // Set the coordinates entered by the user using the setter functions.
    p.SetX(x);
    p.SetY(y);

    // Print the description of the point returned by the ToString() function.
    std::cout << p.ToString() << std::endl;
    // Print the point coordinates using the get functions.
    std::cout << "X: " << p.GetX() << ", Y: " << p.GetY() << std::endl;

    return 0;
    /*
     * ============== *
     * PROGRAM OUTPUT *
     * ============== *
     *
     * Enter the x-coordinate: 7
     * Enter the y-coordinate: 24
     * Point(7, 24)
     * X: 7, Y: 24
     *
     */
}
