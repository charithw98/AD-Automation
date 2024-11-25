pipeline {
    agent any  // Runs on any available Jenkins agent

    environment {
        GIT_REPO = 'https://github.com/charithw98/AD-Automation.git'
        SCRIPT_NAME = 'move_ad_user.py'  // Name of the Python script
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
                echo 'Installing Python dependencies...'
                sh 'pip install -r requirements.txt'  // Ensure a requirements.txt file exists
            }
        }

        stage('Run Script') {
            steps {
                echo 'Running the Python script...'
                sh "python ${SCRIPT_NAME}"
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
