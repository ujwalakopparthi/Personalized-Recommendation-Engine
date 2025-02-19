# Personalized Recommendation Engine 🛍️🤖

## 🚀 Overview
This project demonstrates a **personalized recommendation engine** for an e-commerce platform using a **hybrid recommendation system**. The model combines **collaborative filtering** and **content-based methods** to provide accurate and relevant product recommendations to users.

## 🛠️ Technologies Used
- **Python** 🐍
- **PyTorch** ⚡
- **Flask** 🌐
- **Neo4j** 🌳
- **AWS SageMaker** ☁️

## 🗂️ File Structure
- personalized-recommendation-engine/ │ ├── app/ # API and recommendation logic │ ├── init.py │ ├── recommendation.py │ └── api.py │ ├── model/ # Model training, dataset, and architecture │ ├── train.py │ ├── dataset.py │ └── model.py │ ├── utils/ # Utilities for data processing, graph handling, and deployment │ ├── data_preprocessing.py │ ├── graph.py │ └── aws_deploy.py │ ├── requirements.txt # Python dependencies ├── config.yaml # Configuration settings └── README.md # 

## Project documentation

## 🏗️ Setup

### 1. Install dependencies:
   First, create a virtual environment and install the necessary packages using `requirements.txt`:
    pip install -r requirements.txt 

### 2. Train the model:
    Run the training script to train the recommendation model:
        python model/train.py
### 3. Deploy on AWS:
    Deploy the trained model to AWS SageMaker (refer to utils/aws_deploy.py for deployment instructions).
### 4. Start the Flask API:
    To expose the model as a web service, start the Flask API:
    python app/api.py
### 5. Access the Recommendations:
    Once the Flask app is running, you can access the recommendations via the /recommend endpoint:
    URL: http://localhost:5000/recommend?user_id=<user_id>
    Method: GET
    Parameters: user_id (ID of the user for whom you want recommendations)

### ⚡ Key Features

- Hybrid Recommendation System: Combines collaborative filtering and content-based methods to enhance recommendation quality.
- Graph Database: Utilizes Neo4j to store and manage user-product relationships, enabling efficient retrieval of recommendations.
- Scalable: Deployed on AWS SageMaker, capable of handling thousands of recommendation requests per day.
