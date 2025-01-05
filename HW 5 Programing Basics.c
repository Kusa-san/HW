#include <stdio.h>

int main() {
    int rows = 5 ;
    int colons = 10;
    for ( int i = 0; i < 5; i++ ) {
        for ( int j = 0; j < 10; j++ ) {
            if ( i == 0 || i == rows - 1 || j == 0 || j == colons - 1 ) {
                printf( "# " );
            } else {
                printf( "* " );
            }
        }
        printf("\n");
    }
    return 0;
}