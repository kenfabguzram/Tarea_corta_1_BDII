helm dependency build databases/
helm install databases-v1 databases/ --values databases/values.yaml
