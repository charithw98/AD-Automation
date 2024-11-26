pipeline {
    agent any

    environment {
        AD_SERVER = 'ldap://10.101.16.42'  // Ensure this is correct
        PIP_PACKAGES = 'ldap3'  // Required Python package
    }

    parameters {
        string(name: 'AD_USERNAME', description: 'Enter the Active Directory username to move')
        choice(name: 'DESTINATION_OU', choices: ['OU=TestOU1,DC=example,DC=com', 'OU=TestOU2,DC=example,DC=com'], description: 'Select the destination OU')
    }

    stages {
        stage('Setup Environment') {
            steps {
                sh '''
                echo "Current PATH: $PATH"
                
                # Check if Python is installed, install if missing
                if ! command -v python3 &> /dev/null; then
                    echo "Installing Python3..."
                    apt-get update && apt-get install -y python3 python3-pip
                fi

                # Verify Python version
                python3 --version
                
                # Install required Python packages
                pip3 install --upgrade pip
                pip3 install ${PIP_PACKAGES} || { echo "Failed to install packages"; exit 1; }
                '''
            }
        }

        stage('Move AD User') {
            steps {
                // Load credentials securely
                withCredentials([usernamePassword(credentialsId: 'ad_credentials', usernameVariable: 'AD_USER', passwordVariable: 'AD_PASSWORD')]) {
                    // Run the Python script with parameters
                    sh '''
                    echo "Running Python script to move AD user..."
                    python3 move_ad_user.py "${AD_USER}" "${AD_PASSWORD}" "${params.AD_USERNAME}" "${params.DESTINATION_OU}"
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs for details.'
        }
    }
}
