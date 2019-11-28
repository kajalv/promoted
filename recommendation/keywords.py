# this uses python 3

import csv
import sys

keywords_input="in.txt"
udemy_file="./data/udemy/dataset_with_ratings.csv"
udacity_file="./data/udacity/dataset_udacity.csv"
edx_file="./data/edx/dataset_edx.csv"

def format_udemy(line):
	course = {}
	course['title'] = line[1]
	course['site'] = "Udemy"
	course['duration'] = 1 # all courses seems to take only a couple of days
	course['duration_unit'] = "week"
	if line[3] == 'TRUE':
		course['price'] = float(line[4][1:])
	else:
		course['price'] = 0.0
	if line[7] == 'beginner':
		course['level'] = 0
	elif line[7] == 'intermediate':
		course['level'] = 1
	else:
		course['level'] = 2
	return course

def udemy_reco(keywords, file):
	# get all the courses which have keywords matching
	# id,title,url,is_paid,price,category,duration,instructional_level,rating
	suggestions = {}
	with open(file, 'r', encoding='UTF-8', newline='') as f:
		for line in csv.reader(f, delimiter=','):
			course_name = line[1]
			course_words = course_name.split()
			for word in keywords:
				# for each course in the dataset, count how many keywords are matched in the course name
				if word in course_words:
					if course_name in suggestions:
						suggestions[course_name]["keywords_matched"] = suggestions[course_name]["keywords_matched"] + 1
					else:
						suggestions[course_name] = {}
						suggestions[course_name]["keywords_matched"] = 1
						suggestions[course_name]["category"] = line[5]
						suggestions[course_name]["details"] = format_udemy(line)

	# get all the categories which have keywords matching
	categories = {}
	for course in suggestions:
		current_cat = suggestions[course]["category"]
		if current_cat in categories:
			categories[current_cat] = categories[current_cat] + 1
		else:
			categories[current_cat] = 1

	# get the most probable category - this is content based recommendation
	sorted_categories = sorted(categories.items(), key=lambda kv: kv[1], reverse=True)
	probable_category = sorted_categories[0][0]

	filtered_suggestions = {}
	# filter suggestions in that category
	for course in suggestions:
		current_cat = suggestions[course]["category"]
		if current_cat == probable_category:
			filtered_suggestions[course] = suggestions[course]

	# sort the suggestions based on how many keywords are matched
	sorted_suggestions = sorted(filtered_suggestions.items(), key=lambda kv: kv[1]["keywords_matched"], reverse=True)

	return sorted_suggestions

def format_udacity(line):
	course = {}
	course['title'] = line[0]
	course['site'] = "Udacity"
	course['duration'] = int(line[2].strip()) # all courses seems to take only a couple of days
	course['duration_unit'] = "week"
	course['price'] = 0.0
	if line[1] == 'beginner':
		course['level'] = 0
	elif line[1] == 'intermediate':
		course['level'] = 1
	else:
		course['level'] = 2
	return course

def udacity_reco(keywords, file):
	# get all the courses which have keywords matching
	# title,level,expected_duration,expected_duration_unit,skills,free
	suggestions = {}
	with open(file, 'r', encoding='UTF-8', newline='') as f:
		for line in csv.reader(f, delimiter=','):
			course_name = line[0]

			course_skills = []
			for entry in line[4].split('|'):
				course_skills.append(entry.lower())
			course_words = []
			for entry in course_name.split():
				course_words.append(entry.lower())

			for word in keywords:
				# for each course in the dataset, count how many keywords are matched in the course name and skills
				if word in course_words:
					if course_name in suggestions:
						suggestions[course_name]["keywords_matched"] = suggestions[course_name]["keywords_matched"] + 1
					else:
						suggestions[course_name] = {}
						suggestions[course_name]["keywords_matched"] = 1
						suggestions[course_name]["details"] = format_udacity(line)

				if word in course_skills:
					if course_name in suggestions:
						suggestions[course_name]["keywords_matched"] = suggestions[course_name]["keywords_matched"] + 1
					else:
						suggestions[course_name] = {}
						suggestions[course_name]["keywords_matched"] = 1
						suggestions[course_name]["details"] = format_udacity(line)

	# sort the suggestions based on how many keywords are matched
	sorted_suggestions = sorted(suggestions.items(), key=lambda kv: kv[1]["keywords_matched"], reverse=True)

	return sorted_suggestions

def format_edx(line):
	course = {}
	course['title'] = line[0]
	course['site'] = "edX"
	course['duration'] = int(line[2].strip()) # all courses seems to take only a couple of days
	course['duration_unit'] = "week"
	course['price'] = float(line[5])
	if line[1] == 'Introductory':
		course['level'] = 0
	elif line[1] == 'Intermediate':
		course['level'] = 1
	else:
		course['level'] = 2
	return course

def edx_reco(keywords, file):
	# the structure of this file is similar to udacity
	suggestions = {}
	with open(file, 'r', encoding='UTF-8', newline='') as f:
		for line in csv.reader(f, delimiter=','):
			course_name = line[0]

			course_skills = []
			for entry in line[4].split('|'):
				course_skills.append(entry.lower())
			course_words = []
			for entry in course_name.split():
				course_words.append(entry.lower())

			for word in keywords:
				# for each course in the dataset, count how many keywords are matched in the course name and skills
				if word in course_words:
					if course_name in suggestions:
						suggestions[course_name]["keywords_matched"] = suggestions[course_name]["keywords_matched"] + 1
					else:
						suggestions[course_name] = {}
						suggestions[course_name]["keywords_matched"] = 1
						suggestions[course_name]["details"] = format_edx(line)

				if word in course_skills:
					if course_name in suggestions:
						suggestions[course_name]["keywords_matched"] = suggestions[course_name]["keywords_matched"] + 1
					else:
						suggestions[course_name] = {}
						suggestions[course_name]["keywords_matched"] = 1
						suggestions[course_name]["details"] = format_edx(line)

	# sort the suggestions based on how many keywords are matched
	sorted_suggestions = sorted(suggestions.items(), key=lambda kv: kv[1]["keywords_matched"], reverse=True)

	return sorted_suggestions

def get_courses(keywords):
	# keywords = []
	# # first open the keywords file and read all the words
	# with open(keywords_input, 'r', encoding='UTF-8', newline='') as f:
	# 	for line in csv.reader(f, delimiter=','):
	# 		for word in line:
	# 			word = word.strip(' \t\n\r\'')
	# 			keywords.append(word.lower())

	# get recommendations from each of the MOOC providers
	udemy_recos = udemy_reco(keywords, udemy_file)
	udacity_recos = udacity_reco(keywords, udacity_file)
	edx_recos = edx_reco(keywords, edx_file)

	course_list = []
	for course in udemy_recos:
		course_list.append(course[1]["details"])
	for course in udacity_recos:
		course_list.append(course[1]["details"])
	for course in edx_recos:
		course_list.append(course[1]["details"])
	return course_list
