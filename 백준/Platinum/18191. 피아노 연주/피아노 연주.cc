#include <bits/stdc++.h>
using namespace std;

long long floorDiv(long long a, long long b){
    long long q = a / b;  
    long long r = a % b;

    if(r != 0 && a < 0){
        q -= 1;
    }
    return q;
}

long long ceilDiv(long long a, long long b){
    long long q = a / b; 
    long long r = a % b;
    if(r != 0 && a > 0){
        q += 1;
    }
    return q;
}

bool canPlay(long long N, long long M, long long K, const vector<long long>& P, long long L){
    long long s = 1, e = N;

    for(int i=0; i < (int)M - 1; i++){
        long long d = P[i+1] - P[i];
        
        long long deltaMin = ceilDiv(d - L, K);
        long long deltaMax = floorDiv(d + L, K);

        if(deltaMin > deltaMax) {
            return false;
        }

        long long newS = s + deltaMin;
        long long newE = e + deltaMax;

        if(newS < 1) newS = 1;
        if(newE > N) newE = N;

        if(newS > newE) return false;

        s = newS;
        e = newE;
    }
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, M, K;
    cin >> N >> M >> K;

    vector<long long> P(M);
    for(int i=0; i<(int)M; i++){
        cin >> P[i];
    }

    long long left = 0;
    long long right = 200000000000000LL;

    while(left < right){
        long long mid = (left + right) / 2;
        if(canPlay(N, M, K, P, mid)){
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    cout << left << "\n";
    return 0;
}
