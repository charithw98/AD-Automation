pipeline {
    agent any

    parameters {
        string(name: 'AD_USERNAME', defaultValue: 'exampleuser', description: 'Enter the AD username to move')
        choice(name: 'TARGET_OU', choices: ['TestOU1', 'TestOU2'], description: 'Select the target OU')
    }

    environment {
        AD_SERVER = '10.101.16.42'
        AD_USER = 'tase'
        AD_PASSWORD = 'Testuser@123'
    }

    stages {
        stage('Move AD User') {
            steps {
                script {
                    // Define the parameters from the Jenkins UI
                    def username = params.AD_USERNAME
                    def target_ou = params.TARGET_OU
                    def server_ip = env.AD_SERVER
                    def ad_user = env.AD_USER
                    def ad_password = env.AD_PASSWORD

                    // Run the Python script to move the user
                    sh """
                        python3 move_user.py ${username} ${target_ou} ${server_ip} ${ad_user} ${ad_password}
                    """
                }
            }
        }
    }

    post {
        success {
            echo "User ${params.AD_USERNAME} moved successfully."
        }
        failure {
            echo "Failed to move the user."
        }
    }
}
