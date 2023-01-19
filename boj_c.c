#include <stdio.h>
#include <stdlib.h>

int main() {
	int ocs[6] = {1, 1, 2, 2, 2, 8};
	int cs[6];

	for (int i = 0; i < 6; i++) {
		if (i == 5 || i == 0) scanf("%d", &cs[i]);
		else scanf(" %d", &cs[i]);

		if (cs[i] < 0 && cs[i] > 10) exit(1);
	}

	for (int i = 0; i < 6; i++) {
		printf("%d ", ocs[i] - cs[i]);
	}

	return 0;
}
