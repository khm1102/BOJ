#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int main()
{
    string s1, s2;
    long double cr, gr, sum = 0, ssum = 0;
    int tc = 20;

    while (tc--)
    {
        cin >> s1 >> cr >> s2;

        switch (s2[0])
        {
        case 'A':
            if (s2[1] == '+')
                gr = 4.5;
            else
                gr = 4.0;
            break;
        case 'B':
            if (s2[1] == '+')
                gr = 3.5;
            else
                gr = 3.0;
            break;
        case 'C':
            if (s2[1] == '+')
                gr = 2.5;
            else
                gr = 2.0;
            break;
        case 'D':
            if (s2[1] == '+')
                gr = 1.5;
            else
                gr = 1.0;
            break;
        default:
            gr = 0.0;
        }

        if (s2[0] != 'P')
        {
            sum += (cr * gr);
            ssum += cr;
        }
    }

    cout.precision(7);
    
    if (ssum == 0) {
        cout << showpoint << 0.0;
    } else {
        cout << showpoint << sum / ssum;
    }

    return 0;
}
