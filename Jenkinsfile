pipeline {
    agent any

    environment {
        // Define environment variables (e.g., credentials or directories)
        GIT_REPO = "https://github.com/charithw98/AD-Automation.git"
        PYTHON_VERSION = "python3"
    }

     stages {
        stage('Checkout SCM') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],  // Adjust the branch name if needed
                          userRemoteConfigs: [[url: 'https://github.com/charithw98/AD-Automation.git']]
                ])
            }
        }
    }

        // Stage 2: Setup the environment
        stage('Setup Environment') {
            steps {
                script {
                    // Update the apt package list and install Python3
                    echo "Installing Python3 and necessary dependencies..."

                    // Ensure apt-get update has the proper permissions
                    sh '''#!/bin/bash
                    apt-get update
                    apt-get install -y python3 python3-pip python3-venv
                    '''

                    // Install any Python dependencies from requirements.txt
                    if (fileExists('requirements.txt')) {
                        sh '''
                        pip3 install -r requirements.txt
                        '''
                    }
                }
            }
        }

        // Stage 3: Move AD Users
        stage('Move AD User') {
            steps {
                script {
                    // Assuming move_ad_user.py is the Python script to execute
                    echo "Running AD User Migration Script..."
                    sh '''
                    python3 move_ad_user.py
                    '''
                }
            }
        }

        // Stage 4: Post Actions
        stage('Post Actions') {
            steps {
                script {
                    // Any cleanup or post-deployment tasks can go here
                    echo "Pipeline completed successfully!"
                }
            }
        }
    }

    post {
        // Handling possible errors and cleanup
        failure {
            echo "The pipeline failed. Please check the logs for errors."
        }

        success {
            echo "Pipeline executed successfully!"
        }
    }
}
