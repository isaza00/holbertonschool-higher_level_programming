#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    
    print_listint(head);

    printf("-----------------\n");

    insert_node(&head, 1025);

    print_listint(head);

    free_listint(head);

    return (0);
}