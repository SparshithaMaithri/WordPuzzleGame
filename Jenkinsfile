pipeline {
    agent any

    environment {
        // 🧭 Full PATH so Jenkins can find all necessary tools
        PATH = "C:\\Program Files\\Docker\\Docker\\resources\\bin;" +
               "C:\\Program Files\\Kubernetes\\;" +
               "C:\\Program Files\\Git\\cmd;" +
               "C:\\Program Files\\nodejs\\;" +
               "C:\\Program Files\\Python312\\Scripts\\;" +
               "C:\\Program Files\\Python312\\;" +
               "C:\\Windows\\System32;" +
               "C:\\Windows;" +
               "C:\\Windows\\System32\\Wbem;" +
               "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;" +
               "${PATH}"

        // 🧩 Kube configuration for your Kubernetes cluster
        KUBECONFIG = "C:\\Users\\spmah\\.kube\\config"

        // 📁 Project directory
        PROJECT_DIR = "C:\\Users\\spmah\\Downloads\\WordPuzzle"
    }

    stages {
        stage('Verify Tools') {
            steps {
                echo "🔍 Checking Docker & Kubectl setup..."
                bat '''
                docker --version
                kubectl version --client
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🏗️ Building Word Puzzle Docker Image..."
                dir("${PROJECT_DIR}") {
                    bat 'docker build -t wordpuzzleapp:v1 .'
                }
            }
        }

        stage('Docker Login') {
            steps {
                echo "🔐 Logging into Docker Hub..."
                // ⚠️ Replace password with Jenkins credentials later for security
                bat 'docker login -u sparshitha -p 0213_Csptha'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "🚀 Pushing Docker Image to Docker Hub..."
                bat '''
                docker tag wordpuzzleapp:v1 sparshitha/wordpuzzle:latest
                docker push sparshitha/wordpuzzle:latest
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "⚙️ Deploying Word Puzzle app to Kubernetes..."
                bat '''
                kubectl cluster-info
                kubectl apply -f C:\\Users\\spmah\\Downloads\\WordPuzzle\\deployment.yaml
                kubectl apply -f C:\\Users\\spmah\\Downloads\\WordPuzzle\\service.yaml
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "🔎 Checking Kubernetes deployment status..."
                bat '''
                kubectl get pods
                kubectl get svc
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Word Puzzle Game successfully built, pushed, and deployed!"
            echo "🌍 Access it at http://localhost:31125"
        }
        failure {
            echo "❌ Pipeline failed. Check the Jenkins console output for details."
        }
    }
}
