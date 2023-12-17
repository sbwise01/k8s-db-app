# k8s-db-app
This repository contains 2 Docker containers and associated kustomize manifests to
demonstrate usage of an init container on a deployment to wait for a job.  In this
case, the job builds out a database table, and the init container waits for the job
to finish before allowing the main container on the deployment to start running and
consumer the database objects

## Build instructions
1. `docker build -t sbwise/k8s-db-app-init:1.0.3 ./db-init`
1. `docker push sbwise/k8s-db-app-init:1.0.3`
1. `docker build -t sbwise/k8s-db-app:1.0.0 ./db-app`
1. `docker push sbwise/k8s-db-app:1.0.0`

## Minikube
1. Download and install the minikube binary appropriate to your OS platform
   1. See https://github.com/kubernetes/minikube/releases
   1. For example, for Mac OS with M1 chip:  https://github.com/kubernetes/minikube/releases/download/v1.30.1/minikube-darwin-arm64.tar.gz
1. Run minikube `minikube start`
1. Deploy the kustomize:  `kubectl apply -k ./k8s`
   1. Alter the image in `./k8s/app.yaml` to the one you built following the build instructions
1. Create a port forward: `kubectl port-forward service/flaskhelloworld 5000:5000`
1. Test the application in your web browser:  `http://localhost:5000/`
