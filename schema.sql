--Schema for Logging Database
CREATE DATABASE IF NOT EXISTS radio;

USE radio;

CREATE TABLE IF NOT EXISTS `radio`.`rlogs` (
    `log_id` INT NOT NULL AUTO_INCREMENT,
    `time` INT NULL DEFAULT NULL,
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

--Dummy Data

INSERT INTO rlogs (log_id, time, site_num, action, source_type, source_id, target_type, target_id, channel_num, call_type) VALUES ("001", "20220712185319", "259", "Call", "I", "253556", "G", "7014", "259", "4");
INSERT INTO rlogs (log_id, time, site_num, action, source_type, source_id, target_type, target_id, channel_num, call_type) VALUES ("002", "20220713185319", "260", "Call", "I", "253444", "G", "7010", "201", "1");
INSERT INTO rlogs (log_id, time, site_num, action, source_type, source_id, target_type, target_id, channel_num, call_type) VALUES ("003", "20220714185319", "224", "Call", "I", "253543", "G", "7055", "252", "7");
INSERT INTO rlogs (log_id, time, site_num, action, source_type, source_id, target_type, target_id, channel_num, call_type) VALUES ("004", "20220715185319", "259", "Call", "I", "253123", "G", "7001", "212", "9");
INSERT INTO rlogs (log_id, time, site_num, action, source_type, source_id, target_type, target_id, channel_num, call_type) VALUES ("005", "20220716185319", "201", "Call", "I", "253500", "G", "7012", "270", "4")

