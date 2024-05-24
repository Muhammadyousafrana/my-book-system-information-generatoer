import platform
import psutil


def get_system_info():
    # System Information
    print("System Information:")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Hostname: {platform.node()}")
    print(f"Python Version: {platform.python_version()}")

    # CPU Information
    print("\nCPU Information:")
    cpufreq = psutil.cpu_freq()
    print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
    print(f"Total Cores: {psutil.cpu_count(logical=True)}")
    print(f"Max Frequency: {cpufreq.max:.2f} MHz")
    print(f"Min Frequency: {cpufreq.min:.2f} MHz")
    print(f"Current Frequency: {cpufreq.current:.2f} MHz")
    print(f"CPU Usage: {psutil.cpu_percent()}%")

    # Memory Information
    print("\nMemory Information:")
    svmem = psutil.virtual_memory()
    print(f"Total: {svmem.total / (1024 ** 3):.2f} GB")
    print(f"Available: {svmem.available / (1024 ** 3):.2f} GB")
    print(f"Used: {svmem.used / (1024 ** 3):.2f} GB")
    print(f"Percentage Used: {svmem.percent}%")

    # Disk Information
    print("\nDisk Information:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Device: {partition.device}")
        print(f"Mountpoint: {partition.mountpoint}")
        print(f"File System Type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # Skip if permission is denied
            continue
        print(f"Total Size: {partition_usage.total / (1024 ** 3):.2f} GB")
        print(f"Used: {partition_usage.used / (1024 ** 3):.2f} GB")
        print(f"Free: {partition_usage.free / (1024 ** 3):.2f} GB")
        print(f"Percentage Used: {partition_usage.percent}%")

    # Network Information
    print("\nNetwork Information:")
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"Interface: {interface_name}")
            print(f"Address Family: {address.family}")
            print(f"IP Address: {address.address}")
            print(f"Netmask: {address.netmask}")
            if address.broadcast:
                print(f"Broadcast IP: {address.broadcast}")
            print()


if __name__ == "__main__":
    get_system_info()
