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
                    docker.image("${env.DOCKER_IMAGE}").withRun("-p 8777:8777 --name ${env.CONTAINER_NAME}") { container ->
                        sleep(time: 30, unit: 'SECONDS')
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image("${env.DOCKER_IMAGE}").inside {
                        dir('/wog_app/tests'){
                            sh 'python e2e.py'
                        }
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh "docker stop ${env.CONTAINER_NAME} || true"
                    sh "docker rm ${env.CONTAINER_NAME} || true"

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
            sh "docker system prune -af || true"
        }
    }
}