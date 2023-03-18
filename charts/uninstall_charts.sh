# uninstalls
helm uninstall bootstrap-v1 
helm uninstall databases-v1 
helm uninstall grafana-config-v1 
helm uninstall monitoring-stack-v1 
helm uninstall app-v1
sh app/uninstall_flask_app.sh

# delete pvc
minikube kubectl delete pvc data-databases-v1-mariadb-0
minikube kubectl delete pvc data-databases-v1-mariadb-galera-0
minikube kubectl delete pvc data-databases-v1-mariadb-galera-1
minikube kubectl delete pvc data-databases-v1-mariadb-galera-2
minikube kubectl delete pvc data-databases-v1-postgresql-0
minikube kubectl delete pvc data-databases-v1-postgresql-ha-postgresql-0
minikube kubectl delete pvc data-databases-v1-postgresql-ha-postgresql-1
minikube kubectl delete pvc data-databases-v1-postgresql-ha-postgresql-2
minikube kubectl delete pvc databases-v1-mongodb

# rm Chart.lock
rm bootstrap/Chart.lock
rm databases/Chart.lock
rm monitoring-stack/Chart.lock
rm app/Chart.lock
