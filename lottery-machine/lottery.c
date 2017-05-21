#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void print_slot(int guessed_slot[10]) {
	int i;

	printf("\n");

	for (i = 0; i < 10; i++) {
		if (guessed_slot[i] != -1) {
			printf("  %d", guessed_slot[i]);
		} else {
			printf("  ?");
		}
	}

	printf("\n");
	for (i = 1; i <= 10; i++) printf("  -");
	printf("\n");
	for (i = 1; i <= 10; i++) printf("  %d", i);
	printf("\n\n");
}

int main() {
	char data[64];
	FILE *fp;
	fp = fopen("/dev/urandom", "r");
	fread(&data, 1, 64, fp);
	fclose(fp);

	unsigned int random_number = (unsigned int)data;
	srand(random_number);

	int lottery_slot[10];
	int guessed_slot[10];

	memset(lottery_slot, -1, sizeof(lottery_slot));
	memset(guessed_slot, -1, sizeof(guessed_slot));

	int i = 0;

	for (i = 0; i < 10; i++) {
		lottery_slot[i] = rand() % 10;
	}

	printf("Lottery Machine v1.0\n\n");

	printf("Guess 7 slot out of 10\n");

	print_slot(guessed_slot);

	for (i = 0; i < 7; i++) {
		int index, number;
		printf("Choose slot index (1-10) : ");
		scanf("%d", &index);
		printf("Guess the number (0-9) : ");
		scanf("%d", &number);
		index--;
		guessed_slot[index] = number;
		print_slot(guessed_slot);
	}

	int right = 0;
	for (i = 0; i < 10; i++) {
		if (guessed_slot[i] == lottery_slot[i]) right++;
	}

	if (right == 7) {
		printf("YOU WON!!!\n");
		printf("Here is your prize :\n");

		char flag[64];
		fp = fopen("Lottery.flag", "r");
		fread(&flag, 1, 64, fp);
		fclose(fp);

		printf("%s\n", flag);
	} else {
		printf("Better Luck Next Time\n");
	}

	return 0;
}