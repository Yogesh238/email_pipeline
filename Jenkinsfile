pipeline {
    agent any
    stages {
//         stage('sending email') {
//             steps {
//                 sh 'python3 text.py'
//             }
//         }
        stage('Approval') {
            // no agent, so executors are not used up when waiting for approvals
            agent none
            steps {
                script {
                    def deploymentDelay = input (id: 'Deploy', message: 'Deploy to production?', submitter: 'user1', parameters: [[$class: 'BooleanParameterDefinition', defaultValue: true, description: '', name: 'Please confirm you agree with this']])
                }
            }
        }
        stage('Deploy') {
            agent any
            steps {
                // uses https://plugins.jenkins.io/lockable-resources
               // lock(resource: 'deployApplication'){
                    echo 'Deploying...'
            }
        }
    }
}
