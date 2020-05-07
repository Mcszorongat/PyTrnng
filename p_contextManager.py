from contextlib import closing

class refrigeratorRaider:
    
    def open(self):
        print("Open refrigerator.")

    def take(self, food):
        print(f"Finding {food}...")
        if food == "deep fried pizza":
            raise RuntimeWarning("Health warning!")
        print(f"Taking {food}...")

    def close(self):
        print("Close refrigerator.")

def raid(food):
    with closing(refrigeratorRaider()) as r:
        r.open()
        r.take(food)
        # r.close()   <-- context manager closes anyway


if __name__=='__main__':
    raid('bacon')
    print("\n")
    raid('deep fried pizza')