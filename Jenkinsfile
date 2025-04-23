pipeline {
    agent any

    environment {
        TELEGRAM_BOT_TOKEN = credentials('TELEGRAM_BOT_TOKEN')
        TELEGRAM_CHAT_ID = credentials('TELEGRAM_CHAT_ID')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Build'
            }
        }

        stage('Deploy') {
            stages{
                echo 'Deployment'
            }
        }

        stage('Test'){
            stages {
                echo 'Testing success.'
            }
        }
    }

    post {
        success {
            script {
                withCredentials([
                    string(credentialsId: 'telegram-bot-token', variable: 'BOT_TOKEN'),
                    string(credentialsId: 'telegram-chat-id', variable: 'CHAT_ID')
                ]) {
                    def date = new Date().format("yyyy-MM-dd HH:mm:ss 'UTC'", TimeZone.getTimeZone('UTC'))
                    def message = """
\u2705 *cdc_admin*, *prod*, *Phors Phearom*, ${date}
-----------------------------
*Pipeline Overview*
*ID*          : 9105
*ENVIRONMENT* : prod
*APPLICATION* : cdc_admin
*DATE*        : ${date}
*DURATION*    : 2m 37s
*STATUS*      : \u2705 success
-----------------------------
*Commit Details*
*HASH*        : 4689e5fa
*COMMITER*    : Phors Phearom
*MESSAGE*     :\n\u2022 Updated
-----------------------------
*Quick Links*
*VIEW COMMIT*   : [Link](http://git/view/4689e5fa)
*VIEW PIPELINE* : [Link](http://jenkins/pipeline/9105)
*IP*            : 10.255.1.203
*VIEW PROJECT*  : http://10.255.1.208/ipm-admin/cdc_admin
*SERVICE URL*   : https://admin.cdcdigital.net
"""
                    sh """
                    curl -s -X POST https://api.telegram.org/bot${BOT_TOKEN}/sendMessage \
                        -d chat_id=${CHAT_ID} \
                        -d parse_mode=Markdown \
                        --data-urlencode text='${message}'
                    """
                }
            }
        }
        failure {
            script {
                withCredentials([
                    string(credentialsId: 'telegram-bot-token', variable: 'BOT_TOKEN'),
                    string(credentialsId: 'telegram-chat-id', variable: 'CHAT_ID')
                ]) {
                    def date = new Date().format("yyyy-MM-dd HH:mm:ss 'UTC'", TimeZone.getTimeZone('UTC'))
                    def message = """
\u274C *cdc_admin*, *prod*, *Phors Phearom*, ${date}
-----------------------------
*Pipeline Overview*
*ID*          : 9105
*ENVIRONMENT* : prod
*APPLICATION* : cdc_admin
*DATE*        : ${date}
*STATUS*      : \u274C failed
-----------------------------
*Quick Links*
*VIEW PIPELINE* : [Link](http://jenkins/pipeline/9105)
*SERVICE URL*   : https://admin.cdcdigital.net
"""
                    sh """
                    curl -s -X POST https://api.telegram.org/bot${BOT_TOKEN}/sendMessage \
                        -d chat_id=${CHAT_ID} \
                        -d parse_mode=Markdown \
                        --data-urlencode text='${message}'
                    """
                }
            }
        }
    }
}
