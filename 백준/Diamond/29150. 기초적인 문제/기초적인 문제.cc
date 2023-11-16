#include <iostream>
#include <vector>
using namespace std;

const int mod = 1000000007;

int pow(int x, int y, int m) {
    int res = 1;
    while (y > 0) {
        if (y % 2 == 1)
            res = (1LL * res * x) % m;
        x = (1LL * x * x) % m;
        y /= 2;
    }
    return res;
}

int vandermonde_matrix(int N, vector<int> &a) {
    int ans = 1;
    for (int i = 1; i < N; ++i) {
        for (int j = 0; j < i; ++j) {
            ans = (1LL * ans * (a[i] - a[j])) % mod;
            if (ans < 0) ans += mod;
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> fact(501, 1);
    for (int i = 2; i < 501; ++i) {
        fact[i] = (1LL * fact[i - 1] * i) % mod;
    }

    vector<int> hyper(501, 1);
    for (int i = 1; i < 501; ++i) {
        hyper[i] = (1LL * hyper[i - 1] * fact[i]) % mod;
    }

    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        vector<int> a(N);
        for (int i = 0; i < N; ++i) {
            cin >> a[i];
        }
        int ans = (1LL * vandermonde_matrix(N, a) * pow(hyper[N - 1], mod - 2, mod)) % mod;
        cout << ans << "\n";
    }

    return 0;
}
