#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let index = 0;
  let tmp;

  while (len > index) {
    tmp = list[index];
    list[index] = list[len];
    list[len] = tmp;

    len--;
    index++;
  }
  return (list);
};
