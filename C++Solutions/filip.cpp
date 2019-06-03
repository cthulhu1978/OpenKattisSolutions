#include<iostream>
using namespace std;

// function prototype
int reverse(int number);
// MAIN
int main(int argc, char const *argv[]) {

  int first_num, second_num;
  cin >> first_num >> second_num;

  int num_first, num_second;
  num_first = reverse(first_num);
  num_second = reverse(second_num);

  int max;
  (num_first > num_second) ? max = num_first : max = num_second;
  cout << max << endl;

  return 0;
}


int reverse(int number){
  int reverse = 0;
  int rem = 0;

  while (number != 0) {
    rem = number % 10;
    reverse = (reverse*10 + rem);
    number /= 10;
  }
  return reverse;
}
