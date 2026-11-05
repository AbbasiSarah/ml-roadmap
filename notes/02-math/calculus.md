# Calculus & gradients

*Math for ML* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#calculus)

> **In one sentence:** A derivative says which way is downhill, and gradient descent walks downhill on the error until the model is good.

## Key ideas
- The derivative of a loss with respect to a weight tells how the loss changes if the weight moves a little.
- Gradient = all those derivatives together, pointing uphill; we step the opposite way.
- Learning rate = step size: too big jumps around, too small takes forever.
- The chain rule is backpropagation: gradients flow backwards through layers.

## Example
```python
# minimise f(x) = (x - 3)^2 with gradient descent
x, lr = 0.0, 0.1
for step in range(25):
    grad = 2 * (x - 3)        # derivative of (x-3)^2
    x -= lr * grad
print(round(x, 4))           # ~3.0
```

## Common mistakes
- A learning rate so high the loss explodes. Try 10× smaller.
- Thinking you must do calculus by hand; libraries do it, but you must understand it.

## Learn more
- [3Blue1Brown: Essence of calculus](https://www.3blue1brown.com/topics/calculus) · Free · Video

## Practice project
Use gradient descent to find the minimum of y = (x − 3)² and plot each step.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
