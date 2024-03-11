import numpy as np

class CascadingBuffersCounter:
    def __init__(self, epsilon, d, threshold, kappa):
        self.epsilon = epsilon
        self.d = d
        self.threshold = threshold
        self.kappa = kappa
        
        # Initialize levels
        self.levels = []
        for i in range(d):
            accumulator = np.random.laplace(0, 1/epsilon)
            buffer_value = 0
            updates_since_flush = 0
            self.levels.append({"accumulator": accumulator, "buffer_value": buffer_value, "updates_since_flush": updates_since_flush})
        
        # Output counter
        self.output_counter = 0
    
    def flush_buffer(self, level_index):
        # Update output counter
        self.output_counter += self.levels[level_index]["accumulator"] + np.random.laplace(0, 1/self.epsilon)
        
        # Reset accumulator, buffer, and updates_since_flush
        self.levels[level_index]["accumulator"] = np.random.laplace(0, 1/self.epsilon)
        self.levels[level_index]["buffer_value"] = 0
        self.levels[level_index]["updates_since_flush"] = 0
    
    def update(self, xt):
        for i in range(self.d):
            # Update accumulator
            self.levels[i]["accumulator"] += xt
            
            # Update buffer value
            self.levels[i]["buffer_value"] += xt + np.random.laplace(0, 1/self.epsilon)
            
            # Increment updates_since_flush
            self.levels[i]["updates_since_flush"] += 1
            
            # Check for buffer overflow or too many updates
            if self.levels[i]["buffer_value"] >= self.threshold or self.levels[i]["updates_since_flush"] >= (self.threshold * self.epsilon / (4 * self.kappa)) ** 2:
                self.flush_buffer(i)
                
        # Update output counter
        self.output_counter += xt + np.random.laplace(0, 1/self.epsilon)
    
    def get_output_counter(self):
        return self.output_counter
