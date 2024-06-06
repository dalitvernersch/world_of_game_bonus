pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/dalitvernersch/world_of_game_bonus.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t world-of-game-bonus-app .'
            }
        }

        stage('Run Migrations') {
            steps {
                sh 'docker run --rm world-of-game-bonus-app alembic upgrade head'
            }
        }

        stage('Run') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                sh 'docker exec world-of-game-app-container python3 /app/test/e2e.py http://localhost:8777'
            }
            post {
                failure {
                    echo 'Tests failed!'
                }
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker-compose down'

                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                    sh "echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin"
                    sh 'docker tag world-of-game-bonus-app $DOCKER_HUB_USERNAME/world_of_game_bonus:latest'
                    sh 'docker push $DOCKER_HUB_USERNAME/world_of_game_bonus:latest'
                }
            }
        }
    }
}
