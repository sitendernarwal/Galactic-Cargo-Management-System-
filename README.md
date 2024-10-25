# Galactic Cargo Management System

## Overview

The **Galactic Cargo Management System** is an advanced application designed to efficiently manage the transportation of cargo across various planets in a fictional galaxy. Leveraging the properties of an AVL tree, this system ensures optimal performance for operations related to cargo management, including insertion, deletion, and searching of cargo records. 

## Features

- **Custom AVL Tree Implementation**: A self-balancing binary search tree that maintains order and balance, ensuring efficient operations even with large datasets.
- **Cargo Record Management**: Supports adding, removing, and searching cargo records based on attributes such as cargo ID, destination, and weight.
- **User-Friendly Command-Line Interface**: Intuitive prompts allow users to interact seamlessly with the system.
- **Dynamic Balancing**: Automatic rebalancing of the AVL tree during insertions and deletions to maintain optimal performance.
- **Sorting and Traversal**: Ability to display cargo records in sorted order based on user-defined criteria.

## AVL Tree Implementation

### What is an AVL Tree?

An AVL tree is a type of self-balancing binary search tree where the difference in heights between the left and right subtrees for any node is at most one. This property ensures that the tree remains approximately balanced, allowing for efficient O(log n) time complexity for search, insertion, and deletion operations.

### Key Components of the Custom AVL Tree

1. **Node Structure**: Each node in the AVL tree represents a cargo record, containing:
   - `cargo_id`: Unique identifier for the cargo.
   - `destination`: The destination planet for the cargo.
   - `weight`: The weight of the cargo.
   - `height`: The height of the node for balancing purposes.
   - Pointers to left and right child nodes.

2. **Insertion**: The insert operation includes:
   - Adding a new node in accordance with binary search tree properties.
   - Checking the balance factor of nodes and performing necessary rotations (single or double) to maintain AVL balance.

3. **Deletion**: The delete operation includes:
   - Removing a node while ensuring the AVL tree properties are maintained.
   - Rebalancing the tree after a deletion if needed.

4. **Search**: Efficiently locate a cargo record by its unique ID, ensuring that operations remain efficient even with extensive cargo lists.

5. **Traversal Methods**: In-order traversal displays records in sorted order, while pre-order and post-order traversals allow for different representations of the cargo data.

### Custom Implementation

The AVL tree has been implemented from scratch, showcasing a thorough understanding of data structures and algorithms. The implementation includes:

- **Node Class**: Defines the structure and properties of each node.
- **AVL Tree Class**: Contains methods for:
  - Insertion (`insert`)
  - Deletion (`delete`)
  - Searching (`search`)
  - Rotations (`rotate_left`, `rotate_right`)
  - Balancing (`balance`)
  - Traversals (`in_order`, `pre_order`, `post_order`)

## Getting Started

### Prerequisites

- Python 3.x
- Basic knowledge of command-line operations
- Any code editor (e.g., VSCode, PyCharm)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/galactic-cargo-management-system.git
