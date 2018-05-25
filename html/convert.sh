#!/bin/bash
for i in {1..8} ;  
do 

cd Module$i ; 

jupyter nbconvert --template full index.ipynb ;

jupyter nbconvert --template full assignment/assignment.ipynb ;

jupyter nbconvert --template full notebooks/*.ipynb ;

cd .. ; 

done

