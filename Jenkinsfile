pipeline {
    agent any

    parameters {
        string(name: 'USERNAME', defaultValue: '', description: 'Enter the username to move.')
        choice(name: 'DESTINATION_OU', choices: ['OU=TestOU1,DC=example,DC=com', 'OU=TestOU2,DC=example,DC=com'], description: 'Select the destination OU')
    }

    environment {
        AD_SERVER = 'ldap://yourserver'  // Replace with your actual AD server
    }

    stages {
        stage('Checkout') {
            steps {
                // Assuming the script is in the repository
                git 'https://your-repository-url.git'
            }
        }

        stage('Move AD User') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'ad_credentials', usernameVariable: 'AD_USER', passwordVariable: 'AD_PASSWORD')]) {
                    // Run the Python script, passing parameters
                    sh """
                    python3 move_ad_user.py
                    """
                }
            }
        }
    }
}
