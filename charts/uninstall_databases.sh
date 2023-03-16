helm uninstall databases-v1
kubectl delete pvc data-databases-v1-mariadb-galera-0
kubectl delete pvc data-databases-v1-mariadb-galera-1
kubectl delete pvc data-databases-v1-mariadb-galera-2
rm databases/Chart.lock
