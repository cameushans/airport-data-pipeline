#!/usr/bin/env bash

# Définir les variables
SPARK_VERSION="3.5.2"
SPARK_ARCHIVE="spark-${SPARK_VERSION}-bin-hadoop3.tgz"
SPARK_URL="https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/${SPARK_ARCHIVE}"
SPARK_DIR="spark-${SPARK_VERSION}-bin-hadoop3"
INSTALL_DIR="$HOME/spark"

# Télécharger et décompresser Spark
echo "Téléchargement de Spark..."
wget $SPARK_URL -O $SPARK_ARCHIVE

echo "Décompression de Spark..."
tar -xzf $SPARK_ARCHIVE

# Créer le dossier d'installation si nécessaire
mkdir -p $INSTALL_DIR

# Déplacer Spark dans le dossier d'installation
mv $SPARK_DIR $INSTALL_DIR

# Créer le fichier spark-env.sh
echo "Création du fichier spark-env.sh..."
cat <<EOL > $INSTALL_DIR/$SPARK_DIR/conf/spark-env.sh.template
#!/usr/bin/env bash

# Configuration Spark
SPARK_MASTER_HOST=192.168.1.94
SPARK_MASTER_PORT=7077
SPARK_MASTER_WEBUI_PORT=8081
SPARK_DAEMON_MEMORY=2g

# Variables additionnelles
# Exemple : HADOOP_CONF_DIR, SPARK_LOCAL_IP, etc.
EOL

# Rendre le fichier exécutable
chmod +x $INSTALL_DIR/$SPARK_DIR/conf/spark-env.sh.template

# Nettoyage du fichier .tgz
rm -f $SPARK_ARCHIVE

echo "Installation terminée ! Spark est installé dans $INSTALL_DIR/$SPARK_DIR"

# Start the Spark worker
echo "Starting Spark worker..."
"$SPARK_HOME/spark-3.5.2-bin-hadoop3/sbin/start-worker.sh" spark://192.168.1.94:7077
