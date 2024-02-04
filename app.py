from flask import Flask, request, jsonify, render_template
import workouts

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

import base64

@app.route('/workouts', methods=['POST'])
def add_workout():
    data = request.form.to_dict()  
    image = request.files.get('image') 
    
    if image:
        image_string = base64.b64encode(image.read()).decode('utf-8')
        data['image'] = image_string

    workout_id = workouts.add_workout(data)
    return jsonify({'message': 'Workout added successfully', 'id': workout_id}), 201

@app.route('/workouts', methods=['GET'])
def get_workouts():
    return jsonify(workouts.get_all_workouts()), 200

@app.route('/workouts/filter', methods=['GET'])
def filter_workouts_by_date():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    filtered_workouts = workouts.filter_workouts_by_date(start_date, end_date)
    return jsonify(filtered_workouts), 200

@app.route('/workouts/search', methods=['GET'])
def search_workouts():
    nickname = request.args.get('nickname', '')
    found_workouts = workouts.search_workouts_by_nickname(nickname)
    return jsonify(found_workouts), 200

@app.route('/workouts/summary', methods=['GET'])
def workouts_summary():
    summary_type = request.args.get('summary_type', 'monthly')
    summary_data = workouts.aggregate_data(summary_type)
    return jsonify(summary_data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)



