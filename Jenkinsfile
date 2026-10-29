pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python train.py'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat 'python monitor.py'
            }
        }
    }
}