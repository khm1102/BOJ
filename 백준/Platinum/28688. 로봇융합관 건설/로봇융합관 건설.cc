#include <iostream>
using namespace std;

string choose_player(long long N, long long M) {
    if (N == 1 || M == 1) {
        return "First";
    }

    if (N == 2 || M == 2) {
        return "First";
    }

    if (N % 2 == 1 && M % 2 == 1) {
        return "First";
    }

    if (N % 2 == 0 && M % 2 == 0) {
        return "Second";
    }

    return "Second";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {
        long long N, M;
        cin >> N >> M;
        string result = choose_player(N, M);
        cout << result << "\n";
    }

    return 0;
}
