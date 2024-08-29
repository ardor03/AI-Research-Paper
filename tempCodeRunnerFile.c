include <stdio.h>
int x;
void bar();
void foo() {
	char c = 'c';
	bar();
	printf("%d %c\n", x, c);
}
void baz() {
	printf("%d\n", x);
	x = 1337;
}
void bar() {
	int x = 100;
	baz();}
int main() {   
	x = 10;
	{
		char* x = "testing";
		printf("%s\n", x);
	}
	foo();
}
