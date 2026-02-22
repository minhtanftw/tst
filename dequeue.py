def introduce(**kwargs):
    details = []
    for k,v in kwargs.items():
        details.append(k + ":" + str(v))
    return ",".join(details)

print(introduce(name = "alice", age = 25, city ="New York"))