pipeline {
    agent any
    
    environment {
        AD_SERVER = 'ldap://yourserver'
    }
    
    parameters {
        string(name: 'AD_USERNAME', description: 'Enter the Active Directory username to move')
        choice(name: 'DESTINATION_OU', choices: ['OU=TestOU1,DC=example,DC=com', 'OU=TestOU2,DC=example,DC=com'], description: 'Select the destination OU')
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Clone the repository containing the Python script
                git 'https://your-repository-url.git'
            }
        }
        
        stage('Move AD User') {
            steps {
                // Load credentials securely
                withCredentials([usernamePassword(credentialsId: 'ad_credentials', usernameVariable: 'AD_USER', passwordVariable: 'AD_PASSWORD')]) {
                    // Run the Python script with parameters
                    sh """
                    python3 move_ad_user.py
                    """
                }
            }
        }
    }
}
