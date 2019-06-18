#include <stdio.h>
#include <string.h>
#define MAX 20

struct Colors {
  char color[20];
  int radius;
} color;

int main(int argc, char const *argv[]) {
  int numCases = 0;
  char line[100];
  // ARRAY OF STRUCTS
  // Get number of test cases
  scanf("%d\n", &numCases );
  struct Colors myStructArray [numCases];

  // Pull put data and insert into structs
  for (int i = 0; i < numCases; i++) {
    int n = 0;
    fgets(line,MAX, stdin);

// IF NUMBER IS FIRST //
    if (line[0] <= '9' && line[0] >= '0') {
      int j = 0;
      while (line[j] != ' ') {
        n = 10 * n + (line[j] - '0');
        j++;
      }
      // SET STRUCT RADIUS
      myStructArray[i].radius = (n / 2);

      int charCounter = 0;
      while (line[j] != '\0') {
        myStructArray[i].color[charCounter] = line[j];
        j++; charCounter++;
      }
      charCounter -=1;
      myStructArray[i].color[charCounter] = '\0';

    } else {
      int j2 = 0; int charCounter2 = 0;
      while (line[charCounter2] != ' ') {
           myStructArray[i].color[charCounter2] = line[j2];
           charCounter2++; j2++;
      }
      myStructArray[i].color[charCounter2] = '\0';
      j2++;
      int nn = 0;
      while (line[j2] <= '9' && line[j2] >= '0') {
        nn = 10 * nn + (line[j2] - '0');
        j2++;
      }
      myStructArray[i].radius = nn;
    }


  } // END FOR LOOP
  int myOrderArray[numCases];
  int min = 1001;
  struct Colors finalArr[numCases];
  int finalArrIncrement = 0;
  int destroy = 10000;
  for (size_t x = 0; x < numCases; x++) {
    for (size_t u = 0; u < numCases; u++) {
      if(myStructArray[u].radius < min){
        min = myStructArray[u].radius;
        finalArr[x].radius = min;
        char myString[20];
        //strncpy()
        strcpy(finalArr[x].color,myStructArray[u].color);
        destroy = u;
      }
    }
    myStructArray[destroy].radius = 1002;
    myOrderArray[x] = min;
    min = 1001;
    printf("%s\n",finalArr[x].color);
  }



  return 0;
}
