# model/dataset.py
import torch
from torch.utils.data import Dataset

class RecommendationDataset(Dataset):
    def __init__(self, file_path):
        self.data = self.load_data(file_path)

    def load_data(self, file_path):
        # Load the data from a CSV file (user, product, interaction score)
        import pandas as pd
        df = pd.read_csv(file_path)
        return df.values  # Return data as numpy array for easy processing

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        user_id, product_id, interaction = self.data[idx]
        return torch.tensor(user_id), torch.tensor(product_id), torch.tensor(interaction)
