import time
import data_visualizer
class Bubble_Sort():
    
    def sort(self, visualizer):
        length = len(visualizer.array)
        for _ in range(length - 1):
            for j in range(length - 1):
                if visualizer.array[j] > visualizer.array[j + 1]:
                    visualizer.array[j], visualizer.array[j+1] = visualizer.array[j+1], visualizer.array[j]
                    visualizer.visualize(['#CCA43B' if x == j or x == j+1 else '#363636' for x in range(length)])
                    time.sleep(1)
        visualizer.visualize(['#363636' for x in range(length)])
        
    def get_stats(self):
        space = "O(n)"
        best_time = "Ω(n)"
        average_time = "θ(n^2)"
        worst_time = "O(n^2)"
        sort_in_place = "Yes"
        stable = "Yes"
        return (space, (best_time, average_time, worst_time), sort_in_place, stable)