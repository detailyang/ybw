#! /bin/bash

for i in $(cat ./LICENSES); do
    l=$(echo $i | tr '[:lower:]' '[:upper:]')
    #github.com/nishanths/license
    license $l > $l
done
