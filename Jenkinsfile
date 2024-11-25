pipeline {
    agent any  // Runs on any available Jenkins agent

    environment {
        GIT_REPO = 'https://github.com/charithw98/AD-Automation.git'
        SCRIPT_NAME = 'move_ad_user.py'
        AD_SERVER = 'YourADServerAddress'  // Replace with your AD server address if needed
    }

    parameters {
        string(name: 'USERNAME', description: 'Enter the username to move')
        choice(name: 'TARGET_OU', choices: ['OU1', 'OU2', 'OU3'], description: 'Select the target OU')
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository...'
                git branch: 'main', url: "${GIT_REPO}"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python and dependencies...'
                // Ensure Python is installed and dependencies are added here
                sh '''
                sudo apt-get update
                sudo apt-get install -y python3 python3-pip
                pip3 install ldap3 pywinrm
                '''
            }
        }

        stage('Run Script') {
            steps {
                echo 'Running the Python script...'
                sh "python3 ${SCRIPT_NAME} --username ${params.USERNAME} --target_ou ${params.TARGET_OU}"
            }
        }
    }

    post {
        success {
            echo 'User successfully moved in Active Directory.'
        }
        failure {
            echo 'Failed to move user.'
        }
    }
}
