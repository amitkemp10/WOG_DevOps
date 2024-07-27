pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "amitkemp10/wog_app:v1.0"
        CONTAINER_NAME = "wog_app_container"
        DOCKER_USERNAME = "amitkemp10"
        DOCKER_PASSWORD = "Ak206078537$@"
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
                    bat 'echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin'
                    bat 'docker push %DOCKER_IMAGE%'
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