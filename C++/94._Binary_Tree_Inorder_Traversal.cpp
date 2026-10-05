#include <iostream>
#include <vector>
#include <stdexcept>

using namespace std;

/*
struct TreeNode 
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
*/


template <typename T>
class Stack 
{
    private:
        int size;
        T *data;
        int head;
    public:
        Stack(int size = 100) 
        {
            if (size <= 0) throw invalid_argument("Size must be > 0");
            this->size = size;
            this->head = -1;
            this->data = new T[size];
        }
        void push(T value)
        {
            if (head == size - 1) throw overflow_error("Stack is full");
            data[++head] = value;
        }
        T peek()
        {
            if (head == -1) throw underflow_error("Stack is empty");
            return data[head];
        }
        T pop()
        {
            if (head == -1) throw underflow_error("Stack is empty");
            return data[head--];
        }
        bool isEmpty()
        {
            return head == -1;
        }
        ~Stack()
        {
            delete[] data;
        }
};


class Solution 
{
public:
    vector<int> inorderTraversal(TreeNode* root)
    {
        if (root == nullptr) return {};
        Stack<TreeNode*> stack;
        vector<int> result;
        TreeNode *current = root;

        while (!stack.isEmpty() || current != nullptr)
        {
            while (current != nullptr)
            {
                stack.push(current);
                current = current->left;
            }
            current = stack.pop();
            result.push_back(current->val);
            current = current->right;
        }
        return result;
    }
};
