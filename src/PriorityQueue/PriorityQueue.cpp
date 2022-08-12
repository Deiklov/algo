#include "PriorityQueue.hpp"
PriorityQueue::PriorityQueue() {
  first = nullptr;
}
string PriorityQueue::Getstr() {
  return "mda";
}
void PriorityQueue::enqueue(int priority, int item) {
  //added new priory queue to head
  if (first == nullptr) {
    first = new PriorLeaf(priority);
    first->child = new Leaf(item);
    return;
  }
  // maybe not work if prior>first prior
  auto prior_list_elem = first;
  for (; prior_list_elem->prior > priority && prior_list_elem->next != nullptr;
         prior_list_elem = prior_list_elem->next) {}
  //added new priory queue to tail
  if (prior_list_elem->next == nullptr) {
    auto last_prior_leaf = new PriorLeaf(priority);
    last_prior_leaf->child = new Leaf(item);
  } else {
    //added new priory queue to middle
    if (prior_list_elem->next->prior != priority) {
      auto new_prior_leaf = new PriorLeaf(priority);
      new_prior_leaf->child = new Leaf(item);
      new_prior_leaf->next = prior_list_elem->next;
      prior_list_elem->next = new_prior_leaf;
    }
  }

}
int PriorityQueue::dequeue() {
  return 0;
}
