//
//  npf.cpp
//  
//
//  Created by David Chen on 10/13/19.
//

#include "npf.hpp"
#include <bits/stdc++.h>
using namespace std;
int main(){
    // add the two lines below
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int num;
    cin >> num;
    int
    int n, k, t;
    int cnt = 0;
    cin >> n >> k;
    for(int i=0; i<n; i++){
        cin >> t;
        if(t % k == 0) cnt++;
    }
    cout << cnt << "\n";
     
    return 0;
}
