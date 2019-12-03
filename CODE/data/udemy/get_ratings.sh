#!/bin/sh
input="dataset.csv"
output="dataset_with_ratings.csv"

header=$(head -n 1 $input)
header="${header},rating"

echo $header > $output

course_count=0

sed 1d $input | while read d
do
   course_id="$(echo $d | cut -d ',' -f 1)"
   url="https://www.udemy.com/api-2.0/courses/${course_id}/?fields[course]=rating"
   result="$(curl --silent -g -X GET $url -H 'Authorization: Basic $UDEMY_BASE64' -H 'Content-Type: application/json')"
   rating="$(echo $result|jq '.rating')"
   line="${d},${rating}"
   echo $line >> $output
   course_count=$((course_count+1))
   if ! (($course_count % 100)); then
      echo "Progress: $course_count courses"
   fi
done
