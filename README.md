# customer-churn-analysis
This project is a machine development application developed to predict customer churn. The cleanliness of Jupyter Notebook was verified and the model was trained, and the model that gave the most successful results was created with xgboost. Additionally, an interactive web block has been developed using Streamlit and the application is containerized and distributed on Docker.

## Technology and Tools

- **Data Analysis:** Detailed data analysis using Python.
- **Interface Design:** Interactive web interface developed with Streamlit.
- **Project Management:** Code management on GitHub and integration with Streamlit Cloud.

## Purpose and Objectives of the Project

- **Purpose:** Understanding the reasons why customers leave and using this information to improve businesses' customer relationship strategies.
- **Objective:** To enable businesses to develop their customer management and marketing strategies with a data-driven approach.

## Proje Demo

![projefoto](https://github.com/frktsc/customer-churn-analysis/blob/main/Screenshot%202024-01-19%20233916.png?raw=true)

![projefoto](https://github.com/frktsc/customer-churn-analysis/blob/main/Screenshot%202024-01-19%20221820.png?raw=true)

![projefoto](https://github.com/frktsc/customer-churn-analysis/blob/main/Screenshot%202024-01-19%20221646.png?raw=true)

# Customer Churn Analysis Docker Instructions

## Prerequisites

Before you begin, make sure you have Docker installed on your system. You can download and install Docker from the [official Docker website](https://www.docker.com/get-started).

## Building the Docker Image

To build the Docker image for the Bank Marketing App, use the following command:

```bash
docker build -t myapp .
```
This command will build a Docker image with the name "myapp" using the Dockerfile located in the current directory (`.`). Be sure to run this command in the same directory as your Dockerfile.

## Running the Docker Container

Once the Docker image is built, you can run the Customer Churn app in a Docker container using the following command:

```bash
docker run -p 5000:5000 myapp
```

This command starts a Docker container based on the "myapp" image and maps port 5000 from the container to port 5000 on your host machine. You can access the Customer churn analysis by opening a web browser and navigating to `http://localhost`.

### Optional: Running on a Different Port

If port 5000 is already in use on your host machine, you can choose a different available port by modifying the `-p` option. For example, to use port 8080 on your host, you can run:

```bash
docker run -p 8080:80 myapp
```

Click [here](https://churn-analysis-99.streamlit.app/) to experience app
