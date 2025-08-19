class Shape 
{
  area() 
  {
    return 0;
  }
}

class Circle extends Shape 
{
  area(r) 
  {
    return 3.14 * r * r;
  }
}

class Triangle extends Shape 
{
  area(b, h) 
  {
    return 0.5 * b * h;
  }
}

let c = new Circle();
console.log("Circle area:", c.area(5)); 

let t = new Triangle();
console.log("Triangle area:", t.area(10, 5)); 
