# this uses python 3

import csv
import sys

keywords_input="in.txt"
udemy_file="../data/udemy/dataset_with_ratings.csv"
udacity_file="../data/udacity/dataset_udacity.csv"
edx_file="../data/edx/dataset_edx.csv"

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
						suggestions[course_name]["details"] = line

	# get all the categories which have keywords matching
	categories = {}
	for course in suggestions:
		current_cat = suggestions[course]["details"][5]
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
		current_cat = suggestions[course]["details"][5]
		if current_cat == probable_category:
			filtered_suggestions[course] = suggestions[course]

	# sort the suggestions based on how many keywords are matched
	sorted_suggestions = sorted(filtered_suggestions.items(), key=lambda kv: kv[1]["keywords_matched"], reverse=True)

	return sorted_suggestions

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
						suggestions[course_name]["details"] = line

				if word in course_skills:
					if course_name in suggestions:
						suggestions[course_name]["keywords_matched"] = suggestions[course_name]["keywords_matched"] + 1
					else:
						suggestions[course_name] = {}
						suggestions[course_name]["keywords_matched"] = 1
						suggestions[course_name]["details"] = line

	# sort the suggestions based on how many keywords are matched
	sorted_suggestions = sorted(suggestions.items(), key=lambda kv: kv[1]["keywords_matched"], reverse=True)

	return sorted_suggestions

def edx_reco(keywords, file):
	# the structure of this file is similar to udacity
	return udacity_reco(keywords, file)

def main():
	keywords = []
	# first open the keywords file and read all the words
	with open(keywords_input, 'r', encoding='UTF-8', newline='') as f:
		for line in csv.reader(f, delimiter=','):
			for word in line:
				word = word.strip(' \t\n\r\'')
				keywords.append(word.lower())

	# get recommendations from each of the MOOC providers
	udemy_recos = udemy_reco(keywords, udemy_file)
	udacity_recos = udacity_reco(keywords, udacity_file)
	edx_recos = edx_reco(keywords, edx_file)

	# print the course names
	for course in udemy_recos:
		print(course[1]["details"][1])
	for course in udacity_recos:
		print(course[1]["details"][0])
	for course in edx_recos:
		print(course[1]["details"][0])

if __name__ == "__main__":
	main()