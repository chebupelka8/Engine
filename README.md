# Engine

<h2>Import</h2>

```python
from Engine import *
```

<h2>Basic class</h2>

```python
class Main(WindowLoop):
    def __init__(self) -> None:
        super().__init__(Vec2(1000, 600), 165)
    
    def update_events(self, __event) -> None:
        if __event.type == KEYDOWN:
            print("key pressed")

        else:
            super().update_events(__event)
    
    def main(self) -> None:
        while True: # mainloop
            self.update_display()


if __name__ == "__main__":
    Main().main()
```

<h2>class Player</h2>

```python
from Engine import *


class Player(AnimatedSprite):
    def __init__(self) -> None:
        super().__init__(Vec2(0, 300), AnimationEditor.mult_size(Tileset.split_by_size(Image("source/assets/run.png"), Vec2(32, 32)), 2, 2))

class Main(WindowLoop):
    def __init__(self) -> None:
        super().__init__(Vec2(1000, 600), 165)
    
    def update_events(self, __event) -> None:
        if __event.type == KEYDOWN:
            ...

        else:
            super().update_events(__event)
    
    def main(self) -> None:
        self.player = Player()

        while True:
            self.player.draw(self.display)
            self.player.animating(0.1)

            self.update_display()


if __name__ == "__main__":
    Main().main()
```
