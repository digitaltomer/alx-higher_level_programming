#include "lists.h"

/**
 * check_cycle - checks if a linked list is circular
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle
 * 0 if none
 */

int check_cycle(listint_t *list)
{
	listint_t *red = list;
	listint_t *blue = list;

	if (!list)
		return (0);

	while (red && blue && blue->next)
	{
		red = red->next;
		blue = blue->next->next;
		if (red == blue)
			return (1);
	}

	return (0);
}
