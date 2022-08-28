

pipeline {
    agent  any

    stages {

        stage('Install Python Libraries'){
            steps {
                sh '''
                    pip install -r requirements.txt
                    python3 -m pip install pytest allure-python-commons allure-pytest pytest-html
                '''
            }
        }

        stage("Running Test & Report "){
            steps {
                sh '''
                    python3 -m pytest --html=report.html --alluredir=allure-results
                '''
            }
        }

        stage('Build Image'){
            steps {
                sh '''
                    docker image build -t tamer-assi/django-project .
                '''
            }
        }
                stage('Run Container'){
            steps {
                sh '''
                    docker run -p 8000:8000 -d tamer-assi/django-project
                '''
            }
        }
                stage('Run Tests on container'){
            steps {
                sh '''
                    python3 -m pytest ./tests/E2E
                '''
            }
        }
    }

    post{
        failure {
        // Create Jira issue and attach html report.
        echo 'Build has failed opening jira issue!'
      }

      always{
            publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: '', reportFiles: 'report.html', reportName: 'HTML Report', reportTitles: ''])
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
    }
}
