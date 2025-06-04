#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
static const ll inf = 2e14;

inline ll floordiv(ll a, ll b) {
    ll q = a / b;
    ll r = a % b;

    if(r != 0 && a < 0) q--;
    return q;
}

inline ll ceildiv(ll a, ll b) {
    ll q = a / b;
    ll r = a % b;

    if(r != 0 && a > 0) q++;
    return q;
}

bool play(ll n, ll m, ll k, const vector<ll>& p, ll l) {
    ll s = 1, e = n;

    for(int i = 0; i + 1 < (int)m; i++) {
        ll d = p[i+1] - p[i];

        ll dmn = ceildiv(d - l, k);
        ll dmx = floordiv(d + l, k);
        if(dmn > dmx) return false;

        ll ns = s + dmn;
        ll ne = e + dmx;

        if(ns < 1) ns = 1;
        if(ne > n) ne = n;
        if(ns > ne) return false;

        s = ns;
        e = ne;
    }


    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n, m, k;
    cin >> n >> m >> k;

    vector<ll> p(m);
    for(int i = 0; i < m; i++){
        cin >> p[i];
    }

    ll left = 0, right = inf;
    while(left < right){
        ll mid = (left + right) / 2;
        if(play(n, m, k, p, mid)) right = mid;
        else left = mid + 1;
    }

    cout << left << "\n";
    return 0;
}
