helm uninstall app-v1
rm app/Chart.lock
rm app/charts/*
helm dependency build app/
helm install app-v1 app/ --values app/values.yaml
