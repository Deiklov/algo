#include "VectorArray.hpp"

VectorArray::VectorArray(uint64_t _scale_size) {
  arr = new int[0];
  size = 0;
  scale_size = _scale_size;
}

void VectorArray::add(int item, u_int64_t index) {
//  grow array
  assert(index >= 0);

  if (index >= size) {
    auto arr2 = new int[index + scale_size]();//set all memory cells as zero
    // copy old data
    for (int i = 0; i < size; ++i) {
      arr2[i] = arr[i];
    }
    // set new item
    arr2[index] = item;
    // resize
    size = index + scale_size;
    // change pointer to arr
    arr = arr2;
  } else {
    auto arr2 = new int[size + scale_size]();
    for (int i = 0; i < size; ++i) {
      arr2[i] = arr[i];
    }
    arr2[index] = item;

    for (int i = index; i < size + scale_size; ++i) {
      arr2[i + 1] = arr[i];
    }
    arr = arr2;
    size++;
  }

}

string VectorArray::Getstr() {
  string str;
  for (int i = 0; i < size - 1; ++i) {
    str += to_string(arr[i]);
    str += " ";
  }
  str += to_string(arr[size - 1]);
  return str;
}

int VectorArray::remove(u_int64_t index) {
  assert(index < size);
  auto item = arr[index];
  auto arr2 = new int[size - 1]();

  for (int i = 0; i < index; ++i) {
    arr2[i] = arr[i];
  }
  for (int i = index + 1; i < size; ++i) {
    arr2[i - 1] = arr[i];
  }
  size--;
  arr = arr2;
  return item;
}
