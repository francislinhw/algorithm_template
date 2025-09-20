// First add a header file for the Point class with private members for the x- and y-coordinates. Do not forget to add the #ifndef/#define/#endif statements to avoid multiple inclusion.
// Also make sure you make to following public functionality (see also Figure 1):
// • Default constructor.
// • Destructor.
// • Getter functions for the x- and y-coordinates (GetX() and GetY() functions).
// • Settter functions for the x- and y-coordinates (SetX() and SetY() functions).
// • A ToString() that returns a string description of the point. Use the std::string class as
// return type.
// Next create the source file that implements the Point class defined in the header file. The source file must include the header file.
// Making the string in the ToString() function, requires conversion of the double coordinates to a string.
// Easiest is to use a std::stringstream object and the standard stream operators (as with iostream) to create the string. This requires the “sstream” header file.
// Use the str() function to retrieve the string from the string buffer. T
#ifndef POINT_H
#define POINT_H

#include <string>

class Point {
private:
    double m_x; // The x-coordinate
    double m_y; // The y-coordinate

public:
    Point(); // Default constructor
    ~Point(); // Destructor

    double GetX() const; // Getter for the x-coordinate
    double GetY() const; // Getter for the y-coordinate

    void SetX(double x); // Setter for the x-coordinate
    void SetY(double y); // Setter for the y-coordinate

    std::string ToString() const; // Returns a string description of the point
};

#endif // POINT_H
