pipeline {
    agent any
    environment {
        //GIT_REPO = 'https://github.com/charithw98/AD-Automation.git'
        SCRIPT_NAME = 'move_ad_user.py'
    }
    parameters {
        string(name: 'USERNAME', description: 'Enter the AD username to move.')
        choice(name: 'TARGET_OU', choices: ['OU=TestOU1,DC=test,DC=com', 'OU=TestOU2,DC=test,DC=com'], description: 'Select the target OU.')
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: "${GIT_REPO}"
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install ldap3'
            }
        }
        stage('Run Script') {
            steps {
                sh "python3 ${SCRIPT_NAME} ${USERNAME} ${TARGET_OU}"
            }
        }
    }
    post {
        success {
            echo 'User moved successfully!'
        }
        failure {
            echo 'Failed to move user.'
        }
    }
}
