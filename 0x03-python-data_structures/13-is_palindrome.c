#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome_2 - check if a list is palindrome
 * @arr: pointer to list
 * @index_a: primero indice (inicial)
 * @index_b: seg indice (final)
 * Return: return 1 if list is palindrome or 0 otherwise
 */
int is_palindrome_2(int *arr, int index_a, int index_b)
{
	if (arr[index_a] != arr[index_b])
		return (0);
	if (index_a < index_b)
		is_palindrome_2(arr, index_a + 1, index_b - 1);
	return (1);
}
/**
 * is_palindrome - check if a single linked list is palindrome
 * @head: pointer to node listint_t
 * Return: return 1 if list is palindrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len = 0;
	int i = 0; /*, j = 0, node_a = 0, node_b = 0, index_a = 0, index_b = 0;*/
	const listint_t *temp = *head;
	int *arr;

	if (!*head)
		return (1);
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	temp = *head;
	arr = malloc(sizeof(int) * len);
	if (!arr)
		return (0);
	for (i = 0; i <= (len - 1); i++)
	{
		arr[i] = temp->n;
		temp = temp->next;
	}
	if (is_palindrome_2(arr, 0, len - 1))
		return (1);
	return (0);
}
