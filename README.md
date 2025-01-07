# AI-in-Devops

What is AI in Devops?
   
AI is growing rapidly in all software streams, I would like to focus on leveraging GenAI in to devops (let's explore this thoroughly).
AI in DevOps is an added benefit that enhances and empowers DevOps engineers to become more efficient. Here are some things you can do to leverage AI in DevOps.

You may have already heard about using AI tools to generate scripts, manifest files, Jenkins files, and other DevOps artifacts. However, here are some more valuable ways to leverage these tools:

* Proactive analysis:
    * Monitor system metrics and logs to predict potential issues before they become critical
    * Analyze code quality and security vulnerabilities during development
    * Forecast resource utilization and capacity needs
* Anomaly detection:
    * Identify unusual patterns in system behavior and performance
    * Detect security threats and suspicious activities in real-time
    * Flag irregular deployment patterns or configuration changes
* Pattern Recognition and Process Optimization:
    * Analyze historical data to identify performance bottlenecks
    * Discover recurring issues in deployment pipelines
    * Optimize resource allocation based on usage patterns
    * Identify gaps in existing processes and suggest improvements

# AI Tools that Devops can use:

**Github Copilot/Amazon Q** 

  * For Amazon Q: Sign up for an AWS account and install the Amazon Q plugin in your preferred IDE
  * For GitHub Copilot: Create a GitHub account and install the Copilot extension in your IDE

These AI assistants can significantly boost your DevOps productivity by helping with:

* Generating and optimizing Terraform configurations
* Writing Python and Bash scripts
* Formatting code automatically
* Providing code suggestions in real-time
* Explaining code and suggesting improvements

Note: While both services offer free tiers, be sure to review their current pricing and limitations before getting started. GitHub Copilot is free for students and maintainers of popular open-source projects, while Amazon Q offers certain features in its free tier.

**ChatGPT, Claude, Gemini** 

* You can create a free account with these, (feature limitations)
* These can be used as your Problem-Solving Companions that provides assistance in debugging an issue, Understand error messages and get actionable solutions.
* Get guidance on performance optimization
* Receive infrastructure scaling recommendations
* Get explanations of complex concepts & Compare different tools and approaches

**DevOps SaaS tools are integrating AI features**

* Monitoring & Observability: Datadog (AI-powered log analysis), New Relic (Anomaly detection & Incident prediction), Dynatrace (Automatic problem detection)
* Security Tools: Snyk(AI-powered vulnerability detection)
* Infrastructure Management: HashiCorp (Configuration optimization, Security compliance checking) AWS DevOps Tools

# Sample demonstration :

I want to demonstrate a simple use case by parsing an Nginx log file and extracting the following metrics by running log_analyzer.py with nginx.log

* **Traffic Patterns**: Group logs by time intervals (e.g., hourly, daily) to analyze traffic volume.
* **Traffic Anomalies**: Identify anomalies in traffic patterns.
* **Traffic Forecasting**: Forecast future traffic based on historical data.

 **I am using below open source Machine learning models in my script for Anomaly detection & Forecasting**

# IsolationForest:  
* Type: Machine Learning Model
* Library: sklearn.ensemble
* Purpose: Anomaly Detection
* Description: Isolation Forest is an unsupervised learning algorithm used for anomaly detection. It works by isolating observations by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of the selected feature. The logic is that anomalies are few and different, and they are easier to isolate. It is an open-source model provided by the scikit-learn library.

# Prophet:
* Type: Machine Learning Model
* Library: prophet
* Learning Type: Supervised Learning
* Purpose: Time Series Forecasting
* Description: Prophet is a forecasting tool developed by Facebook (Meta) for time series data. It is designed to handle missing data and shifts in the trend, and it works well with daily observations that display seasonality. It is an open-source model and is particularly useful for forecasting traffic, sales, and other time-dependent data. Prophet is a supervised learning model because it uses historical data to predict future values.

**Here are the metrics after running the script**


<img width="596" alt="image" src="https://github.com/user-attachments/assets/a05c47e3-a6f6-43c7-904b-09878cb7886c" />

                     **Above picture shows traffic trends**

<img width="604" alt="image" src="https://github.com/user-attachments/assets/bdf9de41-2a8b-41d9-9a53-031cb8264e11" />

                     **Above picture shows anamalies in traffic**

<img width="981" alt="image" src="https://github.com/user-attachments/assets/ebf13aa9-37af-46c8-988c-7bee64f68565" />

                     **Above picture shows forecast traffic**


**Note: In this demonstration, I utilized open-source machine learning models to analyze historical data, detect anomalies, and make forecasts. Implementing such models effectively requires a comprehensive setup and thorough training to achieve real-time metrics and improved accuracy.**


# Useful blogs for Devops

* This page here provides better understanding of an AI model and different types of models and their uses. (Refer them)
     https://www.geeksforgeeks.org/common-ai-models-and-when-to-use-them/

* Sample prompts to use in Devops.
     https://gartdevops.medium.com/10-chatgpt-prompts-to-use-in-devops-dddc0d599ec8
