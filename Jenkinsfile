pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "amitkemp10/wog_app:v1.0"
        CONTAINER_NAME = "wog_app_container"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}", ".")
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    bat 'docker-compose up -d'
                    sleep(time: 10, unit: 'SECONDS')
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat 'python ./tests/e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    bat 'docker-compose down'
                    withDockerRegistry(credentialsId: 'f9af52af-4330-49f8-bd03-7464b52334c0', url: 'https://index.docker.io/') {
                        docker.image("${env.DOCKER_IMAGE}").push("v1.0")
                    }
                }
            }
        }
    }

//     post {
//         always {
//             cleanWs()
//             bat "docker system prune -af || true"
//         }
//     }
}