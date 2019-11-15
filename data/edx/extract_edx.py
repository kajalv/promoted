import json

with open('edX.json', 'r') as f:
    data = json.load(f)['results']

    datafile = open("dataset_edx.csv", "w+")
    datafile.write("title,level,expected_duration,expected_duration_unit,skills,price\n")
    count = 0
    for course in data:
        title = course['title'].replace(",","")
        level = course['level_type']
        expected_duration = course['course_runs'][0]['weeks_to_complete']
        expected_duration_unit = 'week'
        skills = []
        for subject in course['subjects']:
            skills.append(subject['name'])
        price = course['course_runs'][0]['first_enrollable_paid_seat_price']
        string_to_write = title + "," + level + ", " + str(expected_duration) + "," + expected_duration_unit + "," + ("|".join(skills)) + "," + str(price)
        datafile.write(string_to_write + "\n")
        count += 1
    datafile.close()

    print("Extracted " + str(count) + " courses")
