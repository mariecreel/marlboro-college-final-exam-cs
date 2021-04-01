/*scope.c
 * this code was written to demonstrate how variables are scoped in the c
 * programming language. In writing this code, I referenced the Second 
 * edition of The C Programming Language by Brian W. Kernighan and
 * Dennis M. Ritchie. specifically, I referenced the section in the
 * first chapter that discusses variable scoping. 
 *
 * Nick Creel - Apr 11, 2020 - MIT License
 */
# include <stdio.h>

int max; /*maximum value out of x and y*/
int x = 2;
int y = 3;

main()
{       
	x = 4;
	
	if(x > y)
		max = x;
	else
		max = y;
	printf("max is %d\n", max);
}
