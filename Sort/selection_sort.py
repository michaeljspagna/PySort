import time
import data_visualizer
class Selection_Sort():
    
    def sort(self, visualizer):
        length = len(visualizer.array)
        for index in range(length):
            min_index = index
            for comparison_index in range(index + 1, length):
                if visualizer.array[comparison_index] < visualizer.array[min_index]:
                    min_index = comparison_index
            visualizer.array[index], visualizer.array[min_index] = visualizer.array[min_index], visualizer.array[index]
            visualizer.visualize(['#CCA43B' if x == index or x == min_index else '#363636' for x in range(length)])
            time.sleep(1)
        visualizer.visualize(['#363636' for x in range(length)])
    
    def get_stats(self):
        space = "O(n)"
        best_time = "Ω(n^2)"
        average_time = "θ(n^2)"
        worst_time = "θ(n^2)"
        sort_in_place = "Yes"
        stable = "No"
        return (space, (best_time, average_time, worst_time), sort_in_place, stable)