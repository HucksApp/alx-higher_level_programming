#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *slw = list, *fst = list;



	while(fst != NULL && fst->next != NULL)
	{
		slw = slw->next;
		fst = fst->next->next;

		if(slw == fst)
			return 1;
	}

    return 0;
}

