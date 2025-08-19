class University 
{
    univ_name(name) 
    {
    this.name = name;
    this.departments = [];
    }

    add_department(dept) 
    {
    this.departments.push(dept);
    }

    remove_department(dept) 
    {
        for (let i = 0; i < this.departments.length; i++) 
        {
            if (this.departments[i] === dept)
            {
                this.departments.splice(i, 1);
            }
        }
    }

  show_departments() 
  {
    console.log("University:", this.name);
    console.log("Departments are:", this.departments);
  }
}

let u = new University();
u.univ_name("Zignuts University");
u.add_department("CSE");
u.add_department("IT");
u.show_departments();
u.remove_department("IT");
u.show_departments();