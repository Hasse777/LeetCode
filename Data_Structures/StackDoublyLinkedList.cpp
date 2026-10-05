#include <iostream>
#include <stdexcept>

using namespace std;


template <typename T>
struct Node
{
    T data;
    Node* next_node = nullptr;
    Node* prev_node = nullptr;
};


template <typename T>
class Stack 
{
    private:
        Node<T>* head_node;
        Node<T>* last_node;

    public:
        Stack() 
        {
            this->head_node = nullptr;
            this->last_node = nullptr;
        }
        void push(T value)
        {
            if(head_node == nullptr)
            {
                this->head_node = new Node<T>;
                this->head_node->data = value;
                this->last_node = this->head_node;
            }
            else
            {
                this->last_node->next_node = new Node<T>;
                this->last_node->next_node->data = value;
                this->last_node->next_node->prev_node = this->last_node;
                this->last_node = this->last_node->next_node;
            }
            cout << "Value was pushed" << endl;
        }
        T peek()
        {
            if(!this->isEmpty())
            {
                return this->last_node->data;
            }
            throw underflow_error("Stack is empty");
        }
        T pop()
        {
            if(!this->isEmpty())
            {
                T current_data = this->last_node->data;
                if (head_node == last_node)
                {
                    delete this->last_node;
                    this->last_node = this->head_node = nullptr;
                    return current_data;
                }
                Node<T>* current_ptr = this->last_node->prev_node;
                delete this->last_node;
                this->last_node = current_ptr;
                this->last_node->next_node = nullptr;
                return current_data;
            }
            throw underflow_error("Stack is empty");
        }
        bool isEmpty()
        {
            return this->last_node == nullptr;
        }

        ~Stack()
        {
            Node<T>* current_ptr = head_node;
            Node<T>* next_ptr = nullptr;
            while(current_ptr != nullptr)
            {
                next_ptr = current_ptr->next_node;
                delete current_ptr;
                current_ptr = next_ptr;
            }
        }
};
