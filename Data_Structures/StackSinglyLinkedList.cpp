#include <iostream>
#include <stdexcept>

using namespace std;


template <typename T>
struct Node
{
    T data;
    Node* next_node = nullptr;
};


template <typename T>
class Stack 
{
    private:
        Node<T>* head_node;

    public:
        Stack() 
        {
            this->head_node = nullptr;
        }
        void push(T value)
        {
            Node<T>* new_node = new Node<T>;
            new_node->data = value;

            new_node->next_node = this->head_node;
            this->head_node = new_node;

            cout << "Value was pushed" << endl;
        }
        T peek()
        {
            if(!this->isEmpty())
            {
                return this->head_node->data;
            }
            throw underflow_error("Stack is empty");
        }
        T pop()
        {
            if(!this->isEmpty())
            {
                T current_data = this->head_node->data;
                Node<T>* current_node = this->head_node->next_node;
                delete this->head_node;
                this->head_node = current_node;
                return current_data;
            }
            throw underflow_error("Stack is empty");
        }
        bool isEmpty()
        {
            return this->head_node == nullptr;
        }

        ~Stack()
        {
            Node<T>* current_ptr = this->head_node;
            Node<T>* next_ptr = nullptr;
            while(current_ptr != nullptr)
            {
                next_ptr = current_ptr->next_node;
                delete current_ptr;
                current_ptr = next_ptr;
            }
        }
};
