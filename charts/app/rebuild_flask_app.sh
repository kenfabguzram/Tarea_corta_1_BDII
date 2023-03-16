docker build -t isolis2000/flask-app .
docker push isolis2000/flask-app:latest
sh uninstall_flask_app.sh 
minikube kubectl -- apply -f Deployment.yaml