# model/model.py
import torch
import torch.nn as nn

class RecommendationModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RecommendationModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.fc3 = nn.Linear(output_size, 1)

    def forward(self, user_input, product_input):
        x = torch.cat([user_input, product_input], dim=1)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def get_recommendations(self, user_id, num_recommendations):
        # Logic for getting recommendations based on the user
        pass
