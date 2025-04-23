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
            steps {
                echo 'Deployment'
            }
        }

        stage('Test'){
            steps {
                echo 'Testing success.'
            }
        }
    }

    post {
        success {
            script {
                withCredentials([
                    string(credentialsId: 'TELEGRAM_BOT_TOKEN', variable: 'TELEGRAM_BOT_TOKEN'),
                    string(credentialsId: 'TELEGRAM_CHAT_ID', variable: 'CHAT_ID')
                ]) {
                    def date = new Date().format("yyyy-MM-dd HH:mm:ss 'UTC'", TimeZone.getTimeZone('UTC'))
                    def message = """
\u2705 *fastapi*, *dev*, *Ding Dann*, ${date}
-----------------------------
*Pipeline Overview*
*ID*          : 9105
*ENVIRONMENT* : dev
*APPLICATION* : fastapi
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
*SERVICE URL*   : Null
"""
                    sh """
                    curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage \
                        -d chat_id=${TELEGRAM_CHAT_ID} \
                        -d parse_mode=Markdown \
                        --data-urlencode text='${message}'
                    """
                }
            }
        }
        failure {
            script {
                withCredentials([
                    string(credentialsId: 'TELEGRAM_BOT_TOKEN', variable: 'TELEGRAM_BOT_TOKEN'),
                    string(credentialsId: 'TELEGRAM_CHAT_ID', variable: 'TELEGRAM_CHAT_ID')
                ]) {
                    def date = new Date().format("yyyy-MM-dd HH:mm:ss 'UTC'", TimeZone.getTimeZone('UTC'))
                    def message = """
\u274C *fastapi*, *dev*, *Ding Dann*, ${date}
-----------------------------
*Pipeline Overview*
*ID*          : 9105
*ENVIRONMENT* : dev
*APPLICATION* : cdc_admin
*DATE*        : ${date}
*STATUS*      : \u274C failed
-----------------------------
*Quick Links*
*VIEW PIPELINE* : [Link](http://jenkins/pipeline/9105)
*SERVICE URL*   : Null
"""
                    sh """
                    curl -s -X POST https://api.telegram.org/bot${TELEGRAM_CHAT_ID}/sendMessage \
                        -d chat_id=${TELEGRAM_CHAT_ID} \
                        -d parse_mode=Markdown \
                        --data-urlencode text='${message}'
                    """
                }
            }
        }
    }
}
