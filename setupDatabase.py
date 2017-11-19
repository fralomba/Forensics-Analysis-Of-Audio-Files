import pymysql
import sqlInterface

connection = pymysql.connect(host=sqlInterface.host,
							 user=sqlInterface.user,
							 password=sqlInterface.pw,
							 db=sqlInterface.database,
							 charset='utf8mb4',
							 port=sqlInterface.port,
							 cursorclass=pymysql.cursors.DictCursor)
    
query = 'SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";SET time_zone = "+00:00";CREATE TABLE `dataset` ( `groundtruth` varchar(255) NULL, `id` int(16) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=latin1;CREATE TABLE `knownMetadata` (  `id` int(16) NOT NULL,  `name` varchar(255) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=latin1;ALTER TABLE `dataset`  ADD PRIMARY KEY (`id`);ALTER TABLE `knownMetadata`  ADD PRIMARY KEY (`id`);ALTER TABLE `dataset`  MODIFY `id` int(16) NOT NULL AUTO_INCREMENT;ALTER TABLE `knownMetadata`  MODIFY `id` int(16) NOT NULL AUTO_INCREMENT;'
try:
    with connection.cursor() as cursor:
        cursor.execute(query)
    connection.commit()
finally:
    connection.close()
