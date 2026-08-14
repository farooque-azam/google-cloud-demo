# Workspace Configuration & Demo Strategy

## Active Google Cloud Project
* **Project Name**: Gemini Project
* **Project ID**: `gen-lang-client-0441613979`
* All configurations and Cloud Shell operations should target this active project.

## Scenario 2: Local Free Minikube Setup (Cloud Shell)
This workspace is configured for **Scenario 2** to run classroom demonstrations for **ASE (Fall 2026)**.

* **Cluster Environment**: Local, free single-node Kubernetes cluster running inside Cloud Shell via **Minikube**.
* **GitOps Controller**: Argo CD installed within the local Minikube cluster (`argocd` namespace).
* **Cost & Access**: Completely free, running inside the Cloud Shell VM without needing paid cloud infrastructure.

## ⚠️ Required Configuration Review: `~/.customize_environment`
The environment setup script [`.customize_environment`](file:///home/farooque_azam/.customize_environment) **must be reviewed and updated**:
* **Current issue**: Lines 49–57 hardcode `PROJECT_ID="fabled-skein-412514"` and attempt `gcloud container clusters get-credentials ase-lab-cluster`.
* **Required change**: Update `PROJECT_ID` to `gen-lang-client-0441613979` and adapt the script to use `minikube start` and local `kubectl` context instead of fetching credentials for the deprecated remote GKE cluster.

## Legacy Infrastructure Notice
* The former remote GKE Google Cloud project `fabled-skein-412514` is scheduled for deletion (`DELETE_REQUESTED`). All associated remote cluster resources have been deprecated in favor of this local Minikube workflow under `gen-lang-client-0441613979`.
