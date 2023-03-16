helm uninstall bootstrap-v1 
helm uninstall databases-v1 
helm uninstall grafana-config-v1 
helm uninstall monitoring-stack-v1 
helm uninstall app-v1
minikube kubectl delete pvc data-databases-v1-mariadb-galera-0
minikube kubectl delete pvc data-databases-v1-mariadb-galera-1
minikube kubectl delete pvc data-databases-v1-mariadb-galera-2
rm bootstrap/Chart.lock
rm databases/Chart.lock
rm monitoring-stack/Chart.lock
rm app/Chart.lock
