#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current_node;
	listint_t *next_node;

	current_node = list;
	next_node = list->next;

	while (next_node != NULL && next_node->next != NULL)
	{
		if (current_node == next_node)
		{
			return (1);
		}
		current_node = current_node->next;
		next_node = (next_node->next)->next;
	}
	return (0);
}
