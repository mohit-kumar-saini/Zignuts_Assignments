function sumofstringnumbers(str) 
{
    let s = 0;
    for (let i = 0; i < str.length; i++)
    {
        if (!isNaN(str[i]) && str[i] !== " ") 
        {
            s = s + parseInt(str[i]);
        }
    }
    return s;
}
console.log(sumofstringnumbers("foo8bar8cat2tc2")); 