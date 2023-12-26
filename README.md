# Engine

<h2>Basic class</h2>

```python
from Engine import *


class Main(WindowLoop):
    def __init__(self) -> None:
        super().__init__(Vec2(1000, 600), 165)
    
    def update_events(self, __event) -> None:
        if __event.type == KEYDOWN:
            print("key pressed")

        else:
            super().update_events(__event)
    
    def main(self) -> None:
        while True:
            self.update_display()


if __name__ == "__main__":
    Main().main()
```
