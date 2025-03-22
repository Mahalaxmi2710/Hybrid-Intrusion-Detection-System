# Hybrid Intrusion Detection System (IDS) Project

## Overview
This project implements a hybrid Intrusion Detection System (IDS) using a combination of machine learning models and transformers to detect suspicious activity in a network. The system first uses a preliminary suspicious model to classify data and routes it through different stages based on detection outcomes. If an activity is flagged, it is sent to a sandbox for further analysis; if not, it proceeds to a misuse detection phase, and ultimately, if still undetected, advanced analysis is performed using transformers.

## Project Flow

1. **Data Collection**
   - The project uses the UNSW-NB15 dataset from Kaggle, which contains network traffic data labeled with different types of attacks.
   - The dataset is split into training and testing sets.

2. **Preliminary Suspicious Model**
   - A simple model is used to initially flag suspicious activity in the data.
   - The model classifies the network traffic data into different categories, marking it as either normal or suspicious.
   
3. **Sandbox Detection**
   - If an activity is flagged as suspicious by the preliminary model, it is moved to a sandbox for more detailed analysis.
   - The sandbox performs further tests on the flagged data to check for potential malicious behavior.

4. **Misuse Detection**
   - If the activity is not detected as malicious in the sandbox, it is sent to a misuse detection phase.
   - This phase uses predefined signatures or rules to detect known malicious activities based on past patterns.

5. **Advanced Analysis with Transformers**
   - If an activity is still undetected, it moves to the final analysis phase, which uses transformer-based models for advanced anomaly detection.
   - Transformers are leveraged to analyze intricate patterns in network traffic, improving detection accuracy for previously unseen threats.

