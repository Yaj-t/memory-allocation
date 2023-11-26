class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.keys = []
        self.hits = 0
        self.faults = 0
        self.message = None

    def refer(self, page):
        if page in self.cache:
            # It's a hit since page is already in cache
            self.hits += 1
            self.message = "Hit"
            self.keys.remove(page)
        else:
            # It's a fault since page is not in cache
            self.faults += 1
            self.message = "Fault"
            if len(self.keys) == self.capacity:
                oldest_page = self.keys.pop(0)
                del self.cache[oldest_page]
            self.cache[page] = None
        self.keys.append(page)

    def display(self, current_page):
        print(f"page: {current_page} memory: {self.keys} {self.message} {self.cache} \n")

# Example Usage
if __name__ == "__main__":
    num_frames = 3
    lru_cache = LRUCache(num_frames)

    pages = [1, 2, 3, 4, 2, 1, 5, 6, 3, 1, 2, 5]
    for page in pages:
        lru_cache.refer(page)
        lru_cache.display(page)
    print(f"Hits: {lru_cache.hits} Page Hit percentage: {lru_cache.hits/(lru_cache.hits + lru_cache.faults)} Faults: {lru_cache.faults} ")
