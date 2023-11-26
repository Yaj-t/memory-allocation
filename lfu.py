class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []  # Stores the page
        self.frequency = {}  # Stores the frequency of accesses for each page
        self.hits = 0
        self.faults = 0
        self.message = None

    def refer(self, page):
        if page in self.cache:
            # It's a hit
            self.hits += 1
            self.message = "Hit"
            self.frequency[page] += 1
        else:
            # It's a fault
            self.faults += 1
            self.message = "Fault"
            if len(self.cache) == self.capacity:
                # Find the least frequently used page
                lfu_page = min(self.frequency, key=self.frequency.get)
                index = self.cache.index(lfu_page) 
                self.cache[index] = page
                self.frequency.pop(lfu_page)
            else:
                self.cache.append(page)
            self.frequency[page] = 1
        
        
    def display(self, current_page):
        print(f"Page: {current_page} Memory: {self.cache} {self.message}")

    def get_stats(self):
        total_accesses = self.hits + self.faults
        hit_percent = (self.hits / total_accesses) * 100 if total_accesses > 0 else 0
        fault_percent = (self.faults / total_accesses) * 100 if total_accesses > 0 else 0
        return hit_percent, fault_percent

# Example Usage
print("LEAST FREQUENTLY USED")
num_frames = 3
lfu_cache = LFUCache(num_frames)

pages = [7,0,1,2,0,3,4,2,3,0,3,2,1,2,0,1,7]
for page in pages:
    lfu_cache.refer(page)
    lfu_cache.display(page)

hitPercent, faultPercent = lfu_cache.get_stats()
print(f"Hits: {lfu_cache.hits} Page Hit percentage: {hitPercent:.2f}%")
print(f"Faults: {lfu_cache.faults} Page Fault percentage: {faultPercent:.2f}%")
