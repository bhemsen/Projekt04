CREATE DATABASE projekt04;
use projekt04

CREATE TABLE `projekt04`.`abteilungen` ( `ID` INT NOT NULL AUTO_INCREMENT ,  `Abteilung` VARCHAR(255) NOT NULL ,    PRIMARY KEY  (`ID`)) ENGINE = InnoDB;
CREATE TABLE `projekt04`.`netze` ( `ID` INT NOT NULL AUTO_INCREMENT ,  `netzadresse` VARCHAR(255) NOT NULL ,  `broadcastadresse` VARCHAR(255) NOT NULL ,  `subnetzmaske` VARCHAR(255) NOT NULL ,  `abteilung` INT NOT NULL ,    PRIMARY KEY  (`ID`)) ENGINE = InnoDB;
CREATE TABLE `projekt04`.`computer` ( `ID` INT NOT NULL AUTO_INCREMENT ,  `name` VARCHAR(255) NOT NULL ,  `abteilung` VARCHAR(255) NOT NULL ,    PRIMARY KEY  (`ID`)) ENGINE = InnoDB;
CREATE TABLE `projekt04`.`adresszuordnung` ( `ID` INT NOT NULL AUTO_INCREMENT ,  `hostadresse` VARCHAR(255) NOT NULL ,  `pc` INT NOT NULL ,  `netz` INT NOT NULL ,    PRIMARY KEY  (`ID`)) ENGINE = InnoDB;


ALTER TABLE `netze` ADD FOREIGN KEY (`abteilung`) REFERENCES `abteilungen`(`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE `computer` ADD FOREIGN KEY (`abteilung`) REFERENCES `abteilungen`(`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE `adresszuordnung` ADD FOREIGN KEY (`pc`) REFERENCES `computer`(`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE `adresszuordnung` ADD FOREIGN KEY (`netz`) REFERENCES `netze`(`ID`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE `netze` ADD UNIQUE( `netzadresse`, `abteilung`);
ALTER TABLE `adresszuordnung` ADD UNIQUE( `hostadresse`, `pc`);
