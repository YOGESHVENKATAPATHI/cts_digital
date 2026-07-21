class Workstation:
    def __init__(self):
        self.processor = ""
        self.memory = ""
        self.disk = ""

    def display_specs(self):
        print(f"Processor: {self.processor}")
        print(f"Memory: {self.memory}")
        print(f"Disk: {self.disk}")


class WorkstationAssembler:
    def __init__(self):
        self.workstation = Workstation()

    def configure_processor(self, processor_model):
        self.workstation.processor = processor_model

    def configure_memory(self, memory_size):
        self.workstation.memory = memory_size

    def configure_disk(self, disk_size):
        self.workstation.disk = disk_size

    def fetch_workstation(self):
        return self.workstation


if __name__ == "__main__":
    assembler = WorkstationAssembler()
    
    assembler.configure_processor("AMD Ryzen 9")
    assembler.configure_memory("32 GB")
    assembler.configure_disk("1 TB NVMe")
    
    built_pc = assembler.fetch_workstation()
    built_pc.display_specs()