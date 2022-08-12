#ifndef ARRAYS__PRIORITYQUEUE_HPP_
#define ARRAYS__PRIORITYQUEUE_HPP_
#include <cstdio>
#include <string>
using namespace std;
struct Leaf {
  int data;
  Leaf *next;
  explicit Leaf(int _data) : data(_data), next(nullptr) {};
};

struct PriorLeaf {
  int prior;
  PriorLeaf *next;
  Leaf *child;
  explicit PriorLeaf(int _prior) : prior(_prior), next(nullptr), child(nullptr) {};
};
class PriorityQueue {
 public:
  PriorLeaf *first;
  explicit PriorityQueue();
  void enqueue(int priority, int item);
  int dequeue();
  string Getstr();
};

#endif //ARRAYS__PRIORITYQUEUE_HPP_
