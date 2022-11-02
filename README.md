# PythonSQLconnector

docker network create test
docker network ls
docker run -d --net test --name db -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=test mysql:latest
docker ps
docker run --rm --net test -e DB_HOST=db -e DB_USER=root -e DB_PASSWORD=root -e DATABASE=test pardeshispavan/sql-db-connector:latest
docker images
docker ps -a
docker restart db
docker run --rm --net test -e DB_HOST=db -e DB_USER=root -e DB_PASSWORD=root -e DATABASE=test pardeshispavan/sql-db-connector:latest
docker inspect db
docker run --rm --net test -e DB_HOST=172.18.0.2 -e DB_USER=root -e DB_PASSWORD=root -e DATABASE=test pardeshispavan/sql-db-connector:latest
docker run --rm --net test -e DB_HOST=172.18.0.3 -e DB_USER=root -e DB_PASSWORD=root -e DATABASE=test pardeshispavan/sql-db-connector:latest
docker run --rm --net test -e DB_HOST=db2 -e DB_USER=root -e DB_PASSWORD=root -e DATABASE=test pardeshispavan/sql-db-connector:latest
