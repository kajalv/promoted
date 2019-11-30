import requests
import os

def main():
	endpoint = "https://www.udemy.com/api-2.0/"
	clientID = ""
	clientSecret = ""
	clientBase64Auth = ""

	categories = [
		"Business",
		"Design",
		"Development",
		"Finance & Accounting",
		"Health & Fitness",
		"IT & Software",
		"Lifestyle",
		"Marketing",
		"Music",
		"Office Productivity",
		"Personal Development",
		"Photography",
		"Teaching & Academics",
	]

	orderings = [
		"relevance", "most-reviewed", "highest-rated", "newest", "price-low-to-high", "price-high-to-low"
	]

	durations = [
		"short", "medium", "long", "extraLong"
	]

	instructional_levels = [
		"beginner", "intermediate", "expert" # also "all" but that's redundant
	]

	try:
		clientID = os.environ["UDEMY_CLIENT_ID"]
		clientSecret = os.environ["UDEMY_CLIENT_SECRET"]
		clientBase64Auth = os.environ["UDEMY_BASE64"]
	except KeyError:
		print "Error: set the Udemy client credentials as environment variables"
		sys.exit(1)

	datafile = open("dataset.csv", "w+")

	udemy_url = endpoint + "courses"

	headers = {
		"Authorization" : "Basic " + clientBase64Auth,
		"Content-Type" : "application/json;charset=utf-8",
		"Accept" : "application/json, text/plain, */*"
	}

	params = {
		"page" : 1,
		"page_size" : 100,
		"ordering" : "highest-rated",
	}

	# for each category/duration/instructional level: get at least 500 courses
	# 13 categories * 4 durations * 3 instructional levels * 500 = 78000 courses maximum
	# But, many of these combinations will have no results

	datafile.write("id,title,url,is_paid,price,category,duration,instructional_level\n")

	total = 0

	for category in categories:
		print "Current category: " + category
		for duration in durations:
			print "Current duration: " + duration
			for instructional_level in instructional_levels:
				print "Current instructional level: " + instructional_level

				params["category"] = category
				params["duration"] = duration
				params["instructional_level"] = instructional_level
				params["page"] = 1

				course_count = 0
				while course_count < 500:
					response = requests.get(url = udemy_url, params = params, headers = headers)
					data = response.json()

					if "results" not in data:
						break

					for item in data["results"]:
						course_id = item["id"]
						course_title = item["title"]
						course_url = item["url"]
						course_paid = item["is_paid"]
						course_price = item["price"]
						string_to_write = str(course_id) + "," + course_title.encode("utf-8") + "," + course_url.encode("utf-8") + "," + str(course_paid) + "," + course_price.encode("utf-8") + "," + category + "," + duration + "," + instructional_level
						datafile.write(string_to_write + "\n")
						course_count = course_count + 1

					params["page"] = params["page"] + 1

				total = total + course_count

	datafile.close()

	print "Done. Found " + str(total) + " courses."

if __name__ == "__main__":
	main()
