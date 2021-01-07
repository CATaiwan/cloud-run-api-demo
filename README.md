# Cloud Run Fastapi Demo

### Environment

```
Dokcer
Python 3.8
Fastapi
```

### Local develop

- Build docker container

```
$ docker build -t cloud-run-api-demo:latest .
```

- Run api server

```
$ docker run --rm -p 8000:8000 cloud-run-api-demo:latest
```

### Deploy to Cloud Run

- gcloud set project

  ```
  $ gcloud config set project {project_id}
  ```

- Build and upload image

  ```
  $ gcloud builds submit --tag asia.gcr.io/{project_id}/cloud-run-api-demo
  ```

- Deploy to cloud run
  ```
  $ gcloud run deploy --image gcr.io/{project_id}/cloud-run-api-demo \
  --platform managed \
  --port 8000 \
  --memory 1Gi \
  --timeout=2m
  ```

### Reference

- [Cloud Run](https://cloud.google.com/run)
- [Fastapi](https://fastapi.tiangolo.com/)

