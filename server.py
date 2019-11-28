from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import csv
import ast
import recommendation

app = Flask(__name__)
CORS(app)

@app.route('/get_courses', methods=['GET'])
def get_courses():
    job = request.args.get('job_title')
    keywords = []
    # get the keywords for the job title
    with open("./data/jobs-data/job_skills_keywords.csv", 'r') as f:
        for line in csv.reader(f, delimiter=","):
            if job == line[1]:
                keywords = ast.literal_eval(line[2]).copy()
                break

    course_list = recommendation.get_courses(keywords)

    return  jsonify(course_list), 200

@app.route('/get_jobs', methods=["GET"])
def get_jobs():
    jobs = []
    with open("./data/jobs-data/job_skills_keywords.csv", 'r') as f:
        for line in csv.reader(f, delimiter=','):
            if line[1] == "job_title":
                continue
            jobs.append(line[1])

    return jsonify(jobs), 200

if __name__ == "__main__":
    app.run(debug=False)
