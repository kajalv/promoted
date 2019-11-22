import json, urllib.request
import re

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open('https://www.udacity.com/public-api/v1/courses')
json_response=json.loads(response.read())
course_list = json_response["courses"]

count = 0

datafile = open("dataset_udacity.csv", "w+")

datafile.write("title,level,expected_duration,expected_duration_unit,skills,free\n")

for course in course_list:
    course_title = course["title"].rstrip()
    course_level = course["level"].rstrip()
    if not course["expected_duration"]:
        continue
    course_expected_duration = course["expected_duration"]
    if not course["expected_duration_unit"]:
        continue
    course_expected_duration_unit = course["expected_duration_unit"]
    if course_expected_duration_unit == "days" or course_expected_duration_unit == "hours" or course_expected_duration_unit == "day":
        course_expected_duration = 1
        course_expected_duration_unit = "week"
    elif course_expected_duration_unit == "months" :
        course_expected_duration *= 4
        course_expected_duration_unit = "weeks"
    #course_required_knowledge = course["required_knowledge"]
    # course_summary = course["summary"].rstrip("\n\r").replace(",", "").replace("\n+", "")
    # course_summary = course_summary.replace("<p>", "").replace("</p>", "")
    # print(course_summary)
    if not course['metadata'] or not 'skills' in course['metadata'].keys() or not 'is_free_course' in course['metadata'].keys():
        continue
    course_skills = course["metadata"]["skills"]
    if len(course_skills) ==0:
        continue
    is_free = "n"
    if course['metadata']['is_free_course']==True:
        is_free = "y"

    string_to_write = course_title + "," + course_level + ", " + str(course_expected_duration) + "," + course_expected_duration_unit + "," + ("|".join(course_skills)) + "," + is_free
    datafile.write(string_to_write + "\n")
    count = count + 1

datafile.close()


print("Total no. of courses: ",count)
