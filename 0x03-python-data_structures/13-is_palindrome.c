#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *current_node = *head;
	listint_t *next_node = *head;
	listint_t *prev_node = NULL;
	listint_t *temp;
	
	if (*head == NULL)
		return (1);
	/**
	 * Find the middle of the linked list using current_node and next_node pointers
	 */
	while (next_node != NULL && next_node->next != NULL)
	{
		next_node = (next_node->next)->next;
		temp = current_node;
		current_node = current_node->next;
		temp->next = prev_node;
		prev_node = temp;
	}
	/**
	 * If the linked list has odd number of nodes, move current_node to the next node
	 */
	if (next_node != NULL)
		current_node = current_node->next;
	/**
	 * Compare the first half of the linked list with the reversed second half
	 */
	while (prev_node != NULL && current_node != NULL)
	{
		if (prev_node->n != current_node->n)
			return (0);
		prev_node = prev_node->next;
		current_node = current_node->next;
	}
	return (1);
}
