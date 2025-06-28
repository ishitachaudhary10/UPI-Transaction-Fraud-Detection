<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>UPI Transaction Fraud Detection - Home</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      min-height: 100vh;
      background: linear-gradient(135deg, #d4a574 0%, #e8b4a0 50%, #f4c2c2 100%);
      padding: 20px;
    }
    
    .container {
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(10px);
      padding: 40px;
      max-width: 900px;
      margin: 0 auto;
      border-radius: 30px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    }
    
    h1 {
      font-size: 3rem;
      font-weight: 400;
      color: #8b5a3c;
      text-align: center;
      margin-bottom: 40px;
      letter-spacing: -0.5px;
    }
    
    h2 {
      font-size: 1.8rem;
      font-weight: 500;
      color: #8b5a3c;
      margin-bottom: 20px;
      margin-top: 30px;
    }
    
    p {
      line-height: 1.6;
      font-size: 16px;
      color: #666;
      margin-bottom: 20px;
    }
    
    a {
      color: #8b5a3c;
      text-decoration: none;
      font-weight: 500;
    }
    
    a:hover {
      text-decoration: underline;
    }
    
    .graph-section {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: center;
      margin: 30px 0;
    }
    
    .graph-container {
      background: rgba(255, 255, 255, 0.8);
      border-radius: 15px;
      padding: 20px;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease;
    }
    
    .graph-container:hover {
      transform: translateY(-5px);
    }
    
    .graph-container img {
      max-width: 100%;
      height: auto;
      border-radius: 10px;
      display: block;
    }
    
    .graph-title {
      text-align: center;
      font-weight: 600;
      color: #8b5a3c;
      margin-bottom: 15px;
      font-size: 1.1rem;
    }
    
    .button-group {
      text-align: center;
      margin-top: 40px;
      display: flex;
      gap: 20px;
      justify-content: center;
      flex-wrap: wrap;
    }
    
    .button-group a {
      text-decoration: none;
      padding: 18px 30px;
      background: linear-gradient(135deg, #8b5a3c 0%, #a0674a 100%);
      color: white;
      border-radius: 25px;
      font-weight: 500;
      display: inline-block;
      transition: all 0.3s ease;
      font-size: 1.1rem;
      letter-spacing: 0.5px;
    }
    
    .button-group a:hover {
      transform: translateY(-3px);
      box-shadow: 0 15px 30px rgba(139, 90, 60, 0.4);
      text-decoration: none;
    }
    
    .button-group a:active {
      transform: translateY(-1px);
    }
    
    .emoji {
      margin-right: 8px;
    }
    
    @media (max-width: 768px) {
      .container {
        padding: 30px 20px;
      }
      
      h1 {
        font-size: 2.5rem;
      }
      
      .button-group {
        flex-direction: column;
        align-items: center;
      }
      
      .button-group a {
        width: 100%;
        max-width: 300px;
      }
      
      .graph-section {
        flex-direction: column;
        align-items: center;
      }
      
      .graph-container {
        width: 100%;
        max-width: 400px;
      }
    }
  </style>
</head>
<body>

<div class="container">
  <h1><span class="emoji">💸</span>UPI Transaction Fraud Detection</h1>
  
  <h2>About the Project</h2>
  <p>
    This project aims to identify potentially fraudulent UPI transactions using machine learning techniques.
    It uses an Isolation Forest anomaly detection algorithm to flag unusual transaction behaviors based on features such as amount, sender/receiver age groups, time of transaction, and more.
  </p>

  <h2>Dataset Used</h2>
  <p>
    The dataset is taken from Kaggle and contains over 60,000 simulated UPI transactions with features including amount, transaction type, sender/receiver details, and a fraud label.
    You can explore the dataset here:
    <a href="https://www.kaggle.com/datasets/skullagos5246/upi-transactions-2024-dataset/data" target="_blank">
      UPI Transactions 2024 Dataset on Kaggle
    </a>.
  </p>

  <h2>Visual Insights</h2>
  <div class="graph-section">
    <div class="graph-container">
      <div class="graph-title">Confusion Matrix</div>
      <img src="public/image.png" alt="Confusion Matrix showing model performance with true positives, false positives, true negatives, and false negatives">
    </div>
    
    <div class="graph-container">
      <div class="graph-title">Anomalies by Sender State</div>
      <img src="public/Anomalies by Sender State.png/image.png" alt="Bar chart showing distribution of fraud predictions across different Indian states">
    </div>
    
    <div class="graph-container">
      <div class="graph-title">Amount Distribution</div>
      <img src="public/Amount Distribution.png" alt="Box plot comparing transaction amounts between normal and anomalous transactions">
    </div>
  </div>

  <div class="button-group">
    <a href="fraud-checker.html"><span class="emoji">🔍</span>Go to Fraud Checker</a>
    <a href="https://github.com/your-github-repo-link" target="_blank"><span class="emoji">🌐</span>View GitHub Repo</a>
  </div>
</div>

</body>
</html>
