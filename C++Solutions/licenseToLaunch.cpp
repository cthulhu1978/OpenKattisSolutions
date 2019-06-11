#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  int numDays = 0;
  long long spaceJunk  = 1000000000;
  int tmp = 0;
  int spaceDay = 0;

  cin >> numDays;
  for (int i = 0; i < numDays; i++) {
      cin >> tmp;
      if(tmp < spaceJunk){
        spaceJunk = tmp;
        spaceDay = i;
      }
  }
  cout << spaceDay << endl;


  return 0;
}
