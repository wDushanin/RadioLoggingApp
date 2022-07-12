CREATE DATABASE IF NOT EXISTS radio;

USE radio;

CREATE TABLE IF NOT EXISTS `final`.`rlogs` (
    `log_id` INT NOT NULL AUTO_INCREMENT,
    `time` INT NOT NULL DEFAULT 0,
    `site_num` INT NOT NULL DEFAULT 0,
    `action` VARCHAR(10) NULL DEFAULT NULL,
    `source_type` VARCHAR(10) NULL DEFAULT NULL,
    `source_id` INT NOT NULL DEFAULT 0,
    `target_type` VARCHAR(10) NULL DEFAULT NULL,
    `target_id` INT NOT NULL DEFAULT 0,
    `channel_num` INT NOT NULL DEFAULT 0,
    `call_type` INT NOT NULL DEFAULT 0,
    PRIMARY KEY (`log_id`)
) 
ENGINE = InnoDB 
DEFAULT CHARACTER SET = utf8mb4 
COLLATE = utf8mb4_0900_ai_ci;
