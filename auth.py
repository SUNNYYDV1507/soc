from logs import log_event, is_blacklisted, blacklist_ip

USERS = {
    "admin": "admin123"
}

FAILED_LIMIT = 3
failed_attempts = {}

def authenticate(username, password, ip):
    if is_blacklisted(ip):
        return False, "IP Blacklisted"

    if username in USERS and USERS[username] == password:
        failed_attempts[ip] = 0
        log_event(username, ip, "SUCCESS")
        return True, "Login Successful"
    else:
        log_event(username, ip, "FAILED")
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

        if failed_attempts[ip] >= FAILED_LIMIT:
            blacklist_ip(ip)
            return False, "IP Blacklisted due to multiple failures"

        return False, "Invalid Credentials"
