
pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '''
                if not exist venv\\Scripts\\python.exe python -m venv venv
                venv\\Scripts\\python.exe -m pip install --upgrade pip
                venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Train Diabetes Model') {
            steps {
                bat 'venv\\Scripts\\python.exe train.py'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'venv\\Scripts\\python.exe -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat 'venv\\Scripts\\python.exe monitor.py'
            }
        }
    }

    post {
        success {
            echo 'Diabetes MLOps Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
