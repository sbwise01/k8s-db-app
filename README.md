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

## kind
1. Install the kind application appropriate to your OS platform
   1. See https://kind.sigs.k8s.io/docs/user/quick-start/#installation
   1. For example, for Mac OS:  `brew install kind`
1. Create a kind cluster `kind create cluster --config ./deploy/kind/config.yaml`
1. Deploy infrastructure dependencies of the application
   1. `kubectl apply -k ./deploy/k8s/dependencies`
   1. This deploys the following infrastructure resources
      1. Database secrets
      1. Postgres database
      1. Nginx Ingress Controller
1. Deploy the kustomize:  `kubectl apply -k ./deploy/k8s/app`
   1. Alter the image in `./deploy/k8s/app/kustomization.yaml` to the one you built following the build instructions
1. Test the application using curl
   1. `curl --resolve "flaskhelloworld.info:8080:127.0.0.1" -s http://flaskhelloworld.info:8080/`
1. Test the application in a web browser
   1. Add `127.0.0.1	flaskhelloworld.info` to `/etc/hosts`
   1. Browse to http://flaskhelloworld.info:8080/
