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
        stage('Verify Environment') {
            steps {
                // Verify that Python3 is available
                sh '''
                echo "Current PATH: $PATH"
                python3 --version || { echo "Python3 not found"; exit 1; }
                '''
            }
        }

        stage('Move AD User') {
            steps {
                // Load credentials securely
                withCredentials([usernamePassword(credentialsId: 'ad_credentials', usernameVariable: 'AD_USER', passwordVariable: 'AD_PASSWORD')]) {
                    // Run the Python script with parameters
                    sh """
                    python3 move_ad_user.py ${params.AD_USERNAME} ${params.DESTINATION_OU}
                    """
                }
            }
        }
    }
}
