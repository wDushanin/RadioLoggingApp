--Schema for Logging Database
--Directions: 
--Copy/Paste this schema into MySQL to create this database
CREATE DATABASE IF NOT EXISTS radio;

USE radio;

CREATE TABLE IF NOT EXISTS `radio`.`rlogs` (
    `log_id` INT NOT NULL AUTO_INCREMENT,
    `time` BIGINT NULL DEFAULT NULL,
    `site_num` INT NULL DEFAULT NULL,
    `action` VARCHAR(10) NULL DEFAULT NULL,
    `source_type` VARCHAR(10) NULL DEFAULT NULL,
    `source_id` INT NULL DEFAULT NULL,
    `target_type` VARCHAR(10) NULL DEFAULT NULL,
    `target_id` INT NULL DEFAULT NULL,
    `channel_num` INT NULL DEFAULT NULL,
    `call_type` INT NULL DEFAULT NULL,
    PRIMARY KEY (`log_id`)
) 
ENGINE = InnoDB 
DEFAULT CHARACTER SET = utf8mb4 
COLLATE = utf8mb4_0900_ai_ci;

