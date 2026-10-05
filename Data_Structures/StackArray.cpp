#include <iostream>
#include <stdexcept>

using namespace std;


template <typename T>
class Stack 
{
    private:
        unsigned size;
        T *data;
        int head;

        void memory_redefinition()
        {
            unsigned new_size = size * 2;
            T *new_data = new T[new_size];
            for(int i = 0; i < size; i++)
            {
                new_data[i] = this->data[i];
            }
            delete[] data;
            size = new_size;
            this->data = new_data;
        }

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
            if (this->isFull()) this->memory_redefinition();
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

        bool isFull()
        {
            return head == size - 1;
        }

        ~Stack()
        {
            delete[] data;
        }
};
