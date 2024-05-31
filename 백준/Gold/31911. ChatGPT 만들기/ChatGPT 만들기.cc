#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <cstring>

#define MAX_CHARS 256

using namespace std;

struct CharCount {
    char next_char;
    int count;
};

struct CharList {
    vector<CharCount> counts;
};

struct ChatGPT {
    CharList char_lists[MAX_CHARS];
    char dictionary[MAX_CHARS];
};

void initChatGPT(ChatGPT& gpt) {
    for (int i = 0; i < MAX_CHARS; ++i) {
        gpt.dictionary[i] = 0;
    }
}

int main() {
    int n, k, m;
    cin >> n >> k >> m;

    ChatGPT gpt;
    initChatGPT(gpt);

    string buffer;
    for (int i = 0; i < n; ++i) {
        cin >> buffer;
        int len = buffer.length();
        for (int j = 0; j < len - 1; ++j) {
            char node = buffer[j];
            char next = buffer[j + 1];
            CharList& list = gpt.char_lists[(unsigned char)node];

            bool found = false;
            for (auto& count : list.counts) {
                if (count.next_char == next) {
                    count.count++;
                    found = true;
                    break;
                }
            }
            if (!found) {
                list.counts.push_back({next, 1});
            }
        }
    }

    for (int i = 0; i < MAX_CHARS; ++i) {
        CharList& list = gpt.char_lists[i];
        if (!list.counts.empty()) {
            char result = 0;
            int max_count = 0;
            for (const auto& count : list.counts) {
                if (count.count > max_count ||
                   (count.count == max_count && count.next_char < result)) {
                    result = count.next_char;
                    max_count = count.count;
                }
            }
            gpt.dictionary[i] = result;
        }
    }

    int idx = 1;
    char node = '[';
    while (idx < k + m) {
        if (idx >= k) {
            cout << node;
        }

        if (node != ']' && node != '.') {
            node = gpt.dictionary[(unsigned char)node];
        } else {
            node = '.';
        }

        idx++;
    }

    return 0;
}
