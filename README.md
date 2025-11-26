3-Day Project: Cloud-Native DevOps Pipeline for FastAPI on AKS 

Project title: Cloud-Native DevOps Pipeline for a Containerized FastAPI App on Azure AKS with Terraform, Helm, GitHub Actions, and Monitoring
A FastAPI app containerized and pushed to Azure Container Registry (ACR), provisioned AKS via Terraform, deployed using a Helm chart, CI/CD using GitHub Actions (reusable workflows), monitoring with Prometheus + Grafana, and basic logging/observability pointers.

Contents 

**Day-by-day tasks and checklist (Day 1, Day 2, Day 3)**
Full minimal FastAPI app (app/main.py)
Dockerfile (multi-stage)
Helm chart (templates + values)
Terraform (main.tf, variables.tf, outputs.tf)
GitHub Actions workflows (ci.yml, cd.yml, reusable templates)
Prometheus scrape basic config & Grafana dashboard notes
README / Runbook (how to run locally and in Azure)
Scenario-based interview questions (with model answers)

**Prerequisites:**

You have an Azure subscription and Azure CLI logged in (`az login`).
You have GitHub repo created and permissions to push/workflows.
`kubectl`, `helm`, `terraform`, `docker`, and `az` installed locally.
Replace placeholders like `<SUBSCRIPTION_ID>`, `<RESOURCE_GROUP>`, `<ACR_NAME>`, `<AKS_CLUSTER_NAME>`, and `<GITHUB_REPO>` with your values.

I find that dividing a project into distinct daily phases allows for a more thorough and focused approach to each component.

**Day 1: Build, Containerize, Push to ACR**

Create FastAPI app
Create Dockerfile
Build image and test locally
Create Azure Container Registry (ACR) or Terraform later
Push image to ACR
Commit code to GitHub

Tip: For production use, prefer managed identities and `az acr update --admin-enabled false` and use `az aks update --attach-acr` instead of admin credentials.

**Day 2: Terraform (AKS) + Helm Chart + Deploy**

Terraform files to create Resource Group, ACR, AKS
`terraform init` && `terraform apply`
 Create Helm chart and templates
Deploy Helm to AKS
Verify pods and services

After apply: get credentials:
az aks get-credentials --resource-group rg-devops-demo --name <AKS_CLUSTER_NAME>
kubectl get nodes

Note: Add ingress.yaml if you want a domain with ingress controller.



**Day 2 continued: Helm deploy**

helm install fastapi-release ./fastapi-chart --set image.repository=<ACR_LOGIN_SERVER>/fastapi-sample --set image.tag=v1
kubectl get pods
kubectl get svc
kubectl describe pod <pod-name>

**Day 2 extra: GitHub Actions (CI + CD)**

Project will have 3 workflow files:

.github/workflows/ci.yml` (build + test + push image to ACR)
.github/workflows/cd.yml` (deploy to AKS via helm)
.github/workflows/reusable/deploy.yaml` (reusable workflow called by cd.yml)

 
Secrets required: `ACR_LOGIN` (e.g. myacr.azurecr.io/fastapi-sample), `ACR_USERNAME`, `ACR_PASSWORD` (or use `AZURE_CONTAINER_REGISTRY` PAT or OIDC to login)


**Day 3: Monitoring + Observability + Documentation**

Prometheus & Grafana via Helm

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install monitoring prometheus-community/kube-prometheus-stack
helm install grafana grafana/grafana

Scrape target: your FastAPI metrics endpoint

Prometheus automatically scrapes kube-service endpoints. If needed, annotate the Service or Pod for scraping. Example Service annotation for Prometheus Operator using `prometheus.io/scrape: 'true'`.

 Basic Grafana dashboard ideas

Uptime/Availability (using `/health`) metrics
Request rate (fastapi_requests_total)
Error rate (if you instrument errors)
Pod CPU / Memory usage

Happy Learning !!!!!
