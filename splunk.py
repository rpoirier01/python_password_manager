import logging
import logging.handlers
import json


#Setup for splunk host, IP and syslog port(udp)

with open("config.json", "r") as file:
    config = json.load(file)
# server_ip = config.get("server_ip"
# splunk_host = "192.168.1" #update to your local
splunk_host = config.get("ip")
splunk_port = 514  

#set up the logger once for the entire application
logger = logging.getLogger("SyslogLogger")
logger.setLevel(logging.DEBUG)  # Allow all logs (DEBUG, INFO, WARNING, ERROR, CRITICAL)

syslog_handler = logging.handlers.SysLogHandler(address=(splunk_host, splunk_port))
logger.addHandler(syslog_handler)



def master_password_error_log():
    try:
        logger.warning("Warning: failed login with master password")
    except Exception as e:
        print("Error occurred while logging transaction: " + e)

def successful_master_login_log():
    try:
        logger.info("Successfully logged in with the master password")   
    except Exception as e:
        print("Error occurred while logging transaction: " + e)

#could update to send a log when a user adds a new, insecure password
def new_password_added_log(username, website):
    try:
        logger.info("Successfully added new password to record with username: " + username + " website: " + website )
    except Exception as e:
        print("Error occurred while logging transaction: " + e)

def user_added_insecure_pw_log(username, website):
    try:
        logger.warning("User has added a password below minimum safety levels with username: " + username + " website: " + website)
    except Exception as e:
        print("Error occurred while logging transaction: " + e)

def user_updated_secure_pw_log(username, website):
    try:
        logger.info("User has updated a password above minimum safety levels with username: " + username + " website" + website)
    except Exception as e:
        print("Error occurred while logging transaction: " + e)

def user_updated_insecure_pw_log(username, website):
    try:
        logger.warning("User has updated a password below minimum safety levels with username: " + username + " website: " + website)
    except Exception as e:
        print("Error occurred while logging transaction: " + e)