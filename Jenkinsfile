pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Start Services') {
            steps {
                sh 'docker-compose build'
                sh 'docker-compose up -d'
                // Optional: wait for FastAPI to be up (basic healthcheck)
                sh 'sleep 5'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests inside the backend container
                sh 'docker-compose exec backend pytest tests --junitxml=report.xml'
            }
        }

        stage('Archive Test Results') {
            steps {
                junit 'report.xml'
            }
        }

        stage('Shutdown Services') {
            steps {
                sh 'docker-compose down'
            }
        }
    }

    post {
        always {
            echo '🔁 Pipeline complete!'
        }
        failure {
            echo '❌ Something went wrong.'
        }
    }
}
