# this uses python 3

import csv
import sys

keywords_input="in.txt"
dataset_file="../data/udemy/dataset_with_ratings.csv"
# each line:
# id,title,url,is_paid,price,category,duration,instructional_level,rating

def udemy_reco(keywords):
	# get all the courses which have keywords matching
	suggestions = {}
	with open(dataset_file, 'r', encoding='UTF-8', newline='') as f:
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
	
	# print the course names
	for course in sorted_suggestions:
		print(course[1]["details"][1])

def udacity_reco(keywords):
	pass

def edx_reco(keywords):
	pass

def main():
	keywords = []
	# first open the keywords file and read all the words
	with open(keywords_input, 'r', encoding='UTF-8', newline='') as f:
		for line in csv.reader(f, delimiter=','):
			for word in line:
				word = word.strip(' \t\n\r\'')
				keywords.append(word.lower())

	# get recommendations from each of the MOOC providers
	udemy_reco(keywords)
	udacity_reco(keywords)
	edx_reco(keywords)

if __name__ == "__main__":
	main()