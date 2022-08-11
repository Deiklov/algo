#include "FactorArray.hpp"

FactorArray::FactorArray() {
  arr = new int[0]();
  size = 0;
  cap = 0;
  scale_koef = 2;
}

void FactorArray::add(int item, u_int64_t index) {
  assert(index >= 0);
  assert(size <= cap);
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
  if (index >= cap) {
    do {
      grow();
    } while (cap <= index);
    arr[index] = item;
    size = index + 1;
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
  auto ret_data = arr[index];
  // copy right part
  for (int i = index; i < size - 1; ++i) {
    arr[i] = arr[i + 1];
  }
  size--;
  if (size * scale_koef == cap) {
    compress();
  }
  return ret_data;
}
// x2 for cap and copy elems, size not change
void FactorArray::grow() {
  if (size == 0 && cap == 0) {
    size = 0;
    cap = 1;
    delete[] arr;
    arr = new int[1]();
    return;
  }

  auto arr2 = new int[cap *= scale_koef]();
  for (int i = 0; i < size; ++i) {
    arr2[i] = arr[i];
  }
  delete[] arr;
  arr = arr2;
}
void FactorArray::compress() {
  auto arr2 = new int[cap /= scale_koef]();
  for (int i = 0; i < size; ++i) {
    arr2[i] = arr[i];
  }
  delete[] arr;
  arr = arr2;
}