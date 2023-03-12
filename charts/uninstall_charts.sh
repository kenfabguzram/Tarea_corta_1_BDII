helm uninstall bootstrap-v1 databases-v1 grafana-config-v1 monitoring-stack-v1 flask-app-v1
rm bootstrap/Chart.lock
rm databases/Chart.lock
rm monitoring-stack/Chart.lock
rm app/Chart.lock
