from abc import ABC, abstractmethod
import random


class CloudSimulator(ABC):

    def __init__(self, provider_name, total_cpu, total_memory):
        self.provider_name = provider_name
        self.total_cpu = total_cpu
        self.total_memory = total_memory

        self.available_cpu = total_cpu
        self.available_memory = total_memory

    @abstractmethod
    def get_metrics(self):
        pass

    def can_run_workload(self, cpu_required, memory_required):
        return (
            self.available_cpu >= cpu_required
            and self.available_memory >= memory_required
        )

    def simulate_workload(self, cpu_required, memory_required):

        if not self.can_run_workload(
            cpu_required,
            memory_required
        ):
            return False

        self.available_cpu -= cpu_required
        self.available_memory -= memory_required

        return True

    def release_workload(self, cpu_required, memory_required):

        self.available_cpu += cpu_required
        self.available_memory += memory_required

        self.available_cpu = min(
            self.available_cpu,
            self.total_cpu
        )

        self.available_memory = min(
            self.available_memory,
            self.total_memory
        )