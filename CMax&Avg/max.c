/*
Author:         Shane Stacy
Description:    This program returns the max integer in an array
*/

#include <stdio.h>
#include <stdlib.h>


int max(int array[], int size) {
    int max = array[0];
    for (int i = 0; i < size; i++) {
        if (array[i] > max) {
            max = array[i];
        }
    }
    return max;
}

