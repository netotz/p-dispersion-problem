# Instances

This directory must contain only the generated instances.

## Files

Each instance should be saved in a `*.dat` file.
If other extension is used or the next naming conventions are ignored, the solver won't recognize the file.

### Syntax

#### Title

The title of an instance file must be like `n_p_i.dat` where:

- *n* is the total number of possible locations.

- *p* is the number of facilites to place.

- *i* is the index to distinguish instances that have the same value for both *p* and *n*.

##### Example

The title of an instance with *n* = 40 and *p* = 12  would be `40_12_0.dat`.
If another instance with same values is generated then its name would be `40_12_1.dat`.

#### Content

The content of the file should look as the following:

```text
0 x0 y0
1 x1 y1
...
n xn yn
```

- The first column is the index to identify each location.

- The second and third columns represents the coordinates (*x*, *y*) of each location on a bidimensional space.

##### Example

File `40_12_0.dat`:

```text
0 23 45
1 11 76
...
40 90 35
```
