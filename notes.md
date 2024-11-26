## Vague idea of structure

Classes:

- Graph
    - Contains the points in the circuit, and is essentially the backend
    - each vertex stores its position, and current "flaminess", as well as time before being able to spread fire
- Graphics
    - Should be able to take a vertex, and its "flaminess" and display it

## How to use:

make your circuit is a png file.
Make the circuit red (255,0,0), and everything else black

In the main function, we put one node on cooldown initially,
ensuring that when the first node is lit, fire only spreads in one way
This worked for the test-circuit,
but depending on your circuit you may want to tweak this aspect

in node.py, there are some coefficients to tweak,
to balance how fast fire spreads, and how fast it
goes out. How long before it can reignite etc.


