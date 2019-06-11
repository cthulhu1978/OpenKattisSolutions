#include <iostream>
#include <vector>
#include <algorithm>
#define COUNT 4
using namespace std;

int main(int argc, char const *argv[]) {
  vector<int> vec;
  for (size_t i = 0; i < COUNT; i++) {
    int tmp;
    cin >> tmp;
    vec.push_back(tmp);
  }
  sort(vec.begin(),vec.end());
  cout << (vec[0] * vec[2]) << endl;

  return 0;
}
