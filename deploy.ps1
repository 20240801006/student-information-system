$ErrorActionPreference = "Stop"

Write-Host "Building updated Docker image..."
docker build -t student-information-system:1.0 .

if ($LASTEXITCODE -ne 0) { throw "Docker build failed" }

Write-Host "Loading image into Kind..."
kind load docker-image student-information-system:1.0 --name student-system

if ($LASTEXITCODE -ne 0) { throw "Kind image load failed" }

Write-Host "Restarting Kubernetes deployment..."
kubectl rollout restart deployment/student-information-system

if ($LASTEXITCODE -ne 0) { throw "Deployment restart failed" }

Write-Host "Waiting for rollout..."
kubectl rollout status deployment/student-information-system

if ($LASTEXITCODE -ne 0) { throw "Rollout failed" }

Write-Host "Deployment completed successfully!" -ForegroundColor Green