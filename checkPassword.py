# checks password vs any number of attempts using yield/send
# Found and solved on codesignal.com

def check_password(attempts, password):
    def check():
        while True:
            attempts_seen = 0
            curr_attempt = yield
            attempts_seen += 1
            if curr_attempt == password:
                yield attempts_seen

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1
