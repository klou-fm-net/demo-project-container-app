from flask import Flask, request, jsonify
import random

app = Flask(__name__)

reviews = [
    "{} consistently delivers high-quality work.",
    "{} is a reliable and proactive team member.",
    "{} brings great energy and positivity to the team.",
    "{} demonstrates strong technical skills and problem-solving ability.",
    "{} is an excellent communicator and collaborator.",
    "{} could improve on time management under tight deadlines.",
    "{} shows potential and willingness to learn quickly.",
    "{} contributes creative ideas during team discussions.",
    "{} pays great attention to detail.",
    "{} meets expectations, but could benefit from more initiative."
]

@app.route('/review', methods=['POST'])
def generate_review():
    data = request.get_json()
    name = data.get('name', 'name')
    comment = random.choice(reviews).format(name)
    return jsonify({"review": comment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
