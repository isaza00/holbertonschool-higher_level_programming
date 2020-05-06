#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - check if a single linked list is palindrome
 * @head: pointer to node listint_t
 * Return: return 1 if list is palindrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
        size_t len = 0;
        int i = 0, j = 0, node_a = 0, node_b = 0, index_a = 0, index_b = 0;
        const listint_t *temp, *last_loc;

        if (!*head)
                return (1);
        temp = *head;
        while (temp)
        {
                temp = temp->next;
                len++;
        }
        temp = *head;
        index_b = len - 1;
        while (index_a < index_b)
        {
                while (i < index_b)
                {
                        if (i == index_a)
                        {
                                node_a = temp->n;
                                last_loc = temp->next;
                        }
                        temp = temp->next;
                        i++;
                }
                node_b = temp->n;
                if (node_a != node_b)
                        return (0);
                j++;
                i = j;
                index_a++;
                index_b--;
                temp = last_loc;
        }
        return (1);
}