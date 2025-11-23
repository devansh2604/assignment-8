#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int data;
    Node *left, *right;
    Node(int v) { data = v; left = right = NULL; }
};

Node* insertBST(Node* root, int key) {
    if (!root) return new Node(key);
    if (key < root->data) root->left = insertBST(root->left, key);
    else if (key > root->data) root->right = insertBST(root->right, key);
    return root;
}

// Recursive Search
Node* searchRec(Node* root, int key) {
    if (!root || root->data == key) return root;
    if (key < root->data) return searchRec(root->left, key);
    return searchRec(root->right, key);
}

// Non-recursive search
Node* searchNonRec(Node* root, int key) {
    while (root) {
        if (key == root->data) return root;
        if (key < root->data) root = root->left;
        else root = root->right;
    }
    return NULL;
}

Node* findMin(Node* root) {
    while (root && root->left) root = root->left;
    return root;
}

Node* findMax(Node* root) {
    while (root && root->right) root = root->right;
    return root;
}

Node* inorderSuccessor(Node* root, Node* target) {
    Node* succ = NULL;
    while (root) {
        if (target->data < root->data) {
            succ = root;
            root = root->left;
        } else root = root->right;
    }
    return succ;
}

Node* inorderPredecessor(Node* root, Node* target) {
    Node* pred = NULL;
    while (root) {
        if (target->data > root->data) {
            pred = root;
            root = root->right;
        } else root = root->left;
    }
    return pred;
}

int main() { return 0; }
