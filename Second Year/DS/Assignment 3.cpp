/*
Name - Soumil Arora
SID - 21105005
BRANCH - ECE
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_map>
using namespace std;

// Creating a function such that we are not passing the size of the array to the function.

// In linear search we are traversing the array, and not keeping any limitation on the the traversing index(i).

int linear_search(int arr[], int x)
{
    for (int i = 0;; i++)                       // no condition to stop the loop until the element not found.
    {
        if (arr[i] == x)
        {
            return i;
        }
    }
}

// Binary Search

// This function is a simple binary search function where left and right indexes are being provided.

int binary_search_code(int arr[],int l,int r,int x)
{
    int mid = (l+r) / 2;
    while(l<=r)
    {
        if(arr[mid]>x)
        {
            r = mid - 1;
            mid = (l+r) / 2;
        }
        else if(arr[mid]<x)
        {
            l = mid+1;
            mid = (l+r) / 2;
        }
        else
        {
            return mid;
        }
    }
}

// We try to reduce our work done to O(log(N)) time complexity, by increasing the range of our search exponentitaly by 2.

int binary_search(int arr[], int x)
{
    int low = 0;
    int high = 1;

    while (arr[high] < x)                       //if element to be found is still high the value at high index .
    {
        low = high;                             //update the low value
        high = 2 * high;                        //double the range of search, when the condition is satisfies then we call BINARY SEARCH on that range(low to high).
    }

    return binary_search_code(arr,low,high,x);
}

// NOTE - We are creating an array , but the size of the array is not passed to the function.

int main()
{
    // you are given the starting index of the array.
    int *arr = new int[10000];
    int n;
    cout << "Number of elements in an array: ";
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int x;
    cout << "Enter the Element to search for: ";
    cin >> x;
    cout << endl;

    cout << "Index of " << x << " from LINEAR SEARCH is : " << linear_search(arr, x) << endl;
    cout << "Index of " << x << " from BINARY SEARCH is : " << binary_search(arr, x) << endl;
    delete[] arr;
}