#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int data;
    Node *left, *right;
    Node(int v) { data = v; left = right = NULL; }
};

bool isBSTUtil(Node* root, long mn, long mx) {
    if (!root) return true;
    if (root->data <= mn || root->data >= mx) return false;

    return isBSTUtil(root->left, mn, root->data) &&
           isBSTUtil(root->right, root->data, mx);
}

bool isBST(Node* root) {
    return isBSTUtil(root, LONG_MIN, LONG_MAX);
}

int main() { return 0; }
