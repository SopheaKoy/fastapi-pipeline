pipeline {
    agent any

    environment {
        TELEGRAM_BOT_TOKEN = credentials('7773964856:AAF5igwKgWTd1xRPAroZ4RgS4SpKan5OQzw')
        TELEGRAM_CHAT_ID = '6465385844' // Replace with your chat ID
    }

    stages {
        stage('Build Docker') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker-compose run --rm backend pytest tests --junitxml=report.xml'
            }
        }

        stage('Shutdown') {
            steps {
                sh 'docker-compose down'
            }
        }
    }

    post {
    success {
        node('') {
            script {
                sh """
                curl -s -X POST https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage \
                    -d chat_id=${env.TELEGRAM_CHAT_ID} \
                    -d text="✅ Build *SUCCESS* on job: ${env.JOB_NAME} (#${env.BUILD_NUMBER})" \
                    -d parse_mode=Markdown
                """
            }
        }
    }
    failure {
        node('') {
            script {
                sh """
                curl -s -X POST https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage \
                    -d chat_id=${env.TELEGRAM_CHAT_ID} \
                    -d text="❌ Build *FAILED* on job: ${env.JOB_NAME} (#${env.BUILD_NUMBER})" \
                    -d parse_mode=Markdown
                """
            }
        }
    }
}
}