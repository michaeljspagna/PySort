import time
import data_visualizer

class Merge_Sort():
    
    def sort(self, visualizer):
        self.visualizer = visualizer
        self.merge_sort(0, len(self.visualizer.array) - 1)
        
    def merge_sort(self, left, right):
        if left < right: 
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid+1, left)
            self.merge(left, mid, right)
    
    def merge(self, left, mid, right):
        self.visualizer.visualize(self.get_colors(left, mid, right))
        time.sleep(1)
        
        left_slice = self.visualizer.array[left: mid + 1]
        right_slice = self.visualizer.array[mid + 1: right + 1]
        l_idx = 0
        r_idx = 0
        for index in range(left, right + 1):
            if l_idx < len(left_slice) and r_idx < len(right_slice):
                if left_slice[l_idx] <= right_slice[r_idx]:
                    self.visualizer.array[index] = left_slice[l_idx]
                    l_idx += 1
                else:
                    self.visualizer.array[index] = right_slice[r_idx]
                    r_idx += 1
        
            elif l_idx < len(left_slice):
                self.visualizer.array[index] = left_slice[l_idx]
                l_idx += 1
            else:
                self.visualizer.array[index] = right_slice[r_idx]
                r_idx += 1
        self.visualizer.visualize(["#363636" if x >= left and x <= right else "white" for x in range(len(self.visualizer.array))])
        time.sleep(1)
    
    def get_colors(self, left, mid, right):
        colors = []
        for i in range(len(self.visualizer.array)):
            if i >= left and i <= mid:
                colors.append('#CCA43B')
            elif i > mid  and i <= right:
                colors.append('#242F40')
            else:
                colors.append('white')
        return colors