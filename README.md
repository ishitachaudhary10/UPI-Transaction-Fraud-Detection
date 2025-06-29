# 💸 UPI Transaction Fraud Detection

This project focuses on detecting potentially fraudulent Unified Payments Interface (UPI) transactions using anomaly detection techniques. It combines machine learning with a web-based user interface to allow anyone to test real-time or hypothetical transactions and check whether they appear suspicious. The goal is to help users and analysts gain insights into digital payment fraud patterns in India.

---

## 🚀 Features

This application integrates a machine learning model trained on transaction data with a web interface, enabling end-users to input transaction details and receive a fraud prediction instantly. It supports both real-time inputs and dataset-level evaluations.

The backend logic is powered by a Python Flask server, while the frontend is built using HTML, CSS, and JavaScript. It allows seamless interaction between the user and the prediction engine, making the application highly intuitive and accessible to non-technical users as well.

---

## 📁 Dataset

We use a rich dataset from Kaggle titled **"UPI Transactions 2024 Dataset"**, which contains over 60,000 synthetic UPI transaction records. Each record includes details such as transaction type, timestamp, amount, sender/receiver information, bank details, and a label indicating whether the transaction was fraudulent.

The dataset can be accessed from the following link:  
🔗 [UPI Transactions 2024 Dataset – Kaggle](https://www.kaggle.com/datasets/skullagos5246/upi-transactions-2024-dataset/data)

It provides a realistic simulation of real-world UPI data, which is especially valuable for research and testing anomaly detection models on financial transactions.

---

## 🧠 ML Model Details

The project uses the **Isolation Forest** algorithm, which is well-suited for unsupervised anomaly detection. This algorithm works by isolating observations that differ significantly from the rest of the data, making it ideal for fraud detection in transactional datasets.

The model is trained on a set of carefully selected features including transaction amount, sender and receiver age groups (label encoded), the hour and day of the transaction, and whether it occurred on a weekend. These features are scaled before model training to ensure accuracy.

---

## 📊 Visual Insights

To support better understanding and analysis, the project also includes several graphical insights generated using Seaborn and Matplotlib. These visualizations help reveal patterns in transaction behavior and how fraud correlates with certain features.

Some of the charts include a **confusion matrix** to evaluate the model’s performance, **anomaly counts per sender state**, and **boxplots of transaction amounts** categorized by anomaly status. These graphs are also displayed on the static homepage for better visibility.

---

## 🌐 Web Interface

The web interface consists of two main HTML pages. The first is a static homepage (`home.html`) that displays an overview of the project, dataset link, and generated graphs. The second page (`index.html`) is interactive and allows users to input transaction values to test for fraud.

Users enter transaction details such as amount, sender/receiver age (encoded), hour, day, and weekend status, and the system returns whether the transaction is classified as fraudulent or normal. The interface is built with responsive design in mind and works well across devices.

---

## ▶️ How to Run (Locally or in Colab)

You can run the Python backend using Flask locally or inside Google Colab using `flask-ngrok`. Once the server is running, it will expose an endpoint which the frontend form communicates with.

Make sure to update the fetch URL inside your JavaScript file (`index.html`) to match the public ngrok link when deploying from Colab. Then open `home.html` or `index.html` in your browser and interact with the application.

---

## 💻 Technologies Used

- **Python & Flask** for backend and ML inference
- **Scikit-learn** for machine learning model (Isolation Forest)
- **Pandas & Seaborn** for data preprocessing and visualization
- **HTML, CSS, JavaScript** for frontend development
- **Ngrok** for exposing local server in cloud environments like Google Colab

These tools together enable end-to-end functionality from data ingestion to live predictions in the browser.

---

## 🔗 Links

- 🔍 [Try It Live (via ngrok URL or hosted)](https://your-ngrok-or-hosted-link.com)
- 📊 [Kaggle Dataset](https://www.kaggle.com/datasets/skullagos5246/upi-transactions-2024-dataset/data)
- 🧠 [GitHub Repo](https://github.com/yourusername/upi-fraud-detector)

---

## ✅ To Do / Future Scope

- Add user login to allow history tracking of predicted transactions.
- Integrate additional features such as device type, transaction type, and merchant category.
- Explore other algorithms like One-Class SVM or Local Outlier Factor.
- Deploy permanently using platforms like Render or Railway.

These improvements would enhance the robustness, scalability, and security of the system.

---

## 📜 License

This project is released under the **MIT License**, allowing free use, modification, and distribution with attribution. See the `LICENSE` file for more details.

