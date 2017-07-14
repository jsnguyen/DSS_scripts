#!/bin/bash

get_query=()
while read name
do
  echo ${name}
  get_query+=("http --auth jsnguyen:csim --download GET  https://www.cosmosim.org/query/download/stream/table/${name}/format/csv")

done < name_list.txt

for el in "${get_query[@]}"
do
  eval ${el}
done
