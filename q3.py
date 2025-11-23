#include <iostream>
#include <algorithm>
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
Node* findMin(Node* root) {
    while (root && root->left) root = root->left;
    return root;
}
Node* deleteNode(Node* root, int k) {
    if (!root) return nullptr;
    if (k < root->key) root->left = deleteNode(root->left, k);
    else if (k > root->key) root->right = deleteNode(root->right, k);
    else {
        if (!root->left && !root->right) { 
            delete root;
            return nullptr;
        } else if (!root->left) {
            Node* temp = root->right;
            delete root;
            return temp;
        } else if (!root->right) { 
            Node* temp = root->left;
            delete root;
            return temp;
        } else {
            Node* succ = findMin(root->right);
            root->key = succ->key;
            root->right = deleteNode(root->right, succ->key);
        }
    }
    return root;
}
int maxDepth(Node* root) {
    if (!root) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}
int minDepth(Node* root) {
    if (!root) return 0;
    if (!root->left) return 1 + minDepth(root->right);
    if (!root->right) return 1 + minDepth(root->left);
    return 1 + min(minDepth(root->left), minDepth(root->right));
}
void inorder(Node* root) {
    if (!root) return;
    inorder(root->left);
    cout << root->key << ' ';
    inorder(root->right);
}
int main() {
    Node* root = nullptr;
    int arr[] = {15, 10, 20, 8, 12, 16, 25};
    for (int x : arr) root = insertNode(root, x);
    cout << "Inorder before delete: ";
    inorder(root); cout << '\n';
    root = deleteNode(root, 20);
    cout << "After deleting 20: ";
    inorder(root); cout << '\n';
    cout << "Max depth: " << maxDepth(root) << '\n';
    cout << "Min depth: " << minDepth(root) << '\n';
    return 0;
}
