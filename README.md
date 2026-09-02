# KTH Formula Student: Driverless Recruitment Exercises

Repository containing the recruitment assignments for the **KTH Formula Student (Driverless)** team, covering ROS 2 communication nodes, data processing, and visualization tools.

---

## Exercise 1: ROS 2 Communication & PlotJuggler

### Overview
Implementation of two interacting ROS 2 nodes using `rclpy` to demonstrate topic-based publisher-subscriber architecture, message handling, and real-time data visualization.

### Objective
* Learn the fundamental structure of **ROS 2 (Jazzy)** and `rclpy`.
* Implement object-oriented ROS 2 nodes with timers and subscription callbacks.
* Configure ROS 2 package entry points in `setup.py`.
* Monitor and plot live network traffic using **PlotJuggler**.

---

### Node Specifications

* **`nodeA` (`package1`)**
  * **Role:** Publisher
  * **Topic:** `/silman` (`std_msgs/msg/Int64`)
  * **Rate:** $20\text{ Hz}$
  * **Behavior:** Increments a counter $k_{m+1} = k_m + n$ where $k_0 = 4$ and $n = 4$.

* **`nodeB` (`package2`)**
  * **Role:** Subscriber & Publisher
  * **Subscribed Topic:** `/silman`
  * **Published Topic:** `/kthfs/result` (`std_msgs/msg/Float64`)
  * **Behavior:** Receives $k$, computes $r = k / q$ where $q = 0.15$, logs the result, and re-publishes $r$.

---

### Workspace Structure

```text
kthfsdv/
└── src/
    ├── package1/
    │   ├── package1/
    │   │   └── nodeA.py
    │   └── setup.py
    └── package2/
        ├── package2/
        │   └── nodeB.py
        └── setup.py
```

## Exercise 2: Data visualization

### Overview
Computation of functions are interactive visual plotter using math plot library (matplotlib)
# Object-Oriented Mathematical Function Plotter

A Python-based standalone visualization tool that calculates and plots complex periodic functions in real time. Built with an Object-Oriented Programming (OOP) approach using `numpy` and `matplotlib`.

---

## Mathematical Model

The tool visualizes the periodic function $h(t)$:

$$h(t) = 3\pi \cdot e^{-\lambda(t)}$$

where $\lambda(t)$ is defined as:

$$\lambda(t) = 5 \cdot \sin(2\pi \cdot 1 \cdot t)$$

* **Periodicity:** $\lambda(t)$ has a fundamental period of $T = 1.0\text{ s}$.
* **Dynamic Range:** Due to the exponential term $e^{-\lambda(t)}$, $h(t)$ oscillates rapidly between $3\pi \cdot e^{-5} \approx 0.063$ and $3\pi \cdot e^{5} \approx 1398.8$.

---

## Architecture & OOP Design

The script uses class inheritance to separate data generation/math logic from the Graphical User Interface (GUI):

```text
       ┌──────────────────┐
       │   BasePlotter    │  <-- Parent Class (Math & Data)
       └────────┬─────────┘
                │
                ▼
   ┌──────────────────────────┐
   │    InteractivePlotter    │  <-- Child Class (GUI & Rendering)
   └──────────────────────────┘

        
