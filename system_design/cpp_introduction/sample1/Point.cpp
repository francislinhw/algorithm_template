#include "Point.hpp"
#include <sstream>

Point::Point() : m_x(0), m_y(0) {} // Initialize to a default of (0,0)

Point::~Point() {} // Destructor

double Point::GetX() const { return m_x; }
double Point::GetY() const { return m_y; }

void Point::SetX(double x) { m_x = x; }
void Point::SetY(double y) { m_y = y; }

std::string Point::ToString() const {
    std::stringstream stream;
    // The output can be like: “Point(1.5, 3.9)”
    stream << "Point(" << m_x << ", " << m_y << ")";
    return stream.str();
}
