#include "FactorArray.hpp"

FactorArray::FactorArray() {
  arr = new int[0];
  size = 0;
  cap = 0;
  scale_koef = 2;
}

void FactorArray::add(int item, u_int64_t index) {
  assert(index >= 0);
  if (index < size && size == cap) {
    grow();// made x2 for size and cap
  }
  // case then have capacity for paste 1 element
  if (index < size && size < cap) {
    // move elems after index position
    for (int i = size; i > index; --i) {
      arr[i] = arr[i - 1];
    }
    arr[index] = item;
    size++;
    return;
  }

}

string FactorArray::Getstr() {
  string str;
  for (int i = 0; i < size - 1; ++i) {
    str += to_string(arr[i]);
    str += " ";
  }
  str += to_string(arr[size - 1]);
  return str;
}

int FactorArray::remove(u_int64_t index) {
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
// x2 for cap and copy elems, size not change
void FactorArray::grow() {
  if (size == 0) {
    size = 0;
    cap = 1;
    delete[] arr;
    arr = new int[1];
    return;
  }

  auto arr2 = new int[cap *= 2];
  for (int i = 0; i < size; ++i) {
    arr2[i] = arr[i];
  }
  delete[] arr;
}
