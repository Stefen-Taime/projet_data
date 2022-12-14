#!/usr/bin/env bash
up() {
  echo "Starting Airflow..."
  docker-compose down -v    
  docker-compose up airflow-init
  docker-compose up -d

  echo "Access Airflow at http://localhost:8080"  
}


case $1 in
  up)
    up
    ;;
  config)
    config
    ;;
  down)
    down
    ;;
  *)
    echo "Usage: $0 {up|config|down}"
    ;;
esac