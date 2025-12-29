#include <stdio.h>
#include <stdlib.h>

struct node {
	int value;
	struct node* next;
};

struct node* new_node(int value) {
	struct node *ptr;
	ptr = (struct node*)malloc(sizeof(struct node));
	ptr->value = value;
	return ptr;
}

int main(void) {
	int input;
	scanf("%d", &input);

	const int cap = 50000000;
	const int steps = input;

	struct node *start, *cur, *new;

	start = new_node(0);
	cur = new_node(1);
	start->next = cur;
	cur->next = start;

	for (int value = 2; value <= cap; ++value) {
		for (int i = 0; i < steps; ++i) {
			cur = cur->next;
		}
		new = new_node(value);
		new->next = cur->next;
		cur->next = new;
		cur = new;
	}

	printf("%d\n", start->next->value);

	return 0;
}