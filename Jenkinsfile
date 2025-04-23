pipeline {
    agent any

    environment {
        TELEGRAM_BOT_TOKEN = credentials('TELEGRAM_BOT_TOKEN')
        TELEGRAM_CHAT_ID = credentials('TELEGRAM_CHAT_ID')
    }

    stages {
        stage('Check version docker compose') {
            steps {
                echo 'Hello Developer'
            }
        }

        // stage('Run Tests') {
        //     steps {
        //         sh 'docker-compose run --rm backend pytest tests --junitxml=report.xml'
        //     }
        // }

        // stage('Shutdown') {
        //     steps {
        //         sh 'docker-compose down'
        //     }
        // }
    }

    // post {
    //     success {
    //         node('') {
    //             script {
    //                 sh """
    //                 curl -s -X POST https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage \
    //                     -d chat_id=${env.TELEGRAM_CHAT_ID} \
    //                     -d text="✅ Build *SUCCESS* on job: ${env.JOB_NAME} (#${env.BUILD_NUMBER})" \
    //                     -d parse_mode=Markdown
    //                 """
    //             }
    //         }
    //     }
    //     failure {
    //         node('') {
    //             script {
    //                 sh """
    //                 curl -s -X POST https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage \
    //                     -d chat_id=${env.TELEGRAM_CHAT_ID} \
    //                     -d text="❌ Build *FAILED* on job: ${env.JOB_NAME} (#${env.BUILD_NUMBER})" \
    //                     -d parse_mode=Markdown
    //                 """
    //             }
    //         }
    //     }
    // }
    post {
        success {
            script {
                withCredentials([
                    string(credentialsId: 'TELEGRAM_BOT_TOKEN', variable: 'BOT_TOKEN'),
                    string(credentialsId: 'TELEGRAM_CHAT_ID', variable: 'CHAT_ID')
                ]) {
                    sh '''#!/bin/bash
                    curl -s -X POST https://api.telegram.org/bot${BOT_TOKEN}/sendMessage \
                        -d chat_id=${CHAT_ID} \
                        -d text="✅ Build *SUCCESS* on job: ${JOB_NAME} (#${BUILD_NUMBER})" \
                        -d parse_mode=Markdown
                    '''
                }
            }
        }
        failure {
            script {
                withCredentials([
                    string(credentialsId: 'TELEGRAM_BOT_TOKEN', variable: 'BOT_TOKEN'),
                    string(credentialsId: 'TELEGRAM_CHAT_ID', variable: 'CHAT_ID')
                ]) {
                    sh '''#!/bin/bash
                    curl -s -X POST https://api.telegram.org/bot${BOT_TOKEN}/sendMessage \
                        -d chat_id=${CHAT_ID} \
                        -d text="❌ Build *FAILED* on job: ${JOB_NAME} (#${BUILD_NUMBER})" \
                        -d parse_mode=Markdown
                    '''
                }
            }
        }
    }
}