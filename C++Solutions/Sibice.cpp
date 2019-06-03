#include <iostream>
#include <string>
#include "math.h"
using namespace std;

int main() {
  float numMatches, width, height;
  cin >> numMatches >> width >> height;


  float power2 = 2.0;
  float halfPow = 0.5;

  float hypot = (pow(width,power2) + pow(height, power2));
  hypot = pow(hypot, halfPow);
  //cout << hypot << endl;
  for(int i = 0; i < numMatches; i++){
    float match;
    cin >> match;
    if(match <= hypot){
      cout << "DA" << endl;
    } else {
      cout << "NE" << endl;
    }
  }
  return 0;
}
//cout << numMatches << width << height << endl;



/*


for x in range(numMatches):
    match = int(input())
    if match <= hypot:
        print("DA")
    else:
        print("NE")
*/
