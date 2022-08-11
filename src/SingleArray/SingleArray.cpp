#include "SingleArray.hpp"

SingleArray::SingleArray() {
  arr = new int[0];
  size = 0;
}
void SingleArray::add(int item, u_int64_t index) {
//  grow array
  if (index >= size) {
    auto arr2 = new int[index + 1];
    for (int i = 0; i < size; ++i) {
      arr2[i] = arr[i];
    }
    arr2[index] = item;
    size = index + 1;
    arr = arr2;
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
    arr = arr2;

  }

}

void SingleArray::print() {
  for (int i = 0; i < size; ++i) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}
int SingleArray::remove(u_int64_t index) {
  return 0;
}
