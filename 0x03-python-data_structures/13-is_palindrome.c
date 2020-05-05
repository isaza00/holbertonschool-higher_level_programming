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
	int i = 0, node_a = 0, node_b = 0, index_a = 0, index_b = 0;
	const listint_t *temp;

	if (!*head)
		return (1);
	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	temp = *head;
	if (len == 1)
		return (1);
	index_b = len - 1;
	while (index_a < index_b)
	{
		while (i < index_b)
		{
			if (i == index_a)
				node_a = temp->n;
			temp = temp->next;
			i++;
		}
		node_b = temp->n;
		i = 0;
		if (node_a != node_b)
			return (0);
		index_a++;
		index_b--;
		temp = *head;
	}
	return (1);
}
