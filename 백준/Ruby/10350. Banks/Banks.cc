#include <bits/stdc++.h>

using namespace std;
#define ll long long int
ll a[30010],b[30010];

int main()
{
    ll n,s=0,res=0;
    scanf("%lld",&n);
    for(ll i = 0; i < n;i++) {
        // 입력
        scanf("%lld",&a[i]);
    }
    for(ll i =0; i < n;i++) {
        // 누적합
        a[i+n] = a[i];
        s += a[i];
    }
    for(ll i = 0;i < n;i++) {
        for(ll j = 0; j < n;j++) {
            //더하기
            b[j + 1] = b[j] + a[i + j];
            if(b[j+1]<0){
                //절댓값
                res += (b[j+1]*-1+s-1)/s;
            }
        }
    }
    printf("%lld",res);

    return 0;
}