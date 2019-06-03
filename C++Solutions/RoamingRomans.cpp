#include <iostream>
#include <math.h>

int main(){
  float miles = 0;
  std::cin >> miles;

  float newMile = 5280.000;
  float romMile = 4854.000;
  float paceConv = 1000.000;
  float mileConv = (newMile/romMile) * paceConv;

  float totalPaces = mileConv * miles;
  int intTotPaces = totalPaces;
  float remainder = totalPaces - intTotPaces;

  remainder >= 0.500 ? totalPaces = ceil(totalPaces) : totalPaces = floor(totalPaces);

  std::cout << totalPaces << std::endl;


  return 0;
}
