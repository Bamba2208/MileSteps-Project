from datetime import datetime, timedelta
from collections import defaultdict
import requests

workouts = []
workout_id = 0

OPENWEATHER_API_KEY = 'ae2477cdd15db41a35ac1d365656c02c'
OPENWEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather(latitude, longitude):
    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric'
    }
    response = requests.get(OPENWEATHER_URL, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data['weather'][0]['description']
    else:
        return 'Weather data not available'

def add_workout(data):
    global workout_id
    workout_id += 1
    data['id'] = workout_id
    data['date_time'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')  # Assuming immediate workout registration
    if 'latitude' in data and 'longitude' in data:
        data['weather'] = fetch_weather(data['latitude'], data['longitude'])
    else:
        data['weather'] = 'Location not provided'
    workouts.append(data)
    return workout_id

def get_all_workouts():
    return workouts

def filter_workouts_by_date(start_date, end_date):
    filtered_workouts = []
    for workout in workouts:
        workout_date = datetime.strptime(workout['date_time'], '%Y-%m-%dT%H:%M:%S')
        if start_date <= workout_date <= end_date:
            filtered_workouts.append(workout)
    return filtered_workouts

def search_workouts_by_nickname(nickname):
    return [workout for workout in workouts if nickname.lower() in workout.get('route_nickname', '').lower()]

def aggregate_data(timeframe='weekly'):
    summary = defaultdict(lambda: {'total_distance': 0.0, 'total_duration': 0.0, 'count': 0})

    for workout in workouts:
        date = datetime.strptime(workout['date_time'], '%Y-%m-%dT%H:%M:%S')
        
        if timeframe == 'weekly':
            start_of_week = date - timedelta(days=date.weekday())
            key = start_of_week.strftime('%Y-%U')
        elif timeframe == 'monthly':
            key = date.strftime('%Y-%m')
        
        summary[key]['total_distance'] += float(workout.get('distance', 0))
        summary[key]['total_duration'] += float(workout.get('duration', 0))
        summary[key]['count'] += 1

    # Calculate averages
    for period, data in summary.items():
        data['average_distance'] = data['total_distance'] / data['count']
        data['average_duration'] = data['total_duration'] / data['count']

    return summary
# def get_weekly_summary():
#     return aggregate_data(timeframe='weekly')

# def get_monthly_summary():
#     return aggregate_data(timeframe='monthly')





