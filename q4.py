#include <iostream>
#include <climits>
using namespace std;
struct Node {
    int val;
    Node *left, *right;
    Node(int v): val(v), left(nullptr), right(nullptr) {}
};
bool isBSTUtil(Node* node, long long low, long long high) {
    if (!node) return true;
    if (node->val <= low || node->val >= high) return false;
    return isBSTUtil(node->left, low, node->val) && isBSTUtil(node->right, node->val, high);
}
bool isBST(Node* root) {
    return isBSTUtil(root, LLONG_MIN, LLONG_MAX);
}
int main() {
    // Example:
    //   10
    //  /  \
    // 5   20
    Node* root = new Node(10);
    root->left = new Node(5);
    root->right = new Node(20);
    cout << (isBST(root) ? "Tree is BST\n" : "Tree is NOT BST\n");
    root->right->left = new Node(9); // violates BST property
    cout << (isBST(root) ? "Tree is BST\n" : "Tree is NOT BST\n");
    return 0;
}
