#include "lists.h"
/**
 * check_cycle - check if a list has a cycle
 * @list: param list
 * Return: 1 if has a cycle 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slower, *faster;

	slower = list;
	faster = list->next;
	while (1)
	{
		if (!faster || !faster->next)
			return (0);
		else if (faster == slower || faster->next == slower)
			return (1);
		slower = slower->next;
		faster = faster->next->next;
	}
}
