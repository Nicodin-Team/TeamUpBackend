import redis

try:
    # Adjust the host and port if your Redis server is running elsewhere
    r = redis.StrictRedis(host='127.0.0.1', port=6379)
    response = r.ping()
    print(response)
    if response:
        print(response)
        print("Connected to Redis successfully!")
    else:
        print("Failed to connect to Redis.")
except Exception as e:
    print(f"Error: {e}")
