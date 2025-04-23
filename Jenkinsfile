pipeline {
    agent any

    environment {
        TELEGRAM_BOT_TOKEN = credentials('telegram-bot-token')
        TELEGRAM_CHAT_ID = '-1001234567890' // Replace with your chat ID
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
            script {
                sh '''
                curl -s -X POST https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage \
                    -d chat_id=$TELEGRAM_CHAT_ID \
                    -d text="✅ Build *SUCCESS* on job: $JOB_NAME (#$BUILD_NUMBER)" \
                    -d parse_mode=Markdown
                '''
            }
        }
        failure {
            script {
                sh '''
                curl -s -X POST https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage \
                    -d chat_id=$TELEGRAM_CHAT_ID \
                    -d text="❌ Build *FAILED* on job: $JOB_NAME (#$BUILD_NUMBER)" \
                    -d parse_mode=Markdown
                '''
            }
        }
    }
}