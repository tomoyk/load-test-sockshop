sec_req = {}
with open("summary_1min_1202.txt") as f:
    lines = f.read().splitlines()
    for l in lines:
        try:
            fields = l.split("\t")
            time_ = fields[0].split(" ")[1]
            hm = time_.split(":")
            seconds = int(hm[0]) * 3600 + int(hm[1]) * 60
            # print(datetime)
            sec_req[seconds] = int(fields[1])
        except Exception:
            continue

if __name__ == "__main__":
    import json
    print(json.dumps(sec_req))
