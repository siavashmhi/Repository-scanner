# init_db.sh
#!/bin/bash

# Wait until MySQL is ready
until mysql -h "db" -P 3306 -u"root" -p"siavash" -e "SHOW DATABASES;" > /dev/null 2>&1; do
  echo "Waiting for database connection..."
  sleep 2
done

# Create the database if it doesn't exist
echo "Creating database if not exists..."
mysql -h "db" -P 3306 -u"root" -p"siavash" -e "CREATE DATABASE IF NOT EXISTS flask_db;"

