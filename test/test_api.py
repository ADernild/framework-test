import re
import subprocess
import threading
import time


def run_wrk(port, endpoint, output_file):
    command = [
        "wrk",
        "-t12",  # Number of threads
        "-c400",  # Number of connections
        "-d30s",  # Duration in seconds
        f"http://127.0.0.1:{port}{endpoint}",
    ]
    with open(output_file, "w") as f:
        result = subprocess.run(command, capture_output=True, text=True)
        f.write(result.stdout)
        if result.stderr:
            f.write("Error:\n" + result.stderr)


def capture_docker_stats(service_name, duration, output_file):
    command = ["docker", "stats", "--no-stream", service_name]
    cpu_usages = []
    mem_usages = []

    start_time = time.time()
    while (time.time() - start_time) < duration:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.strip().split("\n")
            if len(lines) > 1:  # Skip header
                data = lines[1].split()
                cpu_usage = float(data[2].replace("%", ""))
                mem_usage = re.sub(r"[a-zA-Z]", "", data[3])  # Remove units (e.g., MiB)
                mem_usage = float(mem_usage)

                cpu_usages.append(cpu_usage)
                mem_usages.append(mem_usage)
        time.sleep(1)  # Sample every second

    with open(output_file, "w") as f:
        f.write("CPU Usage:\n")
        f.write(f"  Min: {min(cpu_usages)}%\n")
        f.write(f"  Max: {max(cpu_usages)}%\n")
        f.write(f"  Avg: {sum(cpu_usages) / len(cpu_usages)}%\n\n")
        f.write("Memory Usage:\n")
        f.write(f"  Min: {min(mem_usages)} MiB\n")
        f.write(f"  Max: {max(mem_usages)} MiB\n")
        f.write(f"  Avg: {sum(mem_usages) / len(mem_usages)} MiB\n")


def main():
    services = [
        {
            "name": "framework-test-django-1",
            "port": 8050,
            "endpoint": "/api/sleep-async/",
        },
        {
            "name": "framework-test-django-1",
            "port": 8050,
            "endpoint": "/api/sleep-sync/",
        },
        # {
        #     "name": "framework-test-django-sync-1",
        #     "port": 8053,
        #     "endpoint": "/api/sleep-async/",
        # },
        {
            "name": "framework-test-django-sync-1",
            "port": 8053,
            "endpoint": "/api/sleep-sync/",
        },
        {
            "name": "framework-test-fastapi-1",
            "port": 8051,
            "endpoint": "/api/sleep-async/",
        },
        {
            "name": "framework-test-fastapi-1",
            "port": 8051,
            "endpoint": "/api/sleep-sync/",
        },
        {
            "name": "framework-test-actix_web-1",
            "port": 8052,
            "endpoint": "/api/sleep-async/",
        },
        {
            "name": "framework-test-actix_web-1",
            "port": 8052,
            "endpoint": "/api/sleep-sync/",
        },
    ]

    for service in services:
        match = re.search(r"/api/sleep-(sync|async)/", service["endpoint"])
        if match:
            sync_async_part = match.group(1)
        else:
            sync_async_part = "unknown"

        wrk_output_file = f"logs/{service['name']}_{sync_async_part}_wrk_output.txt"
        stats_output_file = f"logs/{service['name']}_{sync_async_part}_stats_output.txt"

        print(f"Running wrk test and capturing docker stats for {service['name']}...")

        # Create threads
        wrk_thread = threading.Thread(
            target=run_wrk, args=(service["port"], service["endpoint"], wrk_output_file)
        )
        stats_thread = threading.Thread(
            target=capture_docker_stats, args=(service["name"], 30, stats_output_file)
        )  # Duration of the wrk test

        # Start threads
        wrk_thread.start()
        stats_thread.start()

        # Wait for both threads to complete
        wrk_thread.join()
        stats_thread.join()


if __name__ == "__main__":
    main()
