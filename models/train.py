# model/train.py
import torch
import torch.nn as nn
import torch.optim as optim
from model.dataset import RecommendationDataset
from model.model import RecommendationModel

def train_model():
    # Initialize dataset and dataloaders
    dataset = RecommendationDataset('data/user_product_interactions.csv')
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=True)

    # Initialize model
    model = RecommendationModel(input_size=1000, hidden_size=500, output_size=100)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Training loop
    for epoch in range(10):  # Change number of epochs as needed
        for data in dataloader:
            user_input, product_input, target = data
            optimizer.zero_grad()
            output = model(user_input, product_input)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

        print(f"Epoch {epoch + 1}, Loss: {loss.item()}")

    # Save the trained model
    torch.save(model.state_dict(), 'model/recommendation_model.pth')

if __name__ == "__main__":
    train_model()
