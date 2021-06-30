pipeline {
    agent any
     
    stages {
        stage('send email') {
            steps {
                sh 'python3 email.py'
            }
        }     
    }
}
