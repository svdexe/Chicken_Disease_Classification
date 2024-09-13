# 🐔 Chicken Disease Classification Project

![Python](https://img.shields.io/badge/python-v3.8-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-v2.x-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A state-of-the-art deep learning project for classifying chicken diseases using fecal image analysis. This project implements a complete machine learning pipeline from data ingestion to model deployment, utilizing Convolutional Neural Networks (CNNs) for accurate disease detection.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Benefits](#project-benefits)
- [Project Architecture](#project-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Deployment](#deployment)
- [License](#license)

## 🔍 Project Overview

Early detection of diseases in poultry farming is crucial for maintaining bird health and optimizing production. This project aims to automate the process of identifying chicken diseases through the analysis of fecal images, providing a quick and non-invasive diagnostic tool for farmers and veterinarians.

### 🌟 Features

- Data ingestion pipeline for processing fecal images
- Custom CNN architecture based on VGG16 for image classification
- Transfer learning techniques for improved model performance
- Modular and scalable code structure
- CI/CD pipelines for AWS and Azure deployment
- Interactive web interface for real-time disease classification

## 💡 Project Benefits

This Chicken Disease Classification project offers several potential benefits to the poultry farming industry and beyond:

1. **Early Disease Detection**: Enables rapid identification of potential health issues in chicken flocks, allowing for timely intervention and treatment.

2. **Cost-Effective Monitoring**: Provides a non-invasive and cost-efficient method for regular health checks, reducing the need for expensive and time-consuming laboratory tests.

3. **Improved Farm Management**: Helps farmers make data-driven decisions about flock health, potentially improving overall farm productivity and profitability.

4. **Scalable Solution**: The modular architecture allows for easy scaling and adaptation to different farm sizes and types.

5. **Reduced Antibiotic Use**: By enabling early and accurate disease detection, the system may contribute to more targeted use of antibiotics, addressing concerns about antibiotic resistance.

6. **Enhanced Food Safety**: Indirectly contributes to food safety by promoting healthier flocks and potentially reducing the spread of diseases.

7. **Research Tool**: Serves as a valuable tool for veterinary researchers studying poultry diseases and their manifestations.

8. **Technology Integration**: Demonstrates the potential of AI and machine learning in agriculture, paving the way for further technological advancements in the field.

## 🏗️ Project Architecture

```
Chicken-Disease-Classification/
│
├── artifacts/               # Model artifacts and pipeline outputs
├── config/                  # Configuration files
├── logs/                    # Log files
├── research/                # Jupyter notebooks for experimentation
├── src/                     # Source code
│   └── cnnClassifier/
│       ├── components/      # Individual pipeline components
│       ├── config/          # Configuration management
│       ├── constants/       # Project constants
│       ├── entity/          # Data models and schemas
│       ├── pipeline/        # ML pipeline modules
│       └── utils/           # Utility functions
│
├── static/                  # Static files for web interface
├── templates/               # HTML templates
├── tests/                   # Unit and integration tests
├── .dvcignore
├── .gitignore
├── app.py                   # Flask application
├── dvc.yaml                 # DVC pipeline configuration
├── params.yaml              # Model parameters
├── requirements.txt         # Project dependencies
└── setup.py                 # Package and distribution management
```

## 🖼️ Website Interface

![Chicken Disease Classifier Interface](path_to_your_screenshot.png)

*Add a brief description of your web interface and its features here.*

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Chicken-Disease-Classification-Project.git
   cd Chicken-Disease-Classification-Project
   ```

2. Create and activate a conda environment:
   ```bash
   conda create -n cnncls python=3.8 -y
   conda activate cnncls
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

To run the application locally:

```bash
python app.py
```

Navigate to `http://localhost:5000` in your web browser to access the interface.

## 🧠 Model Training and Evaluation

### Data Version Control (DVC)

We use DVC to manage our ML pipelines. Here are the main commands:

```bash
dvc init
dvc repro
dvc dag
```

### Workflow Steps

1. Update `config.yaml`
2. Update `params.yaml`
3. Update the entity
4. Update the configuration manager in `src/config`
5. Update the components
6. Update the pipeline
7. Update `main.py`
8. Update `dvc.yaml`

## 🚢 Deployment

### AWS CI/CD Deployment with GitHub Actions

#### 1. Login to AWS console

#### 2. Create IAM user for deployment
- Set up user with programmatic access
- Assign following permissions:
  - EC2 access: Allows management of virtual machines
  - ECR: Elastic Container Registry to store docker images
  
**Required Policies:**
  - `AmazonEC2ContainerRegistryFullAccess`
  - `AmazonEC2FullAccess`

**Deployment Process Overview:**
1. Build docker image of the source code
2. Push docker image to ECR
3. Launch EC2 instance 
4. Pull image from ECR to EC2
5. Launch docker image in EC2

#### 3. Create ECR repository
- This will store/save your docker image
- Note the URI, e.g., `566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken`

#### 4. Create EC2 machine
- Choose Ubuntu as the operating system

#### 5. Install docker on EC2
```bash
# Update and upgrade packages
sudo apt-get update -y
sudo apt-get upgrade

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

#### 6. Configure EC2 as self-hosted runner
1. In your GitHub repository, go to Settings > Actions > Runner
2. Click on "New self-hosted runner"
3. Choose the operating system
4. Follow the command-line instructions provided

#### 7. Set up GitHub secrets
In your GitHub repository, go to Settings > Secrets and add the following:
```
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
AWS_REGION=us-east-1
AWS_ECR_LOGIN_URI=566373416292.dkr.ecr.ap-south-1.amazonaws.com
ECR_REPOSITORY_NAME=simple-app
```

With these steps completed, your AWS CI/CD pipeline with GitHub Actions should be ready to deploy your application automatically when you push changes to your repository.



### Azure CI/CD Deployment with GitHub Actions

Azure provides a straightforward way to set up CI/CD deployment using GitHub Actions. Follow these steps to deploy your application:

#### 1. Azure Container Registry (ACR) Setup
- Create an Azure Container Registry
- Note down the login server name

#### 2. Prepare and Push Docker Image
Run these commands from your local terminal:
```bash
# Build the Docker image
docker build -t chickenapp.azurecr.io/chicken:latest .

# Login to your Azure Container Registry
docker login chickenapp.azurecr.io

# Push the image to ACR
docker push chickenapp.azurecr.io/chicken:latest
```

#### 3. Azure Web App Deployment
1. Create a Web App in Azure
2. Configure it to use the Docker Container from ACR

#### 4. Set Up GitHub Actions with Azure

Azure can automatically set up GitHub Actions for your CI/CD pipeline:

1. In the Azure portal, navigate to your Web App
2. Go to the "Deployment Center" section
3. Choose GitHub as your source control
4. Authenticate and select your repository
5. Azure will automatically generate and commit a GitHub Actions workflow file to your repository

#### 5. Deployment Process Overview
1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure
4. Pull the Docker image from the container registry to Web App server and run

With these steps completed, your Azure CI/CD pipeline with GitHub Actions will automatically deploy your application when you push changes to your repository.

Note: Ensure that you keep any automatically generated files and credentials secure, as they may contain sensitive information about your Azure resources.

## 👨‍💻 Contributor

- Shivam Dali is a Data Science graduate student from Adelaide University. Connect with him on [LinkedIn](https://www.linkedin.com/in/shivam-dali-86b0a1201/) and explore more projects on [GitHub](https://https://github.com/svdexe).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Krish Naik](https://github.com/krishnaik06/Chicken-Disease-Classification-Project) for the inspiring tutorial


## Additional Resources
- [Medium Article](https://medium.com/@SVD.exe/end-to-end-text-summarization-nlp-project-with-aws-deployment-8e2d18b6caa7) - Read the detailed project review on Medium.
- [GitHub Repository](https://github.com/svdexe/NLP_TextSummarizer) - Access the code and project files.
- [LinkedIn](https://www.linkedin.com/in/shivam-dali-86b0a1201/) - Connect with me on LinkedIn.

## Tutorial Link
I followed this tutorial: [End To End NLP Project Implementation With Deployment Github Action- Text Summarization- Krish Naik](https://www.youtube.com/watch?v=p1bfK8ZJgkE&pp=ygUpY2hpY2tlbiBkaXNlYXNlIGNsYXNzaWZpY2F0aW9uIGtyaXNoIG5haWs%3D)
