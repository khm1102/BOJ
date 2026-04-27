#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int test_cases;
    cin >> test_cases;
    while (test_cases--)
    {
        long long dot = 0, count = 0;
        char prev = '.';
        string s;
        cin >> s;
        reverse(s.begin(), s.end());
        for (int i = 0; i < s.length(); ++i)
        {
            char current = s[i];
            if (prev == '.')
                prev = current;
            if (prev == '.')
                continue;
            if (current == '.')
            {
                if (prev == 'W')
                    dot += count;
                else
                    dot -= count;
            }
            else if (current == prev)
                count++;
            else
                prev = '.', count = 0;
        }
        if (dot > 0)
            cout << "WHITE" << '\n';
        else
            cout << "BLACK" << '\n';
    }
    return 0;
}