helm dependency build bootstrap/
helm dependency build monitoring-stack/
helm dependency build databases/
helm dependency build grafana-config/
helm dependency build app/
helm install bootstrap-v1 bootstrap/ --values bootstrap/values.yaml
helm install monitoring-stack-v1 monitoring-stack/ --values monitoring-stack/values.yaml
helm install databases-v1 databases/ --values databases/values.yaml
helm install grafana-config-v1 grafana-config/ --values grafana-config/values.yaml
helm install app/ --values app/values.yaml
