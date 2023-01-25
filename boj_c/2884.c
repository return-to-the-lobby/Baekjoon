#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{	
	int hour, minute;
	scanf("%d %d", &hour, &minute);

	if (hour > 23 || hour < 0) return 0;
	
	minute -= 45;
	if (minute < 0) {
		hour -= 1;
		minute *= -1;
		minute = 60 - minute;
		if (hour < 0) {
			hour = 23;
		}
	}

	printf("%d %d", hour, minute);
	return 0;
}
