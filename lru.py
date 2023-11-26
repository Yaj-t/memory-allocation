class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity
        self.keys = []
        self.hits = 0
        self.faults = 0
        self.message = None

    def refer(self, page):
        if page in self.keys:
            # It's a hit since page is already in keys
            self.hits += 1
            self.message = "Hit"
            self.keys.remove(page)
        else:
            # It's a fault since page is not in keys
            self.faults += 1
            self.message = "Fault"
            if len(self.keys) == self.capacity:
                oldest_page = self.keys.pop(0)
                index = self.cache.index(oldest_page) 
                self.cache[index] = page
            else:
                self.cache.append(page)
        self.keys.append(page)
        

    def display(self, current_page):
        print(f"page: {current_page} memory: {self.cache} {self.message}\n")

# Example Usage
print(f"LEAST RECENTLY USED")
num_frames = 3
lru_cache = LRUCache(num_frames)

pages = [7,0,1,2,0,3,4,2,3,0,3,2,1,2,0,1,7]
for page in pages:
    lru_cache.refer(page)
    lru_cache.display(page)
    hitPercent = (lru_cache.hits/(lru_cache.hits + lru_cache.faults))*100
    faultPercent = (lru_cache.faults/(lru_cache.hits + lru_cache.faults))*100
print(f"Hits: {lru_cache.hits} Page Hit percentage: {hitPercent:.2f}%")
print(f"Faults: {lru_cache.faults} Page Fault percentage: {faultPercent:.2f}%")
