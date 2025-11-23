#include <iostream>
using namespace std;
struct Node {
    int data;
    Node *left, *right;
    Node(int v): data(v), left(nullptr), right(nullptr) {}
};
void preorder(Node* root) {
    if (!root) return;
    cout << root->data << ' ';
    preorder(root->left);
    preorder(root->right);
}

void inorder(Node* root) {
    if (!root) return;
    inorder(root->left);
    cout << root->data << ' ';
    inorder(root->right);
}

void postorder(Node* root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    cout << root->data << ' ';
}

int main() {
    // sample tree:
    //      1
    //     / \
    //    2   3
    //   / \
    //  4   5
    Node *root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    cout << "Preorder: "; preorder(root); cout << '\n';
    cout << "Inorder:  "; inorder(root); cout << '\n';
    cout << "Postorder:"; postorder(root); cout << '\n';
    return 0;
}
