#include <iostream>
#include <climits>
using namespace std;
struct Node {
    int key;
    Node *left, *right;
    Node(int k): key(k), left(nullptr), right(nullptr) {}
};
Node* insertNode(Node* root, int k) {
    if (!root) return new Node(k);
    if (k < root->key) root->left = insertNode(root->left, k);
    else if (k > root->key) root->right = insertNode(root->right, k);
    return root;
}
Node* searchRec(Node* root, int k) {
    if (!root || root->key == k) return root;
    if (k < root->key) return searchRec(root->left, k);
    else return searchRec(root->right, k);
}
Node* searchIter(Node* root, int k) {
    Node* cur = root;
    while (cur) {
        if (cur->key == k) return cur;
        if (k < cur->key) cur = cur->left;
        else cur = cur->right;
    }
    return nullptr;
}
Node* findMin(Node* root) {
    if (!root) return nullptr;
    while (root->left) root = root->left;
    return root;
}
Node* findMax(Node* root) {
    if (!root) return nullptr;
    while (root->right) root = root->right;
    return root;
}
Node* inorderSuccessor(Node* root, int key) {
    Node* cur = root;
    Node* target = searchIter(root, key);
    if (!target) return nullptr;
    if (target->right) return findMin(target->right);
    Node* succ = nullptr;
    cur = root;
    while (cur) {
        if (key < cur->key) {
            succ = cur;
            cur = cur->left;
        } else if (key > cur->key) {
            cur = cur->right;
        } else break;
    }
    return succ;
}
Node* inorderPredecessor(Node* root, int key) {
    Node* target = searchIter(root, key);
    if (!target) return nullptr;
    if (target->left) return findMax(target->left);
    Node* pred = nullptr;
    Node* cur = root;
    while (cur) {
        if (key > cur->key) {
            pred = cur;
            cur = cur->right;
        } else if (key < cur->key) {
            cur = cur->left;
        } else break;
    }
    return pred;
}
int main() {
    Node* root = nullptr;
    int arr[] = {20, 8, 22, 4, 12, 10, 14};
    for (int x : arr) root = insertNode(root, x);

    int key = 10;
    cout << "Search recursive " << key << ": " << (searchRec(root, key) ? "Found\n" : "Not found\n");
    cout << "Search iterative " << 15 << ": " << (searchIter(root, 15) ? "Found\n" : "Not found\n");

    Node* mx = findMax(root);
    Node* mn = findMin(root);
    cout << "Min: " << (mn ? mn->key : INT_MIN) << '\n';
    cout << "Max: " << (mx ? mx->key : INT_MAX) << '\n';

    int q = 12;
    Node* s = inorderSuccessor(root, q);
    Node* p = inorderPredecessor(root, q);
    cout << "Successor of " << q << ": " << (s ? to_string(s->key) : string("None")) << '\n';
    cout << "Predecessor of " << q << ": " << (p ? to_string(p->key) : string("None")) << '\n';

    return 0;
}
