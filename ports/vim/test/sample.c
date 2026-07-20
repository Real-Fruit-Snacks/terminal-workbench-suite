/* twb sample: one screen of varied syntax.
 * TODO: this comment exercises the Todo group. */
#include <stdio.h>
#define ANSWER 42

typedef struct Point { int x, y; } Point;

static int add(int a, int b) { return a + b; }

int main(void) {
    const char *msg = "hello, \x1b[32mworkbench\n";
    double ratio = 3.14159;
    Point p = { .x = ANSWER, .y = 0 };
    for (int i = 0; i < 10; i++) {
        if (i % 2 == 0)
            printf("%s %d %f\n", msg, add(p.x, i), ratio);
    }
    return 0;
}
