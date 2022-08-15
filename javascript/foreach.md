# foreach looping

In `JavaScript` there is a better way to loop through an array using [`foreach`][foreach]

```JavaScript
const my_list = [1,2,3,4,5]
my_list.foreach((number) => {
    console.log(`my number ${number}`);
});
```

Another way is to use the let keyword ([source][letloop]):

```JavaScript
const colors = ["Red", "Purple", "Blue"];
for (let color of colors){
  console.log(color)
}```


[foreach]: https://youtube.com/shorts/f8qh7DqTZrM?feature=share
[letloop]: https://youtube.com/shorts/5LhWaN-ubgU?feature=share
