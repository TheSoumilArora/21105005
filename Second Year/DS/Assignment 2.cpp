/*
Name - Soumil Arora
SID - 21105005
BRANCH - ECE
*/

#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    bool visited;
    Node *next;

    Node(int data)
    {
        this->data = data;
        this->next = NULL;
        this->visited = false;
    }
};

Node *takeinput()
{
    int data;
    cout << "Enter the Linked List :" << endl;
    cin >> data;
    Node *head = NULL, *tail = NULL;
    while (data != -1)
    {
        Node *newnode = new Node(data);
        if (head == NULL)
        {
            head = newnode;
            tail = newnode;
        }
        else
        {
            tail->next = newnode;
            tail = newnode;
        }
        cin >> data;
    }
    tail->next = head;
    return head;
}

void print(Node *head)
{
    Node *temp = head;
    while (temp->visited != true)
    {
        if (temp->next->visited != true)
        {
            cout << temp->data << " -> ";
        }
        else
        {
            cout << temp->data;
        }
        temp->visited = true;
        temp = temp->next;
    }
    cout << endl;
    cout << "We have reached the start of our Circular Linked List" << endl;
}

int main()
{
    Node *head = takeinput();
    print(head);
    return 0;
}



/*

The Applications of Circular Linked List are:

Multiplayer Games use this to give each player chance.
A circular linked list can be used to organize multiple running applications on an operating system. These applications are iterated over by the OS.
It is also used to play music in a playlist. The song in a playlist again start from the begining when the playlist end.

*/