#!/bin/bash

SPARK_CONF_DIR="/usr/local/spark/conf"
SPARK_SBIN_DIR="/usr/local/spark/sbin"
WORKERS_TEMPLATE="$SPARK_CONF_DIR/workers.template"
WORKERS_FILE="$SPARK_CONF_DIR/workers"
hosts=("wor-1" "wor-2" "wor-3")


cd $SPARK_CONF_DIR
if [ ! -f "$WORKERS_TEMPLATE" ]; then
  echo "Erreur : Le fichier $WORKERS_TEMPLATE n'existe pas."
  exit 1
fi



for IP in $hosts; do
  echo "$IP" >> "$WORKERS_TEMPLATE"
done

echo "Adresses IP ajoutées au fichier workers.template."

mv "$WORKERS_TEMPLATE" "$WORKERS_FILE"
echo "Le fichier workers.template a été renommé en workers."

cd "$SPARK_SBIN_DIR" || exit 1
./start-master.sh
if [ $? -eq 0 ]; then
  echo "Le master Spark a été démarré avec succès."
else
  echo "Erreur : Impossible de démarrer le master Spark."
  exit 1
fi

 /usr/local/spark/logs/spark-root-org.apache.spark.sql.connect.service.SparkConnectServer-1-Host-004.out