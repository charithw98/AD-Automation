pipeline {
    agent any
    
    environment {
        AD_SERVER = 'ldap://10.101.16.42'  // Ensure this is correct
    }
    
    parameters {
        string(name: 'AD_USERNAME', description: 'Enter the Active Directory username to move')
        choice(name: 'DESTINATION_OU', choices: ['OU=TestOU1,DC=example,DC=com', 'OU=TestOU2,DC=example,DC=com'], description: 'Select the destination OU')
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Clone the repository containing the Python script
                git url: 'https://github.com/charithw98/AD-Automation.git', branch: 'main'
            }
        }
        
        stage('Verify Environment') {
            steps {
                // Debug steps to verify PATH and python3 availability
                sh '''
                echo "Current PATH: $PATH"
                which python3
                python3 --version
                '''
            }
        }
        
        stage('Move AD User') {
            steps {
                // Load credentials securely
                withCredentials([usernamePassword(credentialsId: 'ad_credentials', usernameVariable: 'AD_USER', passwordVariable: 'AD_PASSWORD')]) {
                    // Run the Python script with parameters using absolute path
                    sh """
                    /usr/bin/python3 move_ad_user.py ${params.AD_USERNAME} ${params.DESTINATION_OU}
                    """
                }
            }
        }
    }
}
