#include <stdio.h>
#include <string.h>

int main(void)
{
    typedef struct
    {
        int vote;
        int age;
    } cand;

    int MAX = 5;

    cand arr[MAX];

    cand arr[0].vote = 10;
    cand arr[0].age = 49;
}