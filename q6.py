#include <bits/stdc++.h>
using namespace std;

class MaxHeap {
public:
    vector<int> h;

    void push(int x) {
        h.push_back(x);
        int i = h.size() - 1;

        while (i > 0 && h[(i-1)/2] < h[i]) {
            swap(h[(i-1)/2], h[i]);
            i = (i - 1) / 2;
        }
    }

    int top() {
        return h.empty() ? -1 : h[0];
    }

    void heapify(int i) {
        int n = h.size();
        int largest = i;
        int l = 2*i + 1;
        int r = 2*i + 2;

        if (l < n && h[l] > h[largest]) largest = l;
        if (r < n && h[r] > h[largest]) largest = r;

        if (largest != i) {
            swap(h[i], h[largest]);
            heapify(largest);
        }
    }

    void pop() {
        if (h.empty()) return;
        h[0] = h.back();
        h.pop_back();
        heapify(0);
    }
};

int main() {
    return 0;
}
