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
                    sleep(time: 30, unit: 'SECONDS')
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image("${env.DOCKER_IMAGE}").inside {
                        dir('/tests') {
                            sh 'python e2e.py'
                        }
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    bat "docker-compose down"
                    withDockerRegistry(credentialsId: 'dockerhub-credentials-id', url: 'https://index.docker.io/v1/') {
                        docker.image("${env.DOCKER_IMAGE}").push("v1.0")
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
            bat "docker system prune -af || true"
        }
    }
}