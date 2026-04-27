#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

vector<int> buildSuffixArray(const string& s) {
    int n = s.length();
    vector<int> sa(n), ranks(n), temp(n);
    for (int i = 0; i < n; i++) {
        sa[i] = i;
        ranks[i] = s[i];
    }

    for (int k = 1; k < n; k <<= 1) {
        auto compare = [&](int i, int j) {
            if (ranks[i] != ranks[j]) return ranks[i] < ranks[j];
            int ri = i + k < n ? ranks[i + k] : -1;
            int rj = j + k < n ? ranks[j + k] : -1;
            return ri < rj;
        };
        sort(sa.begin(), sa.end(), compare);

        temp[sa[0]] = 0;
        for (int i = 1; i < n; i++) {
            temp[sa[i]] = temp[sa[i - 1]] + compare(sa[i - 1], sa[i]);
        }
        ranks = temp;
    }
    return sa;
}

vector<int> buildLCP(const string& s, const vector<int>& sa) {
    int n = s.length();
    vector<int> lcp(n), rank(n);
    for (int i = 0; i < n; i++) rank[sa[i]] = i;

    for (int i = 0, k = 0; i < n; i++, k = max(k-1, 0)) {
        if (rank[i] == n - 1) {
            k = 0;
            continue;
        }
        int j = sa[rank[i] + 1];
        while (i + k < n && j + k < n && s[i + k] == s[j + k]) k++;
        lcp[rank[i]] = k;
    }
    return lcp;
}

int main() {
    int L;
    string s;
    cin >> L >> s;

    auto sa = buildSuffixArray(s);
    auto lcp = buildLCP(s, sa);

    cout << *max_element(lcp.begin(), lcp.end()) << endl;

    return 0;
}
