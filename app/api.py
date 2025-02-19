# app/api.py
from flask import Flask, jsonify, request
from app.recommendation import RecommendationEngine

app = Flask(__name__)
recommendation_engine = RecommendationEngine(model_path='model/recommendation_model.pth')

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    recommendations = recommendation_engine.recommend(user_id)
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
