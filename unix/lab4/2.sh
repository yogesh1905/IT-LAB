#!/bin/bash

# comm -ab == suppress cols a and b

u1=`comm -23 <( sort $1 ) <( sort $2 )`
u2=`comm -13 <( sort $1 ) <( sort $2 )`
c=`comm -12 <( sort $1 ) <( sort $2 )`

if [ -z "$c" ]; then
    echo "no common element found"
else 
    echo "common: "
    echo $c
fi

echo "unique in file 1 - " $1                                  
echo $u1



echo "unique in file 2 - " $2                                  
echo $u2
