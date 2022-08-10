#include "SingleArray.hpp"

 int SingleArray::remove(int index) {
  return 0;
}
SingleArray::SingleArray() {
  arr = new int[0];
  size = 0;
}
void SingleArray::add(int item, int index) {
//  grow array
  if (index >= size) {
    auto arr2 = new int[index + 1];
    for (int i = 0; i < size; ++i) {
      arr2[i] = arr[i];
    }
    arr2[index] = item;
    size++;
  }
//  replace elements
  if (index < size) {
    auto arr2 = new int[size + 1];
    for (int i = 0; i < size; ++i) {
      arr2[i] = arr[i];
    }
    arr2[index] = item;

    for (int i = index; i < size + 1; ++i) {
      arr2[i + 1] = arr[i];
    }
  }
}
void SingleArray::print() {
  for (int i = 0; i < size; ++i) {
    printf("%d", arr[i]);
  }
}
