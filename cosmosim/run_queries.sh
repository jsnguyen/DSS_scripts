#!/bin/bash

id_arr=($(awk -F "\"*,\"*" '{print $2}' bullet_cluster_analog_candidates_id_only.csv))

id_arr=("${id_arr[@]:1}") #remove first element of array

cat /dev/null > job_id_list.txt
cat /dev/null > name_list.txt
for el in "${id_arr[@]}"; do
  query="\"SELECT p.rockstarId, p.x, p.y, p.z, p.vx, p.vy, p.vz, p.angMom_x, p.angMom_y, p.angMom_z, p.axis1_x, p.axis1_y, p.axis1_z, p.Mvir, p.Rvir, p.spin, p.T_U FROM MDPL2.Rockstar AS p, (SELECT depthFirstId, lastProg_depthFirstId FROM MDPL2.Rockstar WHERE rockstarId=${el}) AS r WHERE p.depthFirstId BETWEEN r.depthFirstId AND r.lastProg_depthFirstId ORDER BY p.snapnum\""
  name="id_${el}_a"
  http="http --auth jsnguyen:csim --form --follow POST https://www.cosmosim.org/uws/query query=$query table=\"$name\""

  job_id=$(eval $http | grep "<uws:jobId>" | sed 's|[^0-9]||g')

  echo ${name} >> name_list.txt
  echo ${job_id} >> job_id_list.txt

  run_job="http --auth jsnguyen:csim --form --follow POST https://www.cosmosim.org/uws/query/$job_id/phase phase=run"
  eval $run_job
done
