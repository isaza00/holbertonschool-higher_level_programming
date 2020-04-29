#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *current, *aux;
	int cmp = 0;

	if (!head)
		return (NULL);

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (number < current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current)
	{
		if (current->next)
		{
			aux = current->next;
			cmp = current->next->n;
		}
		else
		{
			aux = NULL;
			cmp = number + 1; }
		if (number >= current->n && number < cmp)
		{
			current->next = new;
			new->next = aux; }
		current = aux; }
	return (new);
}
