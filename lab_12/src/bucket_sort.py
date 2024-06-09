def insertion_sort(bucket, logging=None):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        if logging is not None:
            logging.append(f"compare {bucket[j]} > {key}: {bucket[j] > key}")
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
            if logging is not None:
                logging.append(f"insert bucket[{j+2}] = bucket[{j+1}]; {bucket[j+2]} = {bucket[j+1]}")
        bucket[j + 1] = key
        if logging is not None:
            logging.append(f"insert bucket[{j + 1}] = {key}")

def bucket_sort(arr, logging=None):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)
        if logging is not None:
            logging.append(f"{num} to bucket {bi}")

    for bi, bucket in enumerate(buckets):
        if bucket:
            if logging is not None:
                logging.append(f"Sort bucket {bi}: {bucket}")
            insertion_sort(bucket, logging)

    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            if logging is not None:
                logging.append(f"arr[{index}] = {num}")
            index += 1

    return arr