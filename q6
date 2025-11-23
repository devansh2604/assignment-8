#include <iostream>
using namespace std;
class MaxPQ {
    int *heap;
    int capacity;
    int heapSize;
    void siftUp(int i) {
        while (i > 0) {
            int p = (i - 1) / 2;
            if (heap[p] >= heap[i]) break;
            swap(heap[p], heap[i]);
            i = p;
        }
    }
    void siftDown(int i) {
        while (true) {
            int l = 2*i + 1;
            int r = 2*i + 2;
            int largest = i;
            if (l < heapSize && heap[l] > heap[largest]) largest = l;
            if (r < heapSize && heap[r] > heap[largest]) largest = r;
            if (largest == i) break;
            swap(heap[i], heap[largest]);
            i = largest;
        }
    }
public:
    MaxPQ(int cap=100): capacity(cap), heapSize(0) {
        heap = new int[capacity];
    }
    ~MaxPQ() { delete[] heap; }

    bool empty() const { return heapSize == 0; }
    int size() const { return heapSize; }
    void push(int x) {
        if (heapSize == capacity) {
            int *newh = new int[capacity*2];
            for (int i=0;i<capacity;++i) newh[i]=heap[i];
            delete[] heap;
            heap = newh;
            capacity *= 2;
        }
        heap[heapSize++] = x;
        siftUp(heapSize-1);
    }
    int top() const {
        if (heapSize == 0) { cerr << "Empty PQ\n"; return -1; }
        return heap[0];
    }
    int pop() {
        if (heapSize == 0) { cerr << "Empty PQ\n"; return -1; }
        int ret = heap[0];
        heap[0] = heap[heapSize-1];
        --heapSize;
        if (heapSize > 0) siftDown(0);
        return ret;
    }
};
int main() {
    MaxPQ pq(10);
    pq.push(10);
    pq.push(4);
    pq.push(15);
    pq.push(20);
    cout << "Top: " << pq.top() << '\n';
    cout << "Pop: " << pq.pop() << '\n';
    cout << "Top now: " << pq.top() << '\n';
    cout << "Popping all: ";
    while (!pq.empty()) cout << pq.pop() << ' ';
    cout << '\n';
    return 0;
}
