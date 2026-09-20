import random

from base_simulator import CloudSimulator


class GCPSimulator(CloudSimulator):

    def __init__(self):
        super().__init__(
            provider_name="GCP",
            total_cpu=32,
            total_memory=64
        )

    def get_metrics(self):

        return {
            "provider": self.provider_name,
            "available_cpu": self.available_cpu,
            "available_memory": self.available_memory,
            "cost_per_hour": round(
                random.uniform(0.28, 0.50),
                3
            ),
            "carbon_intensity": random.randint(
                100,
                300
            ),
            "latency_ms": random.randint(
                50,
                80
            )
        }