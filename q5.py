#include <iostream>
using namespace std;
void swapv(int &a, int &b) { int t=a; a=b; b=t; }
void maxHeapify(int arr[], int n, int i) {
    int largest = i;
    int l = 2*i + 1;
    int r = 2*i + 2;
    if (l < n && arr[l] > arr[largest]) largest = l;
    if (r < n && arr[r] > arr[largest]) largest = r;
    if (largest != i) {
        swapv(arr[i], arr[largest]);
        maxHeapify(arr, n, largest);
    }
}
void buildMaxHeap(int arr[], int n) {
    for (int i = n/2 - 1; i >= 0; --i) maxHeapify(arr, n, i);
}
void heapSortIncreasing(int arr[], int n) {
    buildMaxHeap(arr, n);
    for (int i = n-1; i > 0; --i) {
        swapv(arr[0], arr[i]);
        maxHeapify(arr, i, 0); 
    }
}
void minHeapify(int arr[], int n, int i) {
    int smallest = i;
    int l = 2*i + 1;
    int r = 2*i + 2;
    if (l < n && arr[l] < arr[smallest]) smallest = l;
    if (r < n && arr[r] < arr[smallest]) smallest = r;
    if (smallest != i) {
        swapv(arr[i], arr[smallest]);
        minHeapify(arr, n, smallest);
    }
}
void buildMinHeap(int arr[], int n) {
    for (int i = n/2 - 1; i >= 0; --i) minHeapify(arr, n, i);
}
void heapSortDecreasing(int arr[], int n) {
    buildMinHeap(arr, n);
    for (int i = n-1; i > 0; --i) {
        swapv(arr[0], arr[i]);
        minHeapify(arr, i, 0);
    }
}
int main() {
    int n;
    cout << "Enter n: ";
    if (!(cin >> n) || n <= 0) return 0;
    int *a = new int[n];
    cout << "Enter " << n << " integers:\n";
    for (int i = 0; i < n; ++i) cin >> a[i];
    int *b = new int[n];
    for (int i=0;i<n;++i) b[i]=a[i];
    heapSortIncreasing(b, n);
    cout << "Sorted increasing: ";
    for (int i=0;i<n;++i) cout << b[i] << ' ';
    cout << '\n';
    for (int i=0;i<n;++i) b[i]=a[i];
    heapSortDecreasing(b, n);
    cout << "Sorted decreasing: ";
    for (int i=0;i<n;++i) cout << b[i] << ' ';
    cout << '\n';
    delete [] a;
    delete [] b;
    return 0;
}
