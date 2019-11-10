import json, urllib.request

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open('https://www.udacity.com/public-api/v1/courses')
json_response=json.loads(response.read())
course_list = json_response["courses"]

count = 0

datafile = open("dataset_udacity.csv", "w+")

datafile.write("title,level,expected_duration,expected_duration_unit,required_knowledge\n")

for course in course_list:
	course_title 					= course["title"]
	course_level 					= course["level"]
	course_expected_duration 		= course["expected_duration"]
	course_expected_duration_unit 	= course["expected_duration_unit"]
	course_required_knowledge 		= course["required_knowledge"]

	string_to_write = course_title + "," + course_level + "," + str(course_expected_duration) + "," + course_expected_duration_unit + "," + course_required_knowledge
	datafile.write(string_to_write + "\n")

	count = count + 1

datafile.close()


print("Total no. of courses: ",count)
	
	

