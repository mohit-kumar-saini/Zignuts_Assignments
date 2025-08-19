function sumoffloatingnumbers(str) {
  let arr = str.split(",");
  let s = 0;

  for (let i = 0; i < arr.length; i++) {
    s = s + parseFloat(arr[i]);
  }

  return s;
}

console.log(sumoffloatingnumbers("1.5, 2.3, 3.1, 4, 5.5, 6, 7, 8, 9, 10.9"));