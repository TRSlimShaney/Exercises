/*
Author:         Shane Stacy
Description:    This program averages the last three integers, returned as unsigned integer (rounded down)
*/

#include <stdio.h>
#include <stdlib.h>

int array[3];
int counter = 0;


unsigned int avg(unsigned int num) {
    if (counter == 0) {
        array[0] = num;
    }
    else if (counter == 1) {
        array[1] = num;
    }
    else if (counter == 2) {
        array[2] = num;
    }

    counter++;

    if (counter == 3) {
        counter = 0;
    }

    return (array[0] + array[1] + array[2])/3
}

