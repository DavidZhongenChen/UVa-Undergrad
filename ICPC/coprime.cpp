#include <iostream>

using namespace std;
int gcd(int a, int b) { 
   if (b == 0) 
      return a; 
   return gcd(b, a % b);
} 

int main(){
    int b1;
    int e1;
    int b2;
    int e2;
    cin >> b1 >> e1 >> b2 >> e2; 
    int count = 0;
    for (int i = b1; i <= e1; i++){
        for (int j = b2; j <= e2; j++){
            if(gcd(i,j) == 1){
                count++;
            }
        }
    }
    cout << count;
} 

