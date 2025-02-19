# app/recommendation.py
import torch
from model.model import RecommendationModel

class RecommendationEngine:
    def __init__(self, model_path):
        self.model = RecommendationModel()
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()

    def recommend(self, user_id, num_recommendations=5):
        # Sample recommendation logic (You can extend based on your model)
        # Assuming the model has an inference function
        recommendations = self.model.get_recommendations(user_id, num_recommendations)
        return recommendations
